"""Canonical content registry and page compositions for the portfolio.

The original data modules retain the long-form facts and media metadata.  This
module is the one place that decides which entity appears on which public page
and under which editorial angle.
"""

from portfolio_data import (
    BOOKS, CLINEFLOW, CURRENT_PROJECTS, FEATURED_BOOKS, HISTORIC_COMPANIES,
    MEME_ARCADE, PRESS, PROFESSIONAL_PROFILE, SWIFT_FOUNDATIONS, TWINCHAT_PAPER, WAKEN_AI,
    WWDC14_FEATURE,
)
from technical_writing import TECHNICAL_WRITING


SITE_PAGES = {
    "home": {"path": "", "title": "Hassan Uriostegui | Agentic AI, Mobile Products & ClineFlow", "description": "Hassan Uriostegui is an AI-native principal engineer and founder building agentic AI, durable context systems, mobile products, and ClineFlow.", "schema_type": "ProfilePage", "image": "portrait", "image_alt": "Portrait of Hassan Uriostegui", "priority": "1.0", "changefreq": "weekly", "indexable": True},
    "agentic-ai": {"path": "agentic-ai.html", "title": "Agentic AI, Context & Prompt Engineering | Hassan Uriostegui", "description": "Agentic AI projects, durable context systems, prompt engineering, research, and open-source work by Hassan Uriostegui.", "schema_type": "CollectionPage", "image": "infinite-ai-context-cover", "image_alt": "Infinite AI Context: ClineFlow and Google's Open Knowledge Format book cover", "priority": "0.9", "changefreq": "monthly", "indexable": True},
    "mobile-apps": {"path": "mobile-apps.html", "title": "Mobile Apps & iOS Open Source | Hassan Uriostegui", "description": "Mobile products, WWDC work, iOS engineering, and Swift open-source tools by Hassan Uriostegui.", "schema_type": "CollectionPage", "image": "meme-arcade-product-panels", "image_alt": "Meme Arcade iPhone game platform product panels", "priority": "0.9", "changefreq": "monthly", "indexable": True},
    "github": {"path": "github.html", "title": "GitHub Repositories | Hassan Uriostegui", "description": "Owned public repositories, developer tools, and open-source projects by Hassan Uriostegui.", "schema_type": "CollectionPage", "image": "github-terminal-hero", "image_alt": "Developer terminal showing Hassanvfx repositories", "priority": "0.8", "changefreq": "monthly", "indexable": True},
    "startups": {"path": "startups.html", "title": "Startups, Product Impact & Exits | Hassan Uriostegui", "description": "Startup work, product impact, exits, and Waken AI by Hassan Uriostegui.", "schema_type": "CollectionPage", "image": "portrait", "image_alt": "Portrait of Hassan Uriostegui", "priority": "0.8", "changefreq": "monthly", "indexable": True},
    "books": {"path": "books.html", "title": "Books & Technical Writing | Hassan Uriostegui", "description": "Technical books, articles, fiction, and journaling by Hassan Uriostegui.", "schema_type": "CollectionPage", "image": "infinite-ai-context-cover", "image_alt": "Infinite AI Context: ClineFlow and Google's Open Knowledge Format book cover", "priority": "0.8", "changefreq": "monthly", "indexable": True},
    "profile": {"path": "profile.html", "title": "Resume, Evidence, Press & Interviews | Hassan Uriostegui", "description": "Resume, citation evidence, press coverage, and interviews for Hassan Uriostegui.", "schema_type": "ProfilePage", "image": "portrait", "image_alt": "Portrait of Hassan Uriostegui", "priority": "0.8", "changefreq": "monthly", "indexable": True, "og_type": "profile"},
}

NAVIGATION = (
    ("Agentic AI", "agentic-ai"), ("Mobile Apps", "mobile-apps"),
    ("Startups", "startups"), ("Publications", "books"), ("GitHub", "github"),
    ("Resume", "profile"),
)

PROJECTS = {
    "clineflow": CLINEFLOW,
    "meme-arcade": MEME_ARCADE,
    "wwdc14": WWDC14_FEATURE,
    "twinchat-paper": TWINCHAT_PAPER,
    **{item["id"]: item for item in CURRENT_PROJECTS},
    **{item["id"]: item for item in HISTORIC_COMPANIES},
}

