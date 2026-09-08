"""Project facts checked against public sources on 2026-09-07.

Press releases and App Store descriptions are issuer claims; repository docs
and the TwinChat paper are first-party evidence, not independent evaluation.
Page-specific records keep mobile delivery separate from agent architecture.
"""

RESEARCH_SOURCES = {
    "viddy-wired": {"label": "WIRED · Dec 2012", "kind": "Independent reporting", "url": "https://www.wired.com/2012/12/viddy-app-launches-on-android/"},
    "viddy-chart": {"label": "TechCrunch · Apr 2012", "kind": "Independent reporting", "url": "https://techcrunch.com/2012/04/18/viddy-tops-app-store/"},
    "ultrakam-remote-review": {"label": "AppGefahren · 2014", "kind": "Hands-on review", "url": "https://www.appgefahren.de/ultrakam-video-app-iphone-98831.html"},
    "spree-cfda": {"label": "CFDA · Nov 2025", "kind": "Industry partner interview", "url": "https://cfda.com/news/cfda-x-spreeai-how-the-future-of-fashion-meets-ai-with-a-human-touch/"},
    "spree-product": {"label": "SpreeAI platform", "kind": "Current product documentation", "url": "https://spreeai.com/product"},
    "community-funding": {"label": "Variety / Yahoo · Apr 2021", "kind": "Independent reporting", "url": "https://finance.yahoo.com/news/community-text-messaging-platform-celebs-131925689.html"},
    "btwin-app-store": {"label": "BTwin · App Store", "kind": "Developer listing", "url": "https://apps.apple.com/us/app/btwin-ai-friends-life-coaching/id6446806020"},
    "btwin-coverage": {"label": "Cybernews · Jul 2024", "kind": "Independent coverage · includes privacy critique", "url": "https://cybernews.com/privacy/btwin-ai-emotional-support-app-privacy/"},
    "twinchat-study": {"label": "TwinChat production study", "kind": "Author-published research", "url": "https://hassanvfx.github.io/twinchat-paper/"},
    "twinchat-launch": {"label": "TwinChat · May 2023", "kind": "Company release", "url": "https://www.newswire.com/news/ai-podcast-invasion-twinchat-ai-disrupts-social-media-with-10-000-22044933"},
    "twinchat-copycat": {"label": "TwinChat Copycat · Jul 2023", "kind": "Company release", "url": "https://www.newswire.com/news/mind-cloning-is-here-twinchat-brings-to-life-ai-twins-from-any-22074117"},
    "twinchat-spotlight": {"label": "Best Mobile App Awards · Jun 2023", "kind": "Founder interview", "url": "https://bestmobileappawards.com/blog/app-spotlight-twinchat"},
    "meme-app-store": {"label": "Meme Arcade · App Store", "kind": "Developer listing", "url": "https://apps.apple.com/es/app/meme-arcade-games/id6801929719"},
    "community-mobile": {"label": "Community mobile app", "kind": "Current product documentation", "url": "https://community.com/mobile-app"},
    "flyr-templates": {"label": "Flyr · Apr 2018", "kind": "Company release", "url": "https://www.prnewswire.com/news-releases/mexican-startup-raised-us6m-to-democratize-social-tv-advertisement-300626158.html"},
    "flyr-techcrunch": {"label": "TechCrunch · Mar 2017", "kind": "Independent launch coverage", "url": "https://techcrunch.com/2017/03/13/flyr-launch/"},
    "ultrakam-engadget": {"label": "Engadget · Mar 2014", "kind": "Independent launch coverage", "url": "https://www.engadget.com/2014-03-31-ultrakam-app-2k-film-video-iphone-ipad.html"},
}


def fact(value, label, detail, scope, source):
    return dict(value=value, label=label, detail=detail, scope=scope, source=source)


