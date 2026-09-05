# Signal & Craft

Direction and approval of the design brief: **Hassan**. Design, implementation, verification, and documentation: **Codex**.

Local preview: http://127.0.0.1:8874/ and http://127.0.0.1:8874/selected-work.html. Start it again with `python3 -m http.server 8874 --bind 127.0.0.1` from the repository root.

Work lives on `codex/signal-and-craft`, based on `7e34a70bfac784a881a7cfdabdf8622a9ffba8fd`. Local tags `signal-and-craft-before` and `signal-and-craft-after` identify the comparison revisions. No merge, push, or deployment was performed; these require Hassan’s explicit approval.

## Design and accepted revisions

The pages use a cyan-lit, dimensional consulting identity, with generous reading space and a direct booking action. Three repeated treatments connect the site: framed hero artwork, illuminated project frames, and quieter editorial reading sections.

Hassan replaced the particle request with rich block transitions and scroll parallax. There is no particle canvas or animation dependency. Each main section receives an entrance treatment; cards and project frames receive staggered emphasis and decorative depth. Desktop scrolling moves chapter lighting and heading accents, while videos, screenshots, PDFs, installer text, and controls retain their layout geometry. The maximum decorative movement is 24 px for chapters and 12 px for cards. Hero pointer tilt is capped at ±4°.

The resume is near the top, after the hero and proof strip. The press strip retains the original logo artwork in a larger continuous row with a pause control. Homepage content continues through the Selected Work gateway, ClineFlow, Meme Arcade, Apple recognition, citations, books, interviews, press, biography, and contact. Selected Work has its own introduction and section index, followed by the existing work.

Meme Arcade uses sans-serif typography only within that section, a rounded-square app-icon treatment of the approved artwork, and a single carousel on the right on desktop. Controls are small visually but have 44 px targets. Slides advance every 3 seconds while visible. Pointer interaction, keyboard focus, pagination, arrows, or swipes stop autoplay until Play is explicitly selected. Hover temporarily pauses it. Mobile stacks the copy before the carousel.

The fixed booking overlay was replaced by header and in-flow contact actions. The existing consultation destination and UnidosUS statement/link remain. Existing routes, IDs, legacy hash redirects, metadata, downloads, media, and historical standalone pages are preserved.

## Motion and accessibility

- One demand-driven requestAnimationFrame scheduler coalesces pointer and scroll input. Geometry is cached and refreshed on resize/content-size changes; only nearby observed layers update. There is no idle rendering loop.
- Short browser-native entrances run once, pause offscreen/hidden/under the menu, and release their transforms when finished or focused. Decorative border and chapter-line animations follow the same visibility policy.
- Mobile and coarse-pointer devices retain static layered framing and short 8 px / 360 ms entrances. They have no scroll parallax or pointer tilt. Video and PDF hit areas never rotate.
- System reduced motion and a persistent manual toggle disable entrances, parallax, automatic carousel motion, and marquee movement. Failed storage access does not break the page.
- A sustained-performance fallback samples requested desktop frames only. At least 12 delays over 50 ms in 20 samples removes the light background and halves depth movement; a second poor sample window disables motion for that page visit. Idle time does not count as a slow frame.
- The modal menu contains focus, handles Escape, restores focus, closes on selection, locks/unlocks body scrolling, and cleans up when resizing to desktop. Skip navigation, measured header clearance, focus rings, and clipboard status feedback were added.
- Content starts visible; enhancements never depend on a hidden-by-default reveal class. Without scripts, navigation, content, downloads, and all three carousel images remain available. A failed PDF canvas retains the image preview and download link.

## Source and assets

All page changes originate in `generator/`. `generate.py` now composes explicit page sections instead of slicing a rendered document by comments. Shared styles live in `templates/css.py`; shared interactions and the deferred PDF viewer live in `templates/scripts.py`. Generated root HTML is reproducible output.

All existing portraits, logos, screenshots, and covers were reused. No generated imagery, external replacement artwork, or hand-edited image manifest was introduced. Four responsive variants were produced exclusively with `optimize_images.py` from the tracked approved WebPs. The manifest records their sources, dimensions, settings, and fingerprints.

| Variant | Dimensions | Bytes |
| --- | --- | ---: |
| portrait-small | 320 × 570 | 21,036 |
| clineflow-hero-small | 640 × 360 | 57,800 |
| bio-profile-small | 640 × 360 | 17,904 |
| resume-preview-small | 640 × 828 | 111,754 |

The image helper emits manifest-backed `srcset` and `sizes`; verification checks every candidate and width descriptor. The sum of unique full-size image fallback resources is **1,447,366 bytes on the homepage** and **355,494 bytes on Selected Work**, below the 1.45 MB and 0.36 MB decimal budgets. The hero portrait is 51,628 bytes full size or 21,036 bytes for the small candidate, below the 150 KB first-viewport image budget. These are image-resource budgets, not total page transfer including fonts, PDF.js, or third-party players. Dimensions are reserved; appropriate images/iframes and PDF initialization are deferred.