# The Mobile Apps introduction is a compact visual index of the mobile
# products represented in the career catalog. Each treatment is tracked in the
# image manifest, preserving a coherent full-bleed visual system across the wall.
MOBILE_APP_ICON_WALL = (
    {"project_id": "meme-arcade", "label": "Meme Arcade", "image": "meme-arcade-wall-icon", "asset_type": "app-icon"},
    {"project_id": "spreeai", "image": "spreeai-wall-icon", "asset_type": "app-icon"},
    {"project_id": "btwinfriends", "image": "btwin-wall-icon", "asset_type": "app-icon"},
    {"project_id": "twinchat", "image": "twinchat-wall-icon", "asset_type": "app-icon"},
    {"project_id": "community", "image": "community-wall-icon", "asset_type": "app-icon"},
    {"project_id": "ultrakam", "image": "ultrakam-wall-icon", "asset_type": "app-icon"},
    {"project_id": "flyr", "image": "flyrtv-wall-icon", "asset_type": "app-icon"},
    {"project_id": "viddy", "image": "viddy-wall-icon", "asset_type": "app-icon"},
)

BOOK_CATALOG = {
    "clineflow-book": FEATURED_BOOKS[0],
    "mac-silicon-book": FEATURED_BOOKS[1],
    "meme-arcade-book": FEATURED_BOOKS[2],
    "mst-book": BOOKS[2],
    "nemos-mirror": BOOKS[3],
    "cyberpunks": BOOKS[4],
    "humanized-robot": BOOKS[5],
}

# Keep the named project groups as IDs.  Renderers resolve these objects from
# PROJECTS, rather than maintaining separate copies of their descriptions.
PAGE_COMPOSITIONS = {
    "home": {
        "agentic": ("clineflow", "ai-copyright-weights"),
        "mobile": ("meme-arcade", "wwdc14"),
        "books": ("clineflow-book", "mac-silicon-book", "meme-arcade-book"),
    },
    "agentic-ai": {
        "projects": ("clineflow", "btwinfriends", "twinchat", "newsmusic", "lyrics-refiner"),
        "open_source": ("clineflow", "kie-api-python", "newsmusic", "lyrics-refiner"),
        "articles": ("ai-copyright-weights", "writing-agent-alignment"),
        "books": ("clineflow-book", "mac-silicon-book"),
    },
    "mobile-apps": {
        "projects": ("meme-arcade", "spreeai", "btwinfriends", "twinchat", "community", "ultrakam", "flyr"),
        "open_source": ("swift-spm", "datastore", "webview-swiftui"),
        "articles": ("writing-wwdc14", "writing-demystify-swiftui", "writing-modular-swift", "writing-swiftspm", "writing-datastore", "writing-securevault", "writing-swiftwallet"),
        "books": ("meme-arcade-book",),
    },
    "startups": {"exits": ("ultrakam", "flyr", "viddy"), "companies": ("spreeai", "community"), "lab": "waken"},
    "books": {"technical": ("clineflow-book", "mac-silicon-book", "meme-arcade-book"), "earlier": ("mst-book", "nemos-mirror", "cyberpunks", "humanized-robot")},
}

# Article metadata includes a precise topic tag, allowing one source to render
# in a page-specific card without duplicated title or URL text.
ARTICLE_CATALOG = {item["id"]: {**item, "tags": ("writing",)} for item in TECHNICAL_WRITING}
ARTICLE_CATALOG.update({
    "ai-copyright-weights": {
        "id": "ai-copyright-weights", "title": "AI-Copyright Weights: A New Frontier in Intellectual Property Law", "topic": "AI research", "date": "2026-06-20", "url": "https://medium.com/twinchat/ai-copyright-weights-a-new-frontier-in-intellectual-property-law-d8ee1b6c55ee", "description": "A research essay on authorship, provenance, and creative contribution in AI-assisted work.", "tags": ("agentic", "research"),
    },
    "writing-demystify-swiftui": {
        "id": "writing-demystify-swiftui", "title": "Demystify SwiftUI", "topic": "iOS architecture", "date": "2021-06-30", "url": "https://uriostegui.medium.com/demystify-swiftui-cfa69732ad00", "description": "Notes on SwiftUI identity, state, view composition, and the framework's update model.", "tags": ("mobile", "writing"),
    },
    "writing-datastore": {
        "id": "writing-datastore", "title": "DataStorage: Encrypted Data Persistence for SwiftUI", "topic": "iOS persistence", "date": "2024-01-07", "url": "https://uriostegui.medium.com/datastorage-encrypted-data-persistence-for-swiftui-f0187f9f2e40", "description": "A practical introduction to encrypted persistence and background saving for SwiftUI models.", "tags": ("mobile", "writing"),
    },
    "writing-securevault": {
        "id": "writing-securevault", "title": "SecureVault: A Swift Library for Robust Data Encryption", "topic": "iOS security", "date": "2024-01-07", "url": "https://uriostegui.medium.com/introducing-securevault-a-swift-library-for-robust-data-encryption-9e7aff1758cf", "description": "An overview of per-installation encrypted storage backed by the iOS Keychain.", "tags": ("mobile", "writing"),
    },
    "writing-swiftwallet": {
        "id": "writing-swiftwallet", "title": "SwiftWallet: Encrypted Credits Manager for SwiftUI", "topic": "iOS developer tools", "date": "2024-01-07", "url": "https://uriostegui.medium.com/swiftwallet-a-deep-dive-into-practical-use-for-ios-apps-%EF%B8%8F-4aa4e927c63d", "description": "A SwiftUI wallet utility using token bundles and encrypted local storage.", "tags": ("mobile", "writing"),
    },
    "writing-wwdc14": {
        "id": "writing-wwdc14", "title": "The Time Apple Featured My App at WWDC14", "topic": "Mobile products", "date": "2024-01-01", "url": WWDC14_FEATURE["medium_url"], "description": "The story behind Ultrakam Remote Control's appearance in Apple's WWDC14 session 709.", "tags": ("mobile", "writing"),
    },
})