RESEARCH_CASES = {
    "agentic-ai": {
        "clineflow": {
            "contribution_source": "clineflow-repo",
            "thesis": "Project memory that survives the next chat.",
            "contribution": "Created a Git-native knowledge workflow that records decisions, verification, and next steps beside the code. Agent instructions recover that context and update it as part of the commit workflow.",
            "highlights": (
                fact("OKF", "Open knowledge format", "The free book presents project knowledge as open, inspectable files that can travel between AI tools.", "Knowledge architecture", "clineflow-ebook"),
                fact("Git", "Code and context together", "Task journals and additive update records preserve project decisions in version history.", "Workflow", "clineflow-repo"),
                fact("6 agents", "Native instruction files", "The repository documents Cline, Codex, Claude Code, Cursor, Copilot, and Windsurf integration.", "Documented compatibility", "clineflow-repo"),
                fact("Portable", "An open file contract", "Markdown, YAML, and links carry knowledge between tools and collaborators.", "Project continuity", "clineflow-print"),
            ),
        },
        "btwinfriends": {
            "role": "Principal Engineer",
            "thesis": "Turn conversation history into an adaptive companion.",
            "contribution": "Built the companion system around imported relationship context, multi-model orchestration, and persistent profiles. The shared TwinChat research documents the conversation corpus and memory techniques behind this work.",
            "contribution_source": "resume", "additional_source": "twinchat-study",
            "highlights": (
                fact("3 models", "Model orchestration", "Integrated OpenAI, Gemini, and Claude in the companion backend, as documented in the career record.", "My contribution", "resume"),
                fact("WhatsApp", "Context from real exchanges", "The July 2024 launch describes creating companion simulations from imported message histories.", "Released capability", "btwin-release"),
                fact("20K", "Conversations studied", "The author-published study reports 200,000 generated messages across the shared character system.", "Reported research corpus", "twinchat-study"),
                fact("Profiles", "Inspect the companion’s traits", "Launch coverage describes visible cognitive and emotional profiles, alongside questions about data privacy.", "Product transparency", "btwin-coverage"),
            ),
        },
        "twinchat": {
            "role": "Principal Engineer",
            "thesis": "A repeatable architecture for consistent character agents.",
            "contribution": "Built a persona system that extracts a character profile, reinjects it into each turn, and adapts behavior to the conversation category. The published study exposes the prompts and implementation patterns.",
            "contribution_source": "twinchat-study",
            "highlights": (
                fact("30+", "Behavioral constraints", "Five profiling prompts build character traits; identity and behavioral rules return in every generation turn.", "Documented architecture", "twinchat-study"),
                fact("10K+", "A reusable persona system", "The May 2023 launch reported a catalog spanning historical figures, experts, and fictional characters.", "Company-reported deployment", "twinchat-launch"),
                fact("Async", "Dialogue without a live session", "The founder interview describes on-demand, interactive conversations between character agents.", "Interaction architecture", "twinchat-spotlight"),
                fact("Copycat", "Text-to-persona creation", "The July 2023 release documents custom twins built from WhatsApp messages or manually supplied text.", "Public product release", "twinchat-copycat"),
            ),
        },
        "newsmusic": {
            "role": "Principal Engineer",
            "thesis": "One orchestration flow from news to a finished music video.",
            "contribution": "Built a staged pipeline for news transcripts, original lyrics, generated music and images, video assembly, and YouTube metadata. Dry runs and private uploads make intermediate results reviewable.",
            "highlights": (
                fact("5 feeds", "Configured news intake", "The default configuration includes Reuters, BBC News, PBS NewsHour, Al Jazeera English, and DW News; these are inputs, not partners.", "Repository defaults", "newsmusic-repo"),
                fact("2 styles", "Music generation presets", "Pop and Urban Hip Hop / Trap are the documented active styles for generated songs.", "Generation configuration", "newsmusic-repo"),
                fact("Dry run", "Inspect before generation", "Exercises orchestration without paid media generation, rendering, or upload.", "Workflow control", "newsmusic-repo"),
                fact("Private", "Review before publishing", "The default YouTube upload profile is private and requires review.", "Delivery default", "newsmusic-repo"),
            ),
        },
        "lyrics-refiner": {
            "role": "Principal Engineer",
            "thesis": "Five stages of arrangement, with the writer’s words preserved.",
            "contribution": "Built a local arrangement studio for Spanish lyrics and Regional Mexican styles. It combines genre analysis, optional reference matching, musical annotations, and explicit word-preservation checks.",
            "highlights": (
                fact("5 stages", "Inspectable generation", "Structure, reference matching, semantic optimization, musical annotations, and ad-libs form the documented flow.", "Prompt orchestration", "lyrics-refiner-repo"),
                fact("Validation", "Keep the original words", "A deterministic check verifies that source words remain present in the arrangement.", "Output verification", "lyrics-refiner-repo"),
                fact("Phonetics", "Spanish TTS guidance", "Pronunciation suggestions are displayed separately from the source used for generation.", "Language tooling", "lyrics-refiner-repo"),
                fact("10", "In-memory versions", "Inspect intermediate stages, compare recent versions, and export the final arrangement.", "Local review workflow", "lyrics-refiner-repo"),
            ),
        },
    },
    "mobile-apps": {
        "spreeai": {
            "highlights": (
                fact("SwiftUI", "Native commerce foundation", "Led modular iOS architecture, connecting ARKit, LiDAR, and 3D visualization to cloud assets and automated releases.", "My contribution · 2020–2023", "resume"),
                fact("1 photo", "A lightweight try-on entry", "The current platform starts with a shopper photo or a representative digital twin, without requiring a body scan.", "Current product · later evolution", "spree-product"),
                fact("Embedded", "Shopping inside the brand", "The 2025 CFDA interview describes try-ons integrated into brand websites, apps, and in-store experiences.", "Later product · Nov 2025", "spree-cfda"),
                fact("Fit", "Size guidance alongside visuals", "The May 2025 announcement describes virtual try-on and size prediction as connected parts of the shopping experience.", "Later product · May 2025", "spree-valuation"),
            ),
        },
        "meme-arcade": {
            "role": "Principal Engineer",
            "thesis": "An iPhone arcade for discovering and instantly playing web games.",
            "contribution": "Built a mobile discovery experience around swipe browsing, in-app play, saved favorites, and local play history. The App Store listing documents the released experience; the companion book covers the iOS architecture.",
            "contribution_source": "meme-app-store", "additional_source": "meme-arcade-book",
            "highlights": (
                fact("Instant", "Play within the app", "Browse a rotating feed and enter a web game directly from the native discovery surface.", "Released capability", "meme-app-store"),
                fact("On-device", "Favorites and play history", "Save games for later and revisit recent plays from the local profile.", "Product continuity", "meme-app-store"),
                fact("SwiftUI", "Native discovery architecture", "The engineering guide covers SwiftUI, Combine, and web-game integration.", "Technical book", "meme-arcade-book"),
                fact("SPM", "Reusable product modules", "The guide explains package boundaries, persistence, notifications, and observability.", "Technical book", "meme-arcade-book"),
            ),
        },
        "btwinfriends": {
            "role": "Principal Engineer",
            "thesis": "A mobile companion built around import, conversation, and return visits.",
            "contribution": "Built the native client, subscriptions, and analytics for BTwin Friends. The public iOS listing documents text imports, coaching personas, and conversation continuation; the launch release establishes its 2024 rollout.",
            "contribution_source": "resume", "additional_source": "btwin-app-store",
            "highlights": (
                fact("12+", "Languages at launch", "The July 2024 release names English, Spanish, French, Hindi, and Japanese among the supported languages.", "Launch availability", "btwin-coverage"),
                fact("WhatsApp", "Import a relationship", "The launch documents bringing message history into a custom companion’s setup.", "Mobile onboarding", "btwin-release"),
                fact("13+", "Coaching personas", "The App Store description lists a selection of AI coaches alongside custom companions.", "Developer-listed catalog", "btwin-app-store"),
                fact("Subscriptions", "Native product delivery", "Built the SwiftUI client, subscription flow, and analytics supporting repeat visits and paid access.", "My contribution", "resume"),
            ),
        },
        "twinchat": {
            "role": "Principal Engineer",
            "thesis": "Character discovery and interactive dialogue, launched on iOS.",
            "contribution": "Created an iOS conversation product with a large character catalog and custom twin creation. Contemporary launch material and the founder interview document the mobile experience and its asynchronous, podcast-like conversations.",
            "contribution_source": "twinchat-spotlight", "additional_source": "twinchat-launch",
            "highlights": (
                fact("10K+", "Character catalog", "The May 2023 release reports personalities spanning public figures, experts, and fictional characters.", "Company-reported catalog", "twinchat-launch"),
                fact("iOS", "First release platform", "The June 2023 interview confirms the initial iOS release; web and Android were plans at that time.", "Launch history", "twinchat-spotlight"),
                fact("Import", "Make a custom twin", "The Copycat release documents a twin editor using WhatsApp history or manually entered text, with an in-app tutorial.", "Mobile creation flow", "twinchat-copycat"),
                fact("8", "Conversation modes", "The author’s study describes modes spanning character chat, coaching, and other simulations.", "Product research", "twinchat-study"),
            ),
        },
        "community": {
            "highlights": (
                fact("10M+", "Platform users", "Fast Company reported nearly 20 million members by September 2020.", "Company scale · 2020", "community-scale"),
                fact("Native iOS", "Platform migration", "Helped migrate key React Native surfaces and introduced SwiftUI, Combine, and MVVM.", "My contribution · 2019–2020", "resume"),
                fact("Campaigns", "A complete mobile workflow", "Today’s product page documents campaign creation, replies, audience reports, and QR-code growth tools.", "Current product · later evolution", "community-mobile"),
                fact("Global talent", "Direct audience relationships", "January 2020 coverage documents adoption by Jennifer Lopez, Paul McCartney, and the Jonas Brothers.", "Early product adoption", "community-talent"),
            ),
        },
        "ultrakam": {
            "highlights": (
                fact("2K", "Beyond the stock camera", "Launch coverage documents 2240 × 1672 capture on iPhone 5s, with selectable frame rates and codecs.", "Documented capability", "ultrakam-launch"),
                fact("120fps", "Slow-motion capture", "Engadget documented 120fps slow motion on iPhone 5s.", "Independent launch coverage", "ultrakam-engadget"),
                fact("WWDC14", "Featured by Apple", "Ultrakam Remote Control appeared in Session 709 on nearby networking.", "Apple presentation", "wwdc14"),
                fact("2 apps", "Camera and remote", "A hands-on review documents a separate Bluetooth remote operated from a second iOS device.", "Product system", "ultrakam-remote-review"),
            ),
        },
        "flyr": {
            "thesis": "A mobile rendering engine for fast, editable video stories.",
            "contribution": "Co-founded FlyrTV and led its rendering and template architecture. The launch described a proprietary playback engine, editable stories, interactive links, and export for multiple social formats.",
            "contribution_source": "resume", "additional_source": "flyr-launch",
            "highlights": (
                fact("10K+", "Customizable templates", "The April 2018 release reports a library produced with Renderfam Studios.", "Company-reported library", "flyr-templates"),
                fact("Instant", "Publish without a render wait", "TechCrunch observed immediate story publishing with interactive elements.", "Independent launch coverage", "flyr-techcrunch"),
                fact("Editable", "Change a published story", "The launch documents modifying stories after publication through the proprietary playback engine.", "Documented capability", "flyr-launch"),
                fact("1M", "User-created projects", "Flyr reported one million projects and more than 13,000 paid subscribers in April 2018.", "Reported adoption · Apr 2018", "flyr-traction"),
            ),
        },
    },
}


