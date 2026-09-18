# Visual Identity

Personal design language for slides, decks, diagrams, carousels, articles, and all visual artifacts.
Inspired by Anthropic/Claude's warm editorial aesthetic. Adapted with preferred typefaces.

**This is the default for every visual artifact.** Apply it without asking and without
running a style exploration. Depart from it only when Eric asks for something else, or
when the subject carries its own visual argument this identity would fight (a talk about
a specific brand, an era, another company's product). When you depart, say so in one line
and name the reason.

General Sans is not on Google Fonts and its license forbids uploading the files to a
public server, so load it from the Fontshare API. Use the Fontshare API for web delivery.

---

## Fonts

| Role | Family | Fallback | Weight | Google Fonts |
|------|--------|----------|--------|--------------|
| **Display / Headlines** | Newsreader | Georgia, serif | 400–600 | `Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600` |
| **Body / UI** | General Sans | system-ui, -apple-system, sans-serif | 300–600 | Fontshare API (Indian Type Foundry) |
| **Code / Data** | JetBrains Mono | ui-monospace, SFMono-Regular, Menlo, monospace | 400–500 | `JetBrains+Mono:wght@400;500` |

### Implementation

```html
<!-- Newsreader + JetBrains Mono via Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

<!-- General Sans via Fontshare API (not on Google Fonts; do not self-host, see license) -->
<link href="https://api.fontshare.com/v2/css?f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet">
```

Verify after deploying, rather than trusting the tags. On a machine with the font
installed locally a check can pass while remote visitors get the fallback, so inspect successful font-file requests in the browser Network panel as well as loaded faces. The following checks loaded faces only; it does not establish network delivery:

```js
(async () => { await document.fonts.ready;
  return [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family); })()
```

```css
:root {
  --font-serif: 'Newsreader', Georgia, 'Times New Roman', serif;
  --font-sans: 'General Sans', system-ui, -apple-system, 'Segoe UI', sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
}
```

### Typography Scale

| Role | Font | Size | Weight | Line Height | Notes |
|------|------|------|--------|-------------|-------|
| Display | Newsreader | 64px (4rem) | 500 | 1.10 | Hero headlines, title slides |
| Section Heading | Newsreader | 48px (3rem) | 500 | 1.20 | Major section anchors |
| Sub-heading | Newsreader | 32px (2rem) | 500 | 1.25 | Card titles, feature names |
| Sub-heading Small | Newsreader | 24px (1.5rem) | 500 | 1.30 | Smaller titles |
| Body Large | General Sans | 20px (1.25rem) | 400 | 1.60 | Intro paragraphs |
| Body | General Sans | 16px (1rem) | 400 | 1.60 | Standard body text |
| Body Small | General Sans | 14px (0.875rem) | 400 | 1.50 | Captions, metadata |
| Label | General Sans | 12px (0.75rem) | 500 | 1.25 | Badges, overlines |
| Code | JetBrains Mono | 15px (0.94rem) | 400 | 1.60 | Code blocks, data |

### Principles

- Serif for authority, sans for utility. Newsreader carries all headlines. General Sans handles UI and body.
- Single weight for serifs: all Newsreader headings use 500. Consistent voice.
- Relaxed body line-height (1.60): reading experience closer to a book than a dashboard.
- Tight headline line-height (1.10–1.30): serif letterforms need room but not excess.
- No bold serif. Emphasis through size and spacing, not weight.

---

## Color Palette

Warm neutrals throughout. Every gray has a yellow-brown undertone. No cool blue-grays.

### Core

| Name | Hex | Role |
|------|-----|------|
| Near Black | `#141413` | Primary text, dark surfaces |
| Terracotta | `#c96442` | Brand accent, CTAs, emphasis |
| Coral | `#d97757` | Secondary accent, links on dark |
| Parchment | `#f5f4ed` | Primary background (light) |
| Ivory | `#faf9f5` | Card surfaces, elevated containers |

### Neutrals

| Name | Hex | Role |
|------|-----|------|
| Charcoal Warm | `#4d4c48` | Primary dark-on-light text |
| Olive Gray | `#5e5d59` | Secondary body text |
| Stone Gray | `#87867f` | Tertiary text, footnotes |
| Warm Silver | `#b0aea5` | Text on dark surfaces |
| Warm Sand | `#e8e6dc` | Button backgrounds, borders |

### Surfaces

| Name | Hex | Role |
|------|-----|------|
| Deep Dark | `#141413` | Dark-theme background |
| Dark Surface | `#30302e` | Dark-theme containers |
| Border Cream | `#f0eee6` | Light borders (barely visible) |
| Border Warm | `#e8e6dc` | Prominent borders, dividers |

### Semantic

| Name | Hex | Role |
|------|-----|------|
| Error | `#b53333` | Error states |
| Focus | `#3898ec` | Focus rings only (the sole cool color) |

### CSS Variables

```css
:root {
  /* Backgrounds */
  --bg-primary: #f5f4ed;
  --bg-surface: #faf9f5;
  --bg-dark: #141413;
  --bg-dark-surface: #30302e;

  /* Text */
  --text-primary: #141413;
  --text-secondary: #5e5d59;
  --text-tertiary: #87867f;
  --text-on-dark: #b0aea5;

  /* Brand */
  --accent: #c96442;
  --accent-light: #d97757;

  /* Borders */
  --border-light: #f0eee6;
  --border-medium: #e8e6dc;
  --border-dark: #30302e;

  /* Semantic */
  --error: #b53333;
  --focus: #3898ec;
}
```

---

## Design Principles

1. **Warm, not cold.** Every neutral skews yellow-brown. No pure grays, no blue undertones.
2. **Editorial, not corporate.** Serif headlines give book-title gravitas. Feels like reading an essay.
3. **Gradient-free.** Depth comes from surface layering and section alternation (light/dark), not gradients.
4. **Ring shadows over box shadows.** Use `0px 0px 0px 1px` patterns for containment. Whisper-soft shadows only for elevation.
5. **Dense when it serves the story.** Don't dumb down to look clean. Clarity over minimalism.
6. **Parchment, not screen.** The background should feel like quality paper, not a digital canvas.

---

## Components

### Buttons

| Variant | Background | Text | Radius |
|---------|-----------|------|--------|
| Primary (brand) | `#c96442` | `#faf9f5` | 8px |
| Secondary | `#e8e6dc` | `#4d4c48` | 8px |
| Dark | `#30302e` | `#faf9f5` | 8px |
| Ghost | transparent | `#141413` | 8px |

### Cards

- Background: Ivory on light, Dark Surface on dark
- Border: 1px solid Border Cream (light) or Border Dark (dark)
- Radius: 8px standard, 16px featured, 32px hero
- Shadow: `rgba(0,0,0,0.05) 0px 4px 24px` for elevation

### Spacing

- Base unit: 8px
- Section padding: 64–96px vertical
- Content max-width: 1200px
- Card gap: 24px

### Marker Highlight

A highlighter-pen emphasis for a key phrase inside a headline or body line. The color fills only the lower portion of the text height, so it reads like a hand-drawn marker swipe under the words rather than a solid filled box. Use sparingly: one phrase per headline, the single idea you want the eye to land on.

The trick is a hard-stop linear gradient as the background, transparent on top, color on the bottom ~40%.

```css
.marker {
  background: linear-gradient(transparent 60%, var(--marker) 60%);
  padding: 0 2px;        /* a little breathing room around the swipe */
  box-decoration-break: clone;          /* the swipe wraps cleanly across line breaks */
  -webkit-box-decoration-break: clone;
}
```

```html
<h1>The one phrase that <span class="marker">earns the highlight</span>.</h1>
```

Tuning:
- **Swipe height.** The two `60%` stops control where the marker starts. Raise to `68%` for a thin underline-like swipe, lower to `50%` for a bolder half-fill. Keep both stops equal so the edge stays crisp.
- **Color.** Default marker is a warm wash, not neon. Use a pale tint of the accent so it stays editorial: `--marker: #f3d9b0` (warm amber) or a 15–20% Terracotta tint. Avoid pure yellow; it reads digital, not paper.
- **One per view.** The effect dies if repeated. If two phrases both feel essential, the sentence needs a rewrite, not two markers.

```css
:root {
  --marker: #f3d9b0;   /* warm amber highlighter; warm-palette safe */
}
```

---

## Usage

This file is the source of truth for all visual output: slides, diagrams, social graphics, landing pages, investor updates, carousels.

Reference this before creating any visual artifact. When in doubt: warm, editorial, dense-but-clear.

*Design is the clarity of thought made visible.*