for item in ARTICLE_CATALOG.values():
    if item["id"] in {"writing-modular-swift", "writing-swiftspm"}:
        item["tags"] = ("mobile", "writing")
    elif item["id"] == "writing-agent-alignment":
        item["tags"] = ("agentic", "writing")

# Curated portfolio repository snapshot, refreshed from the public GitHub API
# on 2026-09-07. These are only the repositories already linked by the
# previously published site; this is deliberately not an account-wide mirror.
# SUIPlayer remains a Mobile Apps tool but is not added here until it is
# intentionally introduced to the portfolio catalog.
GITHUB_REPOSITORY_SNAPSHOT = (
    {"name": "clineflow", "description": "Durable AI memory, portable across chats, agents, and teams; knowledge-base versioning powered by Google’s OKF and Git.", "language": "Shell", "archived": False, "license": "MIT"},
    {"name": "ios-framework", "description": "Swift Package Manager configuration tool.", "language": "Swift", "archived": False, "license": None},
    {"name": "ios-storage", "description": "Encrypted data persistence for SwiftUI.", "language": "Swift", "archived": False, "license": None},
    {"name": "ios-webViewSwiftUI", "description": "SwiftUI WebView model, view, and helpers.", "language": "Swift", "archived": False, "license": None},
    {"name": "kie-api-python", "description": "Unofficial KIE.AI CLI and MCP server.", "language": "Python", "archived": False, "license": "MIT"},
    {"name": "lyrics-refiner", "description": "Performance-ready lyric refinement tooling.", "language": "TypeScript", "archived": False, "license": "MIT"},
    {"name": "newsmusic", "description": "Automation for turning trending news into songs, visuals, and YouTube videos.", "language": "Python", "archived": False, "license": "MIT"},
)

GITHUB_REPOSITORIES = tuple(item["name"] for item in GITHUB_REPOSITORY_SNAPSHOT)
GITHUB_FEATURED = ("clineflow", "kie-api-python", "ios-framework", "ios-storage")

