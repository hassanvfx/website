# Technical Writing — 2026-09-06

Direction and approval: Hassan. Article authorship: Hassan Uriostegui. Design, implementation, editorial summaries, artwork generation, and documentation: Codex.

## Editorial review

All five linked Medium articles were read in full in the browser. Article titles in the published content take precedence over older URL slugs. The Simple3D article is titled “Modular Applications with SPM, SwiftUI and Combine”; the agent article is titled “Stop Telling AI Agents What to Do.” Canonical article URLs, exact titles, dates, topics, and original summaries are stored in `generator/technical_writing.py`.

- Modular Applications: Simple3D, MVVM, dependency injection, layered SPM dependencies, SwiftUI and Combine.
- AI Agents: shared understanding grounded in real code, explicit success criteria, and durable journals before execution.
- SwiftSPM: a package and locally linked tandem demo app, enabling iteration before publication.
- Newsmusic: transcripts and source metadata become original lyrics, music, visuals, and a reviewed video. The summary avoids promising monetization.
- Lyrics: an inspectable arrangement pipeline with deterministic word-preservation checks, retaining the author’s intent.

## Composition and assets

Technical Writing follows iOS Open Source. Five alternating rows reuse the Swift showcase layout, collapse to one column on phones, and inherit the existing once-only motion controller. Covers, headings, and explicit Read on Medium actions link to their respective articles. HTML retains all important text; decorative cover images have empty alt text inside links labelled by the adjacent article heading.

The shared Explore Sparks renderer now includes Technical Writing as the third More Sparks option, using the official MUI 7.3.4 ArticleOutlined paths and existing icon licensing. The menu is identical on home and Sparks with page-aware anchors. Search metadata includes the topic, five Article nodes, and updated sitemap modification dates; section fragments are not separate sitemap pages.

Five original illustrative covers were generated using OpenAI ImageGen, then converted only through `generator/optimize_images.py` into manifest-backed WebP assets. Covers are illustrative, not screenshots of the tools. Prompts are recorded below. The four supporting bookstore images were resized from 440px to 320px through the same optimizer to retain the existing 360 KB Selected Work image budget; their original provenance was preserved. Their full original files remain in Git history. No image-manifest edits were made by hand.

## Verification

- Generator run; all three published pages match source.
- 16 Python regression tests; 13 existing interaction/controller tests; image verification; git whitespace checks.
- Selected Work unique image sources: 359,440 bytes. Homepage: 1,151,830 bytes. New images are lazy-loaded with reserved dimensions.
- Browser viewport emulation at 320, 390, 768, 1024, 1440, and 1920px: no document or article-row horizontal overflow.
- Visual inspection at 1440×900 and 390×844, default scale; mobile submenu navigation lands below the fixed header; all five covers loaded. Captures in `.cache/technical-writing/desktop.png` and `mobile.png` show the section after its entrance settled, motion enabled, article section in view, external video players elsewhere on the page unplayed. Captures reflect the working tree based on 32047a6c.
- This was browser emulation, not physical-device testing. No new per-frame animation scheduler or external runtime dependency was added.

## Image prompts

### writing-modular-swift

Use case: ads-marketing. Create a sophisticated 16:9 editorial article cover for a technical portfolio, matching a dark near-black cyan and muted purple visual system. Three restrained translucent modular blocks and a tiny wireframe cube, expressing a modular iOS 3D viewer. Minimal spacious composition, flat dark backgrounds, restrained dimensional illustration on the right occupying one third. Main priority: large immaculate readable white sans-serif typography on the left, with the EXACT full article title, broken into well-spaced lines: "Modular Applications with SPM, SwiftUI and Combine". Keep all text in safe margins. No other text, no borders, no logos, no tiny code, no busy textures. Consistent art direction suitable for a collection of article cards.

### writing-agent-alignment

Use case: ads-marketing. Create a sophisticated 16:9 editorial article cover for a technical portfolio, matching a dark near-black cyan and muted purple visual system. Two precise connected maps converging into a single shared blueprint, expressing shared understanding before execution. Minimal spacious composition, flat dark backgrounds, restrained dimensional illustration on the right occupying one third. Main priority: large immaculate readable white sans-serif typography on the left, with the EXACT full article title, broken into well-spaced lines: "Stop Telling AI Agents What to Do". Keep all text in safe margins. No other text, no borders, no logos, no tiny code, no busy textures. Consistent art direction suitable for a collection of article cards.

### writing-swiftspm

Use case: ads-marketing. Create a sophisticated 16:9 editorial article cover for a technical portfolio, matching a dark near-black cyan and muted purple visual system. Two elegantly connected objects, a package cube and an app window, expressing a Swift package developed alongside its demo app. Minimal spacious composition, flat dark backgrounds, restrained dimensional illustration on the right occupying one third. Main priority: large immaculate readable white sans-serif typography on the left, with the EXACT full article title, broken into well-spaced lines: "SwiftSPM: Instant SPM + Tandem App tool". Keep all text in safe margins. No other text, no borders, no logos, no tiny code, no busy textures. Consistent art direction suitable for a collection of article cards.

### writing-newsmusic

Use case: ads-marketing. Create a sophisticated 16:9 editorial article cover for a technical portfolio, matching a dark near-black cyan and muted purple visual system. A restrained transformation of a newspaper panel into a musical waveform and a video frame. No currency symbols or income promises. Minimal spacious composition, flat dark backgrounds, restrained dimensional illustration on the right occupying one third. Main priority: large immaculate readable white sans-serif typography on the left, with the EXACT full article title, broken into well-spaced lines: "Turn trending news into YouTube music videos — and build a faceless channel you can monetize". Keep all text in safe margins. No other text, no borders, no logos, no tiny code, no busy textures. Consistent art direction suitable for a collection of article cards.

### writing-lyrics

Use case: ads-marketing. Create a sophisticated 16:9 editorial article cover for a technical portfolio, matching a dark near-black cyan and muted purple visual system. A lyric sheet becoming a musical arrangement with flowing lines and small musical annotations, original words preserved. Minimal spacious composition, flat dark backgrounds, restrained dimensional illustration on the right occupying one third. Main priority: large immaculate readable white sans-serif typography on the left, with the EXACT full article title, broken into well-spaced lines: "Turn Raw Lyrics Into Performance-Ready Songs". Keep all text in safe margins. No other text, no borders, no logos, no tiny code, no busy textures. Consistent art direction suitable for a collection of article cards.