`generator/video_metadata.json` records the public Vimeo/YouTube oEmbed dimensions and source endpoints used for all 20 videos. Frames use those ratios rather than a universal 16:9 box. TwinChat and BTwin are square; the reel and several older videos use 4:3; Onelapse uses 638:426. Provider player dimensions can include their own letterboxing and should be refreshed if the source video changes. Media URLs were preserved; no video files were downloaded.

## Verification evidence

Run from the repository root:

```sh
python3 generator/generate.py
python3 generator/verify_image_assets.py
python3 -m unittest discover -s generator/tests -p 'test_*.py'
node generator/tests/test_interactions.cjs
git diff --check
```

Seven Python regressions cover generated-output equality, landmarks and destinations against the baseline, resume order, image budgets, provider video dimensions, and no-script carousel content. Nine deterministic JavaScript controller checks cover the 3-second timer, interaction closure, hidden/offscreen resume, reduced motion, unavailable storage, entrance cleanup, keyboard pagination, bounded/coalesced mobile-safe parallax, and degraded performance.

Browser checks used the Codex in-app browser on macOS, with viewport emulation. Both pages passed 320, 390, 768, 1024, 1440, and 1920 px widths with no document overflow or measured text/control bounds outside the viewport: [layout results](layout-results.json). Portrait/landscape changes at 390 × 844 and 844 × 390 preserved layout and cleaned up an open menu. Root text enlarged to 200% (32 px) passed 320, 390, and 1440 px on both pages without measured text clipping: [enlargement results](text-enlargement-results.json).

Browser interaction checks covered menu Escape, focus wrap/restoration, disclosure state, section selection, resize cleanup, persistent reduced motion, copy success and failure, carousel interaction pause, PDF paging, and actual iframe ratios. All 17 Selected Work frames matched their recorded ratios within subpixel rounding; square mobile frames measured 340 × 340 px. Local download targets exist and baseline content destinations pass regression checks.

Controlled ignored QA fixtures exercised a failed image (reserved box and readable hero), failed clipboard access (manual-copy feedback), failed PDF canvas (preview and download remain), and stripped scripts (three visible carousel images and fallback navigation). These are fixture simulations, not claims that browser settings or a physical device were changed. Offscreen/hidden timing and poor frame scheduling are additionally exercised by deterministic controller tests.

| Local sample | Frames | Mean interval | p95 interval | Intervals >50 ms | Observed CLS |
| --- | ---: | ---: | ---: | ---: | ---: |
| Baseline hero | 179 | 8.33 ms | 9.30 ms | 0 | 0 |
| Final hero | 179 | 8.33 ms | 9.10 ms | 0 | 0 |
| Final anchor scroll / section entrance | 179 | 8.33 ms | 9.30 ms | 0 | 0 |

Raw readings: [before](performance-before.json), [after](performance-after.json), [scroll](performance-scroll.json). The sampling script is [measure_frames.js](measure_frames.js), injected only into ignored local QA copies. Hero comparisons used 1440 × 900 at reported DPR 2; the separate scroll run reported DPR 1. This measures local requestAnimationFrame delivery on a high-refresh desktop, with warmed caches and third-party video playback stopped. It is not a physical-phone FPS benchmark, cold-load measurement, LCP result, or proof of performance on every device. Resource transfer fields exclude cached/cross-origin details and must not be interpreted as full network weight.

## Matched captures

The four primary pairs use 1440 × 900 desktop and 390 × 844 mobile, with scroll position 0, default motion enabled, entrances settled, and no external-media playback. All eight primary captures reported DPR 1. Screenshot output is one image pixel per CSS pixel. [Capture records](capture-records.json) record the observed viewport, DPR, scroll position, and revision tag for each capture. Baseline files were served from `git show 7e34a70:<page>` copies with a local base URL; final files were served from regenerated output, recorded in [render hashes](render-hashes.json). Font and external-provider rendering can vary between visits.

| Page | Before | After |
| --- | --- | --- |
| Home, desktop | [Before](captures/before-home-desktop.jpg) | [After](captures/after-home-desktop.jpg) |
| Home, mobile | [Before](captures/before-home-mobile.jpg) | [After](captures/after-home-mobile.jpg) |
| Selected Work, desktop | [Before](captures/before-work-desktop.jpg) | [After](captures/after-work-desktop.jpg) |
| Selected Work, mobile | [Before](captures/before-work-mobile.jpg) | [After](captures/after-work-mobile.jpg) |

Additional details: [Meme Arcade desktop](captures/after-memearcade-desktop.jpg), [Meme Arcade mobile](captures/after-memearcade-mobile.jpg), [square video mobile](captures/after-square-video-mobile.jpg), [mobile menu before](captures/before-menu-mobile.jpg), [mobile menu after](captures/after-menu-mobile.jpg).

## Corrections and limits