# Research checked 2026-09-07. Highlights distinguish personal contributions
# from company-scale outcomes. A source link must support its whole highlight.
STARTUP_SOURCES = {
    "resume": {"label": "Résumé", "kind": "Career record", "url": PROFESSIONAL_PROFILE["pdf"]},
    "spree-valuation": {"label": "SpreeAI · May 2025", "kind": "Company release", "url": "https://www.prnewswire.com/news-releases/spreeai-is-redefining-retail-with-virtual-ai-powered-try-ons-curated-by-the-top-in-tech-and-fashion-302447115.html"},
    "community-scale": {"label": "Fast Company · Sep 2020", "kind": "Independent reporting", "url": "https://www.fastcompany.com/90554036/why-president-barack-obama-is-giving-out-his-phone-number-today"},
    "community-talent": {"label": "Fast Company · Jan 2020", "kind": "Independent reporting", "url": "https://www.fastcompany.com/90439032/why-your-favorite-celebs-are-ditching-twitter-for-an-app-youve-never-heard-of"},
    "flyr-traction": {"label": "The Drum · Apr 2018", "kind": "Independent reporting", "url": "https://www.thedrum.com/news/mexican-startup-flyr-raises-6m-bring-tv-quality-ads-apple-devices"},
    "flyr-launch": {"label": "Flyr · Mar 2017", "kind": "Company release", "url": "https://www.prnewswire.com/news-releases/flyr-introduces-the-first-ai-powered-video-platform-for-faster-better-stories-300422470.html"},
    "founder-interview": {"label": "Authority Magazine · Aug 2024", "kind": "Founder interview", "url": "https://medium.com/authority-magazine/hassan-uriostegui-of-wakenai-on-the-future-of-artificial-intelligence-57d39bf22ced"},
    "viddy-exit": {"label": "NEA portfolio", "kind": "Investor record", "url": "https://www.nea.com/portfolio/viddy"},
    "ultrakam-launch": {"label": "The Next Web · Mar 2014", "kind": "Independent reporting", "url": "https://thenextweb.com/news/ultrakam-paves-way-2k-video-ios"},
    "wwdc14": {"label": "Apple WWDC14 · slide 6", "kind": "Apple presentation", "url": WWDC14_FEATURE["pdf_url"] + "#page=6"},
    "clineflow-launch": {"label": "Waken AI · Sep 2026", "kind": "Company release", "url": "https://www.newswire.com/news/waken-ai-clineflow-makes-ai-context-portable-across-chats-agents-and-teams"},
    "clineflow-repo": {"label": "ClineFlow repository", "kind": "Open source", "url": "https://github.com/hassanvfx/clineflow"},
    "clineflow-ebook": {"label": "Free ClineFlow ebook", "kind": "Free ebook", "url": BOOK_CATALOG["clineflow-book"]["ebook_url"]},
    "clineflow-print": {"label": "ClineFlow printed edition", "kind": "Lulu book", "url": BOOK_CATALOG["clineflow-book"]["url"]},
    "btwin-release": {"label": "BTwin AI Friends", "kind": "Company release", "url": "https://www.prnewswire.com/news-releases/wakenai-launches-btwin-ai-friends-the-first-emotional-support-network-inspired-by-clones-of-your-loved-and-not-so-loved-ones-302193521.html"},
    "twinchat-demo": {"label": "TwinChat product demo", "kind": "Product video", "url": "https://vimeo.com/twinchat"},
    "newsmusic-repo": {"label": "Newsmusic repository", "kind": "Open source", "url": "https://github.com/hassanvfx/newsmusic"},
    "lyrics-refiner-repo": {"label": "Lyrics Refiner repository", "kind": "Open source", "url": "https://github.com/hassanvfx/lyrics-refiner"},
    "meme-arcade-book": {"label": "Meme Arcade engineering guide", "kind": "Technical book", "url": "https://hassanvfx.github.io/meme-arcade-book/"},
}

