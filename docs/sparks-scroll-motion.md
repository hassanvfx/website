# Sparks bridge motion

Direction: Hassan. Design, implementation, and verification: Codex.

The three homepage bridges keep their existing destinations and use one native
link per banner. Its CSS hit area covers the whole colored band, including the
artwork. Keyboard focus outlines the band and settles its animated contents.
The heading, description, URL, and link remain available without JavaScript.

Motion's `scroll()` drives reversible entrance/exit fades and translations with
a broad fully readable middle range. The AI layers orbit in opposite directions;
iOS layers spread in depth; writing sheets fan and tilt. The CTA and banner hit
area stay fixed. Mobile uses shorter copy travel and smaller icon compositions.
These three banners are excluded from the older one-time chapter entrance.

The controller shares the site's motion policy. It cancels subscriptions and
clears animated styles offscreen, on keyboard focus, in hidden tabs, while the
menu is open, and for system/manual/performance reduced motion. Re-entering
subscribes at the current scroll position. No wheel/touch handlers or scroll
hijacking are introduced. No library request occurs on pages without bridges,
or while reduced motion is enabled. A failed load leaves static native links.

## Dependency

- Motion 12.23.24, MIT; license in `assets/vendor/MOTION-LICENSE.txt`.
- Unmodified distribution: https://cdn.jsdelivr.net/npm/motion@12.23.24/dist/motion.js
- Local file: `assets/vendor/motion-12.23.24.js` (81,378 bytes).
- Loaded once on demand near the first bridge, from this site's own origin.
- API reference: https://motion.dev/docs/scroll
- This uses the scroll callback API and transform/opacity updates. It does not
  claim compositor-only execution or a measured device frame-rate guarantee.

## Verification

Generator/output equality, local anchors, image references, and existing site
tests pass. Controller regressions cover forward/backward reveal, readable middle
states, distinct layer transforms, duplicate initialization, visibility/focus/
reduced-motion cleanup, one-time lazy loading, and failed-library fallback.

Browser checks confirmed changing layer transforms during native scrolling and
navigation to `selected-work.html#work` by clicking the AI artwork. Desktop and
390px mobile composition were visually reviewed; mobile layers remain separate
from the title and body. Viewport emulation is not physical-device testing.