STARTUP_RESEARCH_CASES = {
    "ultrakam": {"highlights": RESEARCH_CASES["mobile-apps"]["ultrakam"]["highlights"]},
    "flyr": {"highlights": (
        fact("$6M", "Capital raised", "Funding reported in April 2018 to bring professional video creation to mobile.", "Company funding", "flyr-traction"),
        fact("13K", "Paying subscribers", "Flyr reported more than 13,000 paid subscribers and one million projects in April 2018.", "Company-reported traction", "flyr-templates"),
        fact("Instant", "A differentiated video engine", "Immediate publishing with interactive stories.", "Launch coverage", "flyr-techcrunch"),
        fact("Pond5", "Acquisition", "Founder account of the product’s exit, also documented in the résumé.", "Company outcome", "founder-interview"),
    )},
    "viddy": {"highlights": (
        fact("40M+", "Registered users", "WIRED reported 40 million registered accounts in December 2012; this measures sign-ups, not active users.", "Historical company scale", "viddy-wired"),
        fact("iOS + Android", "Cross-platform VFX", "Architected rendering and visual effects for both mobile platforms.", "My contribution", "resume"),
        fact("#1", "Top free iPhone app", "Reached the App Store’s top free position in April 2012.", "Historical chart milestone", "viddy-chart"),
        fact("Fullscreen", "Acquisition", "Acquired-company status confirmed by Viddy investor NEA.", "Company outcome", "viddy-exit"),
    )},
    "spreeai": {"highlights": (
        fact("$1.5B", "Reported valuation", "Announced in May 2025, after my Dec 2020–Apr 2023 role.", "Later company milestone", "spree-valuation"),
        fact("Native iOS", "Commerce architecture", "Led the modular SwiftUI foundation for AR capture, 3D experiences, cloud assets, and automated releases.", "My contribution", "resume"),
        fact("CFDA", "Fashion industry collaboration", "A November 2025 CFDA event brought SpreeAI together with Alice + Olivia to discuss AI in retail.", "Later industry milestone", "spree-cfda"),
        fact("3 journeys", "Beyond the product page", "The current platform describes online shopping, in-store assistance, and remote clienteling.", "Current product · later evolution", "spree-product"),
    )},
    "community": {"highlights": (
        fact("10M+", "Platform users", "Fast Company reported nearly 20 million members by September 2020.", "Company scale · 2020", "community-scale"),
        fact("Global talent", "Direct fan connections", "Early adopters included Jennifer Lopez, Paul McCartney, Kerry Washington, and the Jonas Brothers.", "Company adoption", "community-talent"),
        fact("Native iOS", "Platform migration", "Helped migrate React Native surfaces and introduce SwiftUI, Combine, and MVVM.", "My contribution · 2019–2020", "resume"),
        fact("$40M", "Salesforce Ventures investment", "An additional funding round was announced in April 2021, after my role ended.", "Later company funding", "community-funding"),
    )},
    "waken": {"highlights": (
        fact("~10%", "Paid conversion", "BTwin focused acquisition tests on a $9.99 weekly plan; résumé-reported results.", "Product experiment", "resume"),
        fact("12+", "Languages at launch", "The July 2024 BTwin release announced availability in the US, UK, Canada, and other selected markets.", "Company launch", "btwin-release"),
        fact("20K", "Conversations studied", "The author-published character study reports a corpus of 200,000 generated messages.", "Reported research corpus", "twinchat-study"),
        fact("Git", "Portable agent memory", "ClineFlow keeps project knowledge in open files that travel with the code.", "Open-source product", "clineflow-repo"),
    )},
}