STARTUP_CASES = {
    "ultrakam": {
        "category": "Independent product", "icon": "filmography", "accent": "cyan",
        "thesis": "Professional filmmaking, built for the phone.",
        "contribution": "Created a filmmaking suite that pushed iPhone capture beyond Full HD, with manual controls, high-quality codecs, and a companion Bluetooth remote. Built around the workflows of independent filmmakers.",
        "contribution_source": "ultrakam-launch",
        "highlights": (
            {"value": "2K", "label": "Mobile capture", "detail": "Delivered up to 2240 × 1672 capture on iPhone 5s with H.264.", "scope": "Product capability", "source": "ultrakam-launch"},
            {"value": "+70%", "label": "Pixels beyond Full HD", "detail": "Higher-resolution recording on the iPhone 5s, documented at launch.", "scope": "Product capability", "source": "ultrakam-launch"},
            {"value": "WWDC14", "label": "Featured by Apple", "detail": "Ultrakam Remote Control appeared in Session 709 on nearby networking.", "scope": "Product recognition", "source": "wwdc14"},
            {"value": "2 apps", "label": "One capture workflow", "detail": "Camera and Bluetooth remote: focus, exposure, white balance, and recording.", "scope": "Product system", "source": "ultrakam-launch"},
        ),
    },
    "flyr": {
        "category": "Founder → acquisition", "icon": "impact", "accent": "pink",
        "thesis": "A video engine became a venture-backed product.",
        "contribution": "Co-founded FlyrTV and led product and engineering from the core rendering engine to a reusable template platform. Co-raised funding and led the technical organization through the acquisition by Pond5.",
        "contribution_source": "resume",
        "highlights": (
            {"value": "$6M", "label": "Capital raised", "detail": "Funding reported in April 2018 to bring professional video creation to mobile.", "scope": "Company funding", "source": "flyr-traction"},
            {"value": "13K", "label": "Paying subscribers", "detail": "Alongside one million user-created projects, reported in April 2018.", "scope": "Company traction", "source": "flyr-traction"},
            {"value": "10K+", "label": "Reusable templates", "detail": "Built the rendering and template architecture for rapid, multi-format video publishing.", "scope": "My contribution", "source": "resume"},
            {"value": "Pond5", "label": "Acquisition", "detail": "Founder account of the product’s exit, also documented in the résumé.", "scope": "Company outcome", "source": "founder-interview"},
        ),
    },
    "viddy": {
        "category": "Mobile video → acquisition", "icon": "filmography", "accent": "violet",
        "thesis": "Video creation at social-platform scale.",
        "contribution": "Architected the mobile VFX and rendering engine across iOS and Android. Built performance-critical editing and compositing systems that made sophisticated video creation possible on early smartphone hardware.",
        "contribution_source": "resume",
        "highlights": (
            {"value": "40M+", "label": "Platform users", "detail": "User reach described in the founder’s career interview and résumé.", "scope": "Company scale", "source": "founder-interview"},
            {"value": "iOS + Android", "label": "Cross-platform VFX", "detail": "Architected rendering and visual effects for both mobile platforms.", "scope": "My contribution", "source": "resume"},
            {"value": "Core engine", "label": "Creation infrastructure", "detail": "Owned performance-critical editing, compositing, and rendering systems.", "scope": "My contribution", "source": "resume"},
            {"value": "Fullscreen", "label": "Acquisition", "detail": "Acquired-company status confirmed by Viddy investor NEA.", "scope": "Company outcome", "source": "viddy-exit"},
        ),
    },
    "spreeai": {
        "category": "AI commerce", "icon": "ios-open-source", "accent": "violet",
        "thesis": "The native foundation for immersive commerce.",
        "contribution": "Led iOS architecture for an AI/3D shopping and avatar platform. Connected modular SwiftUI product domains, AR capture, cloud assets, and automated delivery into a maintainable mobile foundation.",
        "contribution_source": "resume",
        "highlights": (
            {"value": "$1.5B", "label": "Reported valuation", "detail": "Announced in May 2025, after my Dec 2020–Apr 2023 role.", "scope": "Later company milestone", "source": "spree-valuation"},
            {"value": "Modular", "label": "SwiftUI architecture", "detail": "Separated product domains to support feature delivery and immersive 3D experiences.", "scope": "My contribution", "source": "resume"},
            {"value": "AR + 3D", "label": "Native commerce workflows", "detail": "Integrated ARKit, LiDAR, capture, and visualization with cloud-hosted assets.", "scope": "My contribution", "source": "resume"},
            {"value": "CI/CD", "label": "From assets to releases", "detail": "Integrated AWS media workflows and automated releases with GitHub Actions and Fastlane.", "scope": "My contribution", "source": "resume"},
        ),
    },
    "community": {
        "category": "Consumer messaging", "icon": "work", "accent": "cyan",
        "thesis": "A native app behind direct audience relationships.",
        "contribution": "Contributed to iOS architecture during Community’s early growth. Helped move key surfaces from React Native to native iOS and introduced SwiftUI, Combine, and MVVM for a more maintainable product.",
        "contribution_source": "resume",
        "highlights": (
            {"value": "10M+", "label": "Platform users", "detail": "Career-record scale; Fast Company reported nearly 20M members by September 2020.", "scope": "Company scale", "source": "community-scale"},
            {"value": "Global talent", "label": "Direct fan connections", "detail": "Adopted by Jennifer Lopez, Paul McCartney, Kerry Washington, and the Jonas Brothers.", "scope": "Company adoption", "source": "community-talent"},
            {"value": "Native iOS", "label": "Platform migration", "detail": "Helped migrate key React Native surfaces for performance and deeper Apple integration.", "scope": "My contribution", "source": "resume"},
            {"value": "Reactive", "label": "Modern feature architecture", "detail": "Introduced SwiftUI, Combine, and MVVM patterns to improve maintainability.", "scope": "My contribution", "source": "resume"},
        ),
    },
    "waken": {
        "category": "Bootstrapped AI lab", "icon": "work", "accent": "pink",
        "thesis": "From conversational AI to durable agent memory.",
        "contribution": "Founded and built BTwin’s full stack: multi-model orchestration, persistent personas, native SwiftUI, subscriptions, and analytics. The lab’s later work includes ClineFlow, bringing portable project knowledge to agentic workflows.",
        "contribution_source": "resume", "additional_source": "clineflow-launch",
        "highlights": (
            {"value": "3 models", "label": "One adaptive harness", "detail": "Integrated OpenAI, Gemini, and Claude with persistent behavioral and relationship context.", "scope": "My contribution", "source": "resume"},
            {"value": "~10%", "label": "Paid conversion", "detail": "BTwin focused acquisition tests, on a $9.99 weekly plan; résumé-reported results.", "scope": "Product experiment", "source": "resume"},
            {"value": "20K", "label": "Conversations analyzed", "detail": "AI character research across 200K generated messages, documented in the résumé.", "scope": "Research validation", "source": "resume"},
            {"value": "Open memory", "label": "ClineFlow · 2026", "detail": "Created a portable, Git-versioned knowledge layer for agents and collaborators.", "scope": "Later lab release", "source": "clineflow-launch"},
        ),
    },
}

