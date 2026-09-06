# Chapter navigation

Hassan directed a consistent return path from content chapters to Explore Sparks. Codex designed and implemented the shared generator helper.

The “← More Sparks” link pairs with the existing chapter eyebrow on desktop and moves above it on phones. It uses a quiet borderless surface, cyan hover/focus feedback, and a minimum 44px target. Main content chapters on both home and Sparks share the same pattern; nested project cards, introductory heroes, and the resume-only page do not repeat it.

Both menus expose the stable `#explore-sparks` anchor with `tabindex="-1"`. Native fragment navigation keeps the user on the current page and transfers keyboard focus to the menu. Existing document scroll padding clears the fixed header. No JavaScript or animation logic was added; reduced-motion scrolling and completed entrance states retain their existing behavior.

Verification: generation and image verification passed; 17 Python regression checks passed, including page-local return destinations and source/output parity. In browser viewport emulation, homepage and Sparks return links moved focus to Explore Sparks and landed below the header at 1440px and 390px. Homepage controls stayed in bounds at 320, 768, and 1440px; Sparks controls were also checked at 390px. No physical-device testing was performed.
