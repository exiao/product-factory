# Selected code examples

Use these examples after routing to the matching named rule. Confirm the framework and library in the target code before applying a pattern.

## `container-two-div-pattern`

Incorrect, measuring and animating the same node creates a measurement feedback loop:

```tsx
const [ref, bounds] = useMeasure();
return <motion.div ref={ref} animate={{ height: bounds.height }}>{children}</motion.div>;
```

Correct, the inner node is measured while the outer node owns the animated bounds:

```tsx
const [ref, bounds] = useMeasure();
return (
  <motion.div animate={{ height: bounds.height }} style={{ overflow: "hidden" }}>
    <div ref={ref}>{children}</div>
  </motion.div>
);
```

Pair this with `container-guard-initial-zero` when the first measurement can be zero.

## `exit-key-required` and `presence-safe-to-remove`

Incorrect, an index key can attach the wrong exit state after removal, and async cleanup never releases the presence node:

```tsx
<AnimatePresence>
  {items.map((item, index) => <motion.div key={index} exit={{ opacity: 0 }} />)}
</AnimatePresence>
// usePresence cleanup runs, but safeToRemove is never called
```

Correct, use stable identity and finish the lifecycle after cleanup:

```tsx
function Row({ item }: { item: Item }) {
  const [isPresent, safeToRemove] = usePresence();
  useEffect(() => {
    if (!isPresent) {
      void cleanup(item).catch(reportCleanupError).finally(() => safeToRemove?.());
    }
  }, [isPresent, item, safeToRemove]);
  return <motion.div exit={{ opacity: 0 }}>{item.label}</motion.div>;
}

<AnimatePresence>
  {items.map((item) => <Row key={item.id} item={item} />)}
</AnimatePresence>
```

The example assumes `cleanup` is idempotent and `reportCleanupError` records failures without throwing. If cleanup can race with re-entry, cancel or ignore stale completion before releasing the node.

Apply Motion-specific IDs only when `AnimatePresence`/`usePresence` is present.

## `ux-hover-touch-path`

Incorrect, a hover-only control has no keyboard or touch path:

```css
.card-actions { opacity: 0; }
.card:hover .card-actions { opacity: 1; }
```

Correct, expose the same action on focus and on a touch-capable device with an explicit toggle or always-visible placement:

```css
.card-actions { opacity: 0; pointer-events: none; }
.card:hover .card-actions,
.card:focus-within .card-actions { opacity: 1; pointer-events: auto; }
@media (hover: none) {
  .card-actions { opacity: 1; pointer-events: auto; }
}
```

The CSS is only the reveal. Verify the control can be reached by Tab, opened on touch, and dismissed without trapping focus.

## `ux-card-link-layering`

Incorrect, a positioned wrapper changes the containing block for a stretched link and can shrink the clickable card:

```css
.card-footer { position: relative; }
.card-link::after { content: ""; position: absolute; inset: 0; }
```

Correct, keep the card link's containing block on the card and raise inner controls above it:

```css
.card { position: relative; }
.card-footer { display: flex; }
.card-footer button,
.card-footer a:not(.card-link) { position: relative; z-index: 1; }
.card-link::after { content: ""; position: absolute; inset: 0; }
```

Keep `.card-link` itself unpositioned so its pseudo-element uses `.card` as the containing block. Confirm no intermediate positioned ancestor overrides that relationship.

## `ux-refresh-preserves-input`

Incorrect, replacing the editing subtree during polling discards the user's draft and focus:

```tsx
return <Editor key={serverVersion} value={draft} onChange={setDraft} />;
```

Correct, keep the editor identity stable and merge server changes outside the active draft:

```tsx
return <Editor value={draft} onChange={setDraft} aria-busy={refreshing} />;
```

Verify during an actual refresh with text selected and focus inside the editor. The rule is about observed preservation, so do not infer it from a screenshot.