# Hero figures resolve the same evidence records as the detailed cases.
STARTUP_HERO_HIGHLIGHTS = (("spreeai", 0), ("community", 0), ("flyr", 0), ("viddy", 0))

# Project-page cases reuse the evidence format from Startups while keeping the
# lens on systems and technical choices. Existing startup cases stay canonical
# for shared companies rather than repeating their facts in another page model.
PROJECT_CASES = {
    "clineflow": {
        "category": "Agentic infrastructure", "icon": "clineflow", "accent": "cyan", "role": "Creator",
        "thesis": "Durable project knowledge that travels with the work.",
        "contribution": "Built a filesystem-native context layer for agents: structured knowledge lives alongside the repository, can be reviewed in version control, and remains portable across chats, tools, and collaborators.",
        "contribution_source": "clineflow-launch",
        "highlights": (
            {"value": "OKF", "label": "Open knowledge format", "detail": "Uses open project files instead of a vendor-locked memory store.", "scope": "Architecture", "source": "clineflow-ebook"},
            {"value": "Git", "label": "Versioned context", "detail": "Preserves decisions and project knowledge in a workflow developers already inspect.", "scope": "Workflow", "source": "clineflow-repo"},
            {"value": "CLI + MCP", "label": "Agent integration", "detail": "Designed to connect durable context to development workflows and compatible agents.", "scope": "Interface", "source": "clineflow-repo"},
            {"value": "Portable", "label": "Across collaborators", "detail": "Context can move with the project rather than being trapped in a chat history.", "scope": "Outcome", "source": "clineflow-print"},
        ),
    },
    "btwinfriends": {
        "category": "Conversational AI", "icon": "work", "accent": "pink",
        "thesis": "A context-aware harness for long-running AI relationships.",
        "contribution": "Built the product foundation for adaptive companion conversations: model orchestration, persistent behavioral context, a native client, subscriptions, and product analytics designed to learn from repeated use.",
        "contribution_source": "btwin-release",
        "related_publication": {"catalog_id": "mst-book", "label": "Read Mind Simulation Technology"},
        "highlights": (
            {"value": "3 models", "label": "Adaptive harness", "detail": "A single experience can coordinate multiple model providers with persistent context.", "scope": "AI systems", "source": "resume"},
            {"value": "20K", "label": "Conversations analyzed", "detail": "Conversation research informed the product’s profile and behavior design.", "scope": "Research", "source": "resume"},
            {"value": "200K", "label": "Messages generated", "detail": "A working corpus used to study long-running conversational patterns.", "scope": "Research", "source": "resume"},
            {"value": "SwiftUI", "label": "Native product surface", "detail": "The client pairs native interaction design with subscriptions and analytics.", "scope": "Product", "source": "resume"},
        ),
    },
    "twinchat": {
        "category": "Conversational product", "icon": "work", "accent": "violet",
        "thesis": "Profiles, context, and conversation designed as one system.",
        "contribution": "Developed a profile-guided conversational product that makes persona information, long-form interaction, and discovery work together as product primitives instead of isolated chat prompts.",
        "contribution_source": "twinchat-demo",
        "related_publication": {"catalog_id": "twinchat-paper", "label": "Read the TwinChat paper"},
        "highlights": (
            {"value": "10K+", "label": "AI personalities", "detail": "A catalog built around distinct public-figure conversational simulations.", "scope": "Product model", "source": "twinchat-demo"},
            {"value": "Profiles", "label": "Structured identity", "detail": "Conversation behavior is grounded in organized persona information.", "scope": "Context design", "source": "twinchat-demo"},
            {"value": "Long-form", "label": "Conversation state", "detail": "The interaction model supports more than a one-off assistant exchange.", "scope": "Interaction", "source": "twinchat-demo"},
            {"value": "Native", "label": "Mobile delivery", "detail": "A product layer shaped around focused, repeatable conversational use.", "scope": "Platform", "source": "twinchat-demo"},
        ),
    },
    "newsmusic": {
        "category": "Creative automation", "icon": "twinchat-paper", "accent": "cyan",
        "thesis": "From a reporting signal to a publishable music video.",
        "contribution": "Built an automated creative pipeline that transforms current reporting into an English-language story, original lyrics, music, visual sequences, and a YouTube-ready video—with explicit stages that stay inspectable.",
        "contribution_source": "newsmusic-repo",
        "highlights": (
            {"value": "News", "label": "Source intake", "detail": "Starts with current reporting as an editorial signal.", "scope": "Pipeline", "source": "newsmusic-repo"},
            {"value": "Lyrics", "label": "Narrative translation", "detail": "Turns the source into an original English-language story and song structure.", "scope": "Generation", "source": "newsmusic-repo"},
            {"value": "Visuals", "label": "Media assembly", "detail": "Coordinates audio and visual output into a coherent video sequence.", "scope": "Production", "source": "newsmusic-repo"},
            {"value": "YouTube", "label": "Publish-ready output", "detail": "Produces a finished artifact for review and publishing workflows.", "scope": "Delivery", "source": "newsmusic-repo"},
        ),
    },
    "lyrics-refiner": {
        "category": "Creative tooling", "icon": "technical-writing", "accent": "pink",
        "thesis": "A local studio for turning raw lyrics into an arrangement.",
        "contribution": "Built a focused local tool for shaping Spanish-language lyrics into performance-ready arrangements, combining structure analysis, genre direction, phonetic notes, and staged production guidance.",
        "contribution_source": "lyrics-refiner-repo",
        "highlights": (
            {"value": "Local", "label": "Creator-controlled workflow", "detail": "Keeps the drafting and refinement process close to the writer’s own working environment.", "scope": "Workflow", "source": "lyrics-refiner-repo"},
            {"value": "Spanish", "label": "Language-aware craft", "detail": "The tool is designed around Spanish-language lyrical structure and sound.", "scope": "Language", "source": "lyrics-refiner-repo"},
            {"value": "Genre", "label": "Arrangement direction", "detail": "Connects lyric intent with genre analysis and production choices.", "scope": "Analysis", "source": "lyrics-refiner-repo"},
            {"value": "Stages", "label": "Performance preparation", "detail": "Moves from rough words toward a sequence ready for production and performance.", "scope": "Output", "source": "lyrics-refiner-repo"},
        ),
    },
    "meme-arcade": {
        "name": "Meme Arcade", "category": "iPhone game platform", "icon": "ios-open-source", "accent": "violet",
        "thesis": "A native discovery layer for instant, web-powered games.",
        "contribution": "Designed a hybrid iPhone arcade that combines a SwiftUI discovery experience, instant web gameplay, community-made games, and reusable package boundaries into one coherent product surface.",
        "contribution_source": "meme-arcade-book",
        "highlights": (
            {"value": "SwiftUI", "label": "Native discovery", "detail": "A fast, platform-native layer for browsing and returning to games.", "scope": "Interface", "source": "meme-arcade-book"},
            {"value": "WKWebView", "label": "Instant gameplay", "detail": "Brings a web game runtime into an iPhone-first product experience.", "scope": "Runtime", "source": "meme-arcade-book"},
            {"value": "SPM", "label": "Modular foundation", "detail": "Reusable package boundaries keep the product system maintainable as it grows.", "scope": "Architecture", "source": "meme-arcade-book"},
            {"value": "Async", "label": "Responsive flow", "detail": "Modern concurrency supports loading, discovery, and gameplay transitions.", "scope": "Platform", "source": "meme-arcade-book"},
        ),
    },
}
PROJECT_CASES.update({project_id: STARTUP_CASES[project_id] for project_id in ("spreeai", "community", "ultrakam", "flyr")})