Verification caught and corrected intrinsic grid-width overflow at 200% text, header measurement feedback, a carousel Pause/focus ordering issue, the universal video aspect ratio, and screenshot viewport/export-size mismatches. Capture exports were identified as JPEG and given matching extensions.

No physical iPhone/Android testing, touch-hardware scrolling, full assistive-technology audit, cross-browser certification, exhaustive external-link availability check, or automated cold-network audit was performed. Third-party players remain subject to their own loading, permissions, and availability. The original content’s EB1A/citizenship wording and differing book-count claims were preserved rather than independently fact-checked or rewritten.

## Follow-up: clipped glow edges

Hassan’s footer screenshot revealed rectangular edges where the off-center decorative gradients were clipped before reaching transparency. The shared depth layer now has an elliptical alpha mask that fades to fully transparent at every boundary. This applies to both pages and preserves scroll movement, controls, and layout. Verified the desktop footer at 1440 × 900 and phone layout at 390 × 844, with no horizontal overflow; generation, seven output regressions, and image verification pass. [Corrected footer](captures/footer-glow-fix-desktop.jpg). The original comparison tags, captures, and render hashes above remain tied to the initial redesign commit; this is a subsequent correction.

## Follow-up: border-free visual direction

At Hassan’s request, authored borders and section rules were removed throughout both current pages. Former outline buttons now use tonal backgrounds, the hero retains translucent depth surfaces, and hard offset/ring shadows around media were softened. Keyboard-only focus outlines remain available. Scroll transitions and masked lighting are preserved. Browser inspection found no visible CSS borders or horizontal overflow across desktop and mobile layouts; generation, seven output regressions, and image verification pass. [Border-free footer](captures/borderless-footer-desktop.jpg).

## Follow-up: individual row transitions

Each row now has a named motion profile rather than the same generic entrance. The 25 profiles combine ten decorative light animations with distinct palettes, durations, heading entrances, and bounded scroll travel. Nested cards inherit their section’s style and alternate direction. Profiles cover every section, the Selected Work index, the nested featured book, and the shared contact area: [observed profile coverage](row-motion-profiles.json).

| Content | Motion treatment |
| --- | --- |
| Hero / Selected Work introduction | Portrait light bloom / spatial prism opening |
| Impact metrics / startup exits | Rising cascade / stacked momentum |
| Resume / research citations | Document settle / layered reference reveal |
| ClineFlow / Meme Arcade | Cyan signal scan / violet prism lift |
| Apple recognition | Soft, neutral spotlight |
| Books / featured book | Page-like light turn / reading-light sweep |
| Interviews / filmography | Screen widening / cinematic curtain |
| Press / biography | Editorial scan / portrait drift |
| Research / quote / contact | Discovery orbit / quiet resolve / invitation spotlight |

Only decorative light uses rotation, sweeps, and opening effects. Media and chapter containers animate opacity without moving their interactive geometry; headings and smaller editorial blocks use restrained directional entrances. Desktop scroll travel stays within 24 px vertically and 8 px horizontally. The transitions play once as content enters, while the individual depth treatments continue responding to scrolling. Breakpoint and pointer-mode changes settle active entrances immediately.

Mobile uses 360 ms light fades and at most 8 px vertical text entrances, with no parallax. System/manual reduced motion disables all row animation. Browser inspection confirmed complete section coverage, paused offscreen decoration, fixed video transforms, the mobile fallback, and zero animated rows or transformed depth layers in reduced mode. Ten controller tests now include distinct profile selection and fixed chapter geometry, alongside the existing seven generated-output checks and image verification. No borders or animation dependencies were added.

## Follow-up: cinematic entrances that play once

Entrances now have explicit pending, running, and complete states, with one iteration per document load. Completed rows release their entrance observers and cannot replay when scrolling back, changing motion preferences, or restoring the page from the browser cache. Leaving the viewport settles an unfinished entrance immediately, preventing partial reveals on return and releasing their animation work. Hidden tabs and the menu still pause active motion. A document-level initialization guard prevents duplicate listeners, observers, timers, and decorative layers if the script executes again.

The cinematic treatment now uses a three-stage portrait approach, smoother heading easing, and longer light fades through intermediate positions. Decorative light delays match their row’s timing. Chapter and media containers stay fully opaque, eliminating compounded parent/child fades around video, PDF, and installer controls. Mobile retains one 360 ms light fade, stationary depth layers, and short text movement. Previously requested carousel autoplay, the press strip, and scroll-responsive depth keep their separate interaction policies; the one-shot rule applies to entrance reveals.

Verified 13 controller regressions plus seven generated-output regressions and image verification. New checks cover duplicate initialization, a completed reveal surviving scroll/toggle/cache return, interrupted page-cache restoration, and an offscreen reveal settling without replay. Browser checks confirmed the hero remains complete with no active light animation after scrolling away and back; mobile showed one animation iteration, 360 ms duration, fully opaque containers, no moving depth layers, and no horizontal overflow.
