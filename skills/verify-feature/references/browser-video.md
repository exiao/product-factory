# Browser video

Use the running application URL and observed controls. Set up the local app, test account or existing authenticated state before recording; do not substitute a component demo because it is easier to record. Keep real store purchases and other external writes within the task's authorization.

## shot-scraper

Check availability and the installed version's commands:

```bash
command -v shot-scraper
shot-scraper --version
shot-scraper video --help
```

Prefer its video command when available. If the installed version lacks it, record that limitation and use existing Playwright recording. Do not install or upgrade automatically.

`shot-scraper video storyboard.yml --mp4` records WebM and also creates MP4 using ffmpeg. Storyboards support page navigation, selector waits, clicks, typing, scrolling and pauses. `cursor: true` makes actions visible with a cursor and click rings.

This read-only example comes from the official documentation. For feature verification, replace the URL and controls with the actual application and selectors inspected from its running UI; name the real entry, action and resulting state.

```yaml
output: demo.webm
url: https://shot-scraper.datasette.io/en/stable/
viewport:
  width: 1280
  height: 720
cursor: true
wait_for: "text=Quick start"
scenes:
  - name: Documentation home
    do:
      - pause: 1
  - name: Open installation docs
    do:
      - click: '.sidebar-tree a[href="installation.html"]'
      - wait_for: 'h1:has-text("Installation")'
      - pause: 2
```

Source: [Recording videos](https://shot-scraper.datasette.io/en/stable/video.html). Check current documentation when changing storyboard syntax or using options outside this example.

## Playwright fallback

Reuse existing journey automation where it already drives the actual app. Set the viewport and recording size to match, close the browser context to flush the video, and inspect the exported file. Keep each recording at one viewport; use separate clips for desktop, mobile or short-screen checks.

For either recorder, begin at a meaningful ready state, show the action and leave the result readable. Retain originals when trimming setup. Separate supplemental fixture/harness captures from actual-app evidence, identify replaced boundaries, and report unverified branches explicitly.