# A product can serve different readers without blurring its technical story.
# These page-specific case records keep the shared product identity and cited
# sources while presenting the relevant engineering angle on each topic page.
PROJECT_CASES_BY_PAGE = {
    "agentic-ai": {
        "btwinfriends": {
            "category": "Agentic companion system", "icon": "work", "accent": "pink",
            "thesis": "Persistent identity and orchestration for long-running AI relationships.",
            "contribution": "Designed the agentic foundation for adaptive companion conversations: multi-model orchestration, persistent behavioral context, and profile-guided behavior that can evolve across repeated exchanges.",
            "contribution_source": "btwin-release",
            "related_publication": {"catalog_id": "mst-book", "label": "Read Mind Simulation Technology"},
            "highlights": (
                {"value": "3 models", "label": "Model orchestration", "detail": "Coordinates multiple model providers behind one adaptive conversational system.", "scope": "Agent runtime", "source": "resume"},
                {"value": "20K", "label": "Conversation corpus", "detail": "Conversation research informed the relationship and behavior model.", "scope": "Evaluation", "source": "resume"},
                {"value": "200K", "label": "Generated messages", "detail": "A working corpus used to study long-running interaction patterns.", "scope": "Research", "source": "resume"},
                {"value": "Profiles", "label": "Behavioral context", "detail": "Structured relationship and persona information guides each agent response.", "scope": "Context", "source": "resume"},
            ),
        },
        "twinchat": {
            "category": "Persona architecture", "icon": "work", "accent": "violet",
            "thesis": "Structured identity and context for multi-turn character agents.",
            "contribution": "Developed a persona-guided conversation system that treats profile knowledge, agent behavior, and long-form exchanges as a single context-engineering problem.",
            "contribution_source": "twinchat-demo",
            "related_publication": {"catalog_id": "twinchat-paper", "label": "Read the TwinChat paper"},
            "highlights": (
                {"value": "10K+", "label": "Persona catalog", "detail": "A large library of public-figure conversational simulations.", "scope": "Agent model", "source": "twinchat-demo"},
                {"value": "Profiles", "label": "Identity schema", "detail": "Organized persona information grounds agent behavior beyond a one-off prompt.", "scope": "Context", "source": "twinchat-demo"},
                {"value": "Long-form", "label": "Conversation continuity", "detail": "Interaction design supports an ongoing relationship rather than an isolated response.", "scope": "Memory", "source": "twinchat-demo"},
                {"value": "Paper", "label": "System framing", "detail": "The published work connects representation, interaction, and clear boundaries.", "scope": "Research", "source": "twinchat-demo"},
            ),
        },
    },
    "mobile-apps": {
        "btwinfriends": {
            "category": "Native companion app", "icon": "ios-open-source", "accent": "pink",
            "thesis": "A dependable native surface for returning to companion conversations.",
            "contribution": "Built the mobile product layer around adaptive companion conversations: a native client, subscriptions, and product analytics that make repeat interaction feel intentional and measurable.",
            "contribution_source": "btwin-release",
            "highlights": (
                {"value": "Native", "label": "Companion client", "detail": "A focused mobile surface for returning to an ongoing conversational relationship.", "scope": "iOS product", "source": "resume"},
                {"value": "Subscriptions", "label": "Product access", "detail": "The client includes paid-access infrastructure for a continuing product experience.", "scope": "Commerce", "source": "resume"},
                {"value": "Analytics", "label": "Repeat-use signals", "detail": "Product instrumentation supports learning from recurring engagement.", "scope": "Measurement", "source": "resume"},
                {"value": "3 models", "label": "Responsive AI layer", "detail": "The native experience can coordinate multiple model providers behind the interface.", "scope": "Integration", "source": "resume"},
            ),
        },
        "twinchat": {
            "category": "Native conversation app", "icon": "ios-open-source", "accent": "violet",
            "thesis": "A mobile interface for discovering, entering, and returning to AI character conversations.",
            "contribution": "Developed an app-first conversation product where character discovery, profile browsing, and long-form chat work together as clear mobile product surfaces.",
            "contribution_source": "twinchat-demo",
            "highlights": (
                {"value": "10K+", "label": "Character catalog", "detail": "A large selection of AI personalities to browse and revisit from the app.", "scope": "Discovery", "source": "twinchat-demo"},
                {"value": "Profiles", "label": "Character browsing", "detail": "Profile information gives people a clear way to choose and understand each conversation.", "scope": "Interface", "source": "twinchat-demo"},
                {"value": "Long-form", "label": "Conversation surface", "detail": "A focused chat experience designed for more than a one-message interaction.", "scope": "Interaction", "source": "twinchat-demo"},
                {"value": "Native", "label": "App delivery", "detail": "The product is shaped as a dedicated mobile experience for repeat use.", "scope": "Platform", "source": "twinchat-demo"},
            ),
        },
    },
}

# Research overrides preserve product identity and page-specific technical focus.
from project_research import RESEARCH_CASES, RESEARCH_SOURCES, STARTUP_RESEARCH_CASES

STARTUP_SOURCES.update(RESEARCH_SOURCES)
for project_id, researched_case in STARTUP_RESEARCH_CASES.items():
    STARTUP_CASES[project_id] = {**STARTUP_CASES[project_id], **researched_case}
for page_id, researched_cases in RESEARCH_CASES.items():
    for project_id, researched_case in researched_cases.items():
        base = PROJECT_CASES_BY_PAGE[page_id].get(project_id, PROJECT_CASES[project_id])
        PROJECT_CASES_BY_PAGE[page_id][project_id] = {**base, **researched_case}

PRESS_RELEASES = (
    {"title": "ClineFlow makes AI context portable across chats, agents, and teams", "date": "2026-09-01", "url": "https://www.newswire.com/news/waken-ai-clineflow-makes-ai-context-portable-across-chats-agents-and-teams", "source": "Waken AI release"},
    {"title": "WakenAI launches BTwin AI Friends", "date": "2024-07-10", "url": "https://www.prnewswire.com/news-releases/wakenai-launches-btwin-ai-friends-the-first-emotional-support-network-inspired-by-clones-of-your-loved-and-not-so-loved-ones-302193521.html", "source": "Waken AI release"},
    {"title": "BRB2Me's AI Friends", "date": "2024-01-01", "url": "https://www.newswire.com/news/brb2mes-ai-friends-pioneer-the-future-of-the-1b-emotional-wellness-22318265", "source": "Waken AI release"},
)
