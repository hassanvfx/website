"""
Portfolio Data - Impact First Structure
"""

# Core Identity
IDENTITY = {
    "name": "Hassan Uriostegui",
    "status": "EB1A Systems Engineer",
    "title": "Silicon Valley Innovator | AI Pioneer | Author",
    "email": "hassan.uriostegui@gmail.com",
    "portrait": "https://images.squarespace-cdn.com/content/v1/63bb0ee9acd2b07dec642a7b/db719a43-cc9c-4930-b4f8-21112bb508d3/HassanUriostegui1.jpeg?format=1500w",
    "footer_bio": [
        "Hassan Uriostegui is an AI-native principal engineer, founder, and author building agentic systems, consumer products, and mobile platforms. He created ClineFlow to give AI agents durable, auditable project memory across chats, tools, and collaborators.",
        "His work spans context engineering, iOS, real-time systems, and generative workflows—from 0-to-1 products to platforms used by millions."
    ],
    "quote": "Intelligence might be appreciated as the most primitive form of life. As such, the Universe won't be just a pathway full of intelligent life, but an absolute reflection of human awareness."
}

# PROFESSIONAL PROFILE / RESUME
PROFESSIONAL_PROFILE = {
    "eyebrow": "Professional Profile",
    "title": "AI-Native Principal / Founding Engineer",
    "summary": "Building agentic systems, mobile products, and consumer platforms that turn ambitious ideas into resilient, high-impact experiences.",
    "pdf": "assets/hassan-uriostegui-resume-2026-12.pdf",
    "preview": "assets/hassan-uriostegui-resume-2026-12-page-1.png",
    "preview_alt": "First page of Hassan Uriostegui's professional profile and resume.",
    "download_label": "Download Resume (PDF)",
    "open_label": "Open Fullscreen"
}

# Bio/EB1A Overview - Like a famous artist portfolio intro
BIO = {
    "headline": "A Silicon Valley Visionary Shaping the Future of AI",
    "headline_link": "https://medium.com/authority-magazine/hassan-uriostegui-on-the-future-of-artificial-intelligence-a013ebee514e",
    "image": "assets/hassan-silicon-valley-profile.jpg",
    "image_alt": "Hassan Uriostegui standing on a rooftop terrace with a city skyline behind him.",
    "eb1a_overview": {
        "title": "EB1A Extraordinary Ability Recognition",
        "description": "In 2018, Hassan was granted U.S. Citizenship through the EB1A category—reserved for individuals who demonstrate extraordinary ability in sciences, arts, education, business, or athletics. This recognition is awarded to only 0.1% of visa applicants.",
        "wikipedia_url": "https://en.wikipedia.org/wiki/Alien_of_extraordinary_ability#EB-1A_(E11/E16)",
        "criteria_met": [
            "Published works of major significance (4 books on AI for general audiences)",
            "Original contributions to the field (Patents, first-of-kind mobile technologies)",
            "Judging the work of others (Industry expert, VES Member)",
            "High remuneration for services (Silicon Valley executive roles)",
            "Lead/critical role in distinguished organizations (CTO, Principal Architect)"
        ]
    }
}

# Section Divider Quotes - From articles/press mentioning his work
SECTION_QUOTES = [
    {
        "quote": "Flyr was the first third-party company granted access to Snapchat's content API, a testament to their groundbreaking work in mobile video storytelling.",
        "source": "TechCrunch",
        "url": "https://techcrunch.com/2017/03/13/flyr-launch/",
        "context": "On FlyrTV's exclusive Snapchat partnership"
    },
    {
        "quote": "Hassan Uriostegui explores whether ChatGPT could be sentient, diving deep into the philosophical and technical implications of artificial consciousness.",
        "source": "Korea Biz Wire",
        "url": "http://koreabizwire.com/is-chatgpt-sentient-the-question-is-answered-in-i-ai-by-waken-ai-founder-hassan-uriostegui",
        "context": "On 'I, AI: Nemo's Mirror'"
    },
    {
        "quote": "Our AI delves into the human essence, giving voice to silent thoughts.",
        "source": "BTwin AI Mission Statement",
        "url": "https://btwinai.com",
        "context": "On digital twin therapy"
    },
    {
        "quote": "Ultrakam 4K video app arrives for iPhone 6, bringing professional cinematography to mobile devices.",
        "source": "Forbes",
        "url": "https://www.forbes.com",
        "context": "On mobile innovation"
    },
    {
        "quote": "The intersection of AI and human consciousness presents profound questions about the nature of awareness itself.",
        "source": "Authority Magazine",
        "url": "https://medium.com/authority-magazine/hassan-uriostegui-on-the-future-of-artificial-intelligence-a013ebee514e",
        "context": "Interview on AI ethics"
    },
]

# Key Stats (impressive numbers first)
STATS = [
    {"value": "40M+", "label": "Users Impacted"},
    {"value": "$6M+", "label": "Funding Raised"},
    {"value": "3", "label": "Startup Exits"},
    {"value": "7", "label": "Books Published"},
]

# Primary navigation
NAV_ITEMS = [
    {"label": "HOME", "href": "#home"},
    {"label": "RESUME", "href": "#professional-profile"},
    {"label": "AI-CODING", "href": "#clineflow", "featured": True},
    {"label": "APPS", "href": "#memearcade", "featured": True},
    {"label": "CITATIONS", "href": "#citations"},
    {"label": "BOOKS", "href": "#books"},
]

# Secondary navigation
SUBMENU_ITEMS = [
    {"label": "IMPACT", "href": "#impact"},
    {"label": "RESEARCH", "href": "#twinchat-paper"},
    {"label": "FILMS", "href": "#filmography"},
    {"label": "PRESS", "href": "#press"},
    {"label": "CONTACT", "href": "#contact"},
]

# Social Links
SOCIAL_LINKS = [
    {"label": "LinkedIn", "url": "https://www.linkedin.com/in/bensabbah"},
    {"label": "GitHub", "url": "https://github.com/hassanvfx"},
    {"label": "IMDB", "url": "https://www.imdb.com/name/nm2843359/"},
    {"label": "Medium", "url": "https://uriostegui.medium.com"},
]

# IMPACT SECTION - The impressive exits (show first!)
HISTORIC_COMPANIES = [
    {
        "id": "spreeai",
        "name": "SpreeAI",
        "year": "2024-Present",
        "role": "Principal iOS Architect",
        "highlight": "Naomi Campbell Board Member | AI Fashion",
        "description": "Building AI-powered virtual try-on technology for fashion e-commerce. SpreeAI transforms how customers shop online with real-time garment visualization. Partners include CFDA, MIT, Carnegie Mellon, and major fashion brands.",
        "video": "https://player.vimeo.com/video/1143600495",
        "stats": "AI Fashion Revolution",
        "press_quote": {
            "quote": "SpreeAI is pushing the forefront of e-commerce personalization, by leveraging collaborations with academia and assembling a team that understands both the deep technical challenges and their product impact.",
            "source": "Professor Deva Ramanan",
            "source_title": "CMU Robotics Institute Professor"
        }
    },
    {
        "id": "viddy",
        "name": "Viddy",
        "year": "2012-2013",
        "role": "Director of Video Engineering",
        "highlight": "$370M Valuation | 40M Users",
        "description": "Built iOS + Android VFX rendering engine. Created the most advanced video editor when Instagram was photos-only. At peak engagement, served 40M+ users.",
        "video": "https://www.youtube.com/embed/avccq32KfOE",
        "stats": "$370M peak valuation",
        "press_quote": {
            "quote": "Viddy, the video-sharing app that has been called 'Instagram for video,' raised $30 million in funding at a valuation of $370 million.",
            "source": "The Wall Street Journal",
            "source_title": "on Viddy's funding round"
        }
    },
    {
        "id": "flyr",
        "name": "FlyrTV",
        "year": "2014-2018",
        "role": "CTO & Co-founder",
        "highlight": "$6M Raised | Acquired 2018",
        "description": "Raised $6M+, built team of 30 professionals, launched 10,000+ HD video templates. First company to access Snapchat's content API. Acquired by POND5.",
        "video": "https://www.youtube.com/embed/7GQm8h70PRg",
        "stats": "$6M raised",
        "press_quote": {
            "quote": "Flyr was the first third-party company granted access to Snapchat's content API, a testament to their groundbreaking work in mobile video storytelling.",
            "source": "TechCrunch",
            "source_title": "on FlyrTV's Snapchat partnership"
        }
    },
    {
        "id": "community",
        "name": "Community",
        "year": "2019-2020",
        "role": "Principal iOS Architect",
        "highlight": "Backed by Madonna & Ashton Kutcher",
        "description": "Implemented Princeton CS Ph.D. paper in Swift. Architected reactive iOS app. Built and led iOS team of 5 engineers in 6 months.",
        "video": "https://www.youtube.com/embed/ZOWuy-HhQxE",
        "stats": "Millions of users",
        "press_quote": {
            "quote": "Community has raised $35 million in new funding to bring celebrities closer to their fans through direct messaging.",
            "source": "Forbes",
            "source_title": "on Community's Series A"
        }
    },
]

# APPLE WWDC14 - ULTRAKAM REMOTE CONTROL
WWDC14_FEATURE = {
    "eyebrow": "Apple WWDC14 Recognition",
    "title": "Featured by Apple at WWDC14",
    "subtitle": "Ultrakam Remote Control selected for Apple's \"Cross Platform Nearby Networking\" session",
    "description": "In 2014, Apple requested permission to include assets from Ultrakam Remote Control in a Worldwide Developers Conference presentation. The app was subsequently featured in the official WWDC14 Session 709 presentation.",
    "quote": "Selected by Apple as an example of good design.",
    "slide_image": "assets/wwdc14-session-709-slide-6.png",
    "slide_alt": "Slide 6 of Apple's WWDC14 Session 709 presentation, showing Ultrakam Remote Control's blue clapperboard and remote-control icon among selected apps.",
    "icon_image": "assets/ultrakam-remote-control-icon.png",
    "icon_alt": "Blue Ultrakam Remote Control icon with a movie clapperboard and remote control.",
    "email_image": "assets/apple-wwdc14-ultrakam-permission-email.png",
    "email_alt": "Apple email requesting permission to use Ultrakam Remote Control assets at WWDC 2014 as an example of good design.",
    "pdf_url": "assets/wwdc14-session-709-cross-platform-nearby-networking.pdf",
    "video_url": "https://nonstrict.eu/wwdcindex/wwdc2014/709/?t=2604",
    "medium_url": "https://uriostegui.medium.com/the-time-apple-featured-my-app-at-wwdc14-a42dc4cd19bb?postPublishedType=initial"
}

# CURRENT AI WORK (2022-2025)
CURRENT_PROJECTS = [
    {
        "id": "twinchat",
        "name": "TwinChat",
        "year": "2023-Present",
        "description": "AI-Podcast platform that disrupts social media with 10,000 famous personalities' Mind-Deepfakes. Revolutionary AI that creates compelling conversational experiences with celebrity digital twins.",
        "stats": "10,000+ AI Personalities",
        "website": "https://btwinai.com/",
        "vimeo_channel": "https://vimeo.com/twinchat",
        "videos": [
            {"url": "https://player.vimeo.com/video/839937602", "title": "TwinChat Demo"},
            {"url": "https://player.vimeo.com/video/825294756", "title": "TwinChat AI Conversations"},
            {"url": "https://player.vimeo.com/video/824932537", "title": "TwinChat Features"},
        ],
        "quote": "Unlocking VIP Celebrity conversations through AI."
    },
    {
        "id": "btwinfriends",
        "name": "BTwin Friends",
        "year": "2024-Present",
        "description": "Advanced AI platform creating cognitive profiles for conversational simulations. Emotionally responsive AI companions that enhance user interaction with highly accurate personality profiles. Evolution of BRB2Me mind simulation research.",
        "stats": "20,000 conversations | 200,000 messages",
        "website": "https://btwinai.com/",
        "videos": [
            {"url": "https://player.vimeo.com/video/1005370651", "title": "BTwin Friends"},
        ],
        "quote": "Our AI delves into the human essence, giving voice to silent thoughts."
    },
    {
        "id": "brb2me",
        "name": "BRB2Me",
        "year": "2020-2022",
        "description": "Pioneering mind simulation platform that laid the foundation for BTwin Friends. Early research into cognitive profiling and conversational AI companions with therapeutic applications.",
        "stats": "Mind Simulation Pioneer",
        "videos": [
            {"url": "https://player.vimeo.com/video/913284078?h=82df73027a", "title": "BRB2Me Demo"},
        ],
        "quote": "The predecessor to modern AI mind simulation."
    },
    {
        "id": "sendkarma",
        "name": "SendKarma",
        "year": "2025",
        "description": "Sadhguru-inspired AI wellness companion delivering wisdom and guidance through accessible channels.",
        "stats": "AI Wellness",
        "website": "https://www.sendkarma.app/",
        "videos": [
            {"url": "https://player.vimeo.com/video/1138631992", "title": "SendKarma"},
        ]
    },
]

# INTERVIEWS SECTION
INTERVIEWS = [
    {
        "url": "https://player.vimeo.com/video/1001075745",
        "title": "AI & Future of Technology",
        "context": "Interview on AI ethics and innovation"
    },
    {
        "url": "https://player.vimeo.com/video/843499496",
        "title": "Silicon Valley Journey",
        "context": "Career retrospective"
    },
    {
        "url": "https://player.vimeo.com/video/843495231",
        "title": "Entrepreneurship & Innovation",
        "context": "Startup insights"
    },
]

# AI INFLUENCER SIMULATION - Featured Callout
AI_INFLUENCER = {
    "name": "AI Influencer Simulation",
    "tagline": "State-of-the-Art Simulated Influencers",
    "subtitle": "November 2025 - Cutting Edge AI Video Generation",
    "description": "Showcasing the latest advancements in AI-generated influencer content. These simulated personalities demonstrate the state-of-the-art in realistic AI video generation as of November 2025.",
    "videos": [
        {"url": "https://player.vimeo.com/video/1137579986", "title": "AI Influencer Demo 1"},
        {"url": "https://player.vimeo.com/video/1137973511", "title": "AI Influencer Demo 2"},
    ],
    "quote": "The future of digital personalities is here.",
    "positioning": "Pushing the boundaries of AI-generated human simulation."
}

# AI PRODUCT SHOTS - Featured Callout
AI_PRODUCT_SHOTS = {
    "name": "AI Product Shots",
    "tagline": "State-of-the-Art Generative Motion Graphics AI",
    "subtitle": "November 2025 - Revolutionary Product Visualization",
    "description": "Revolutionary AI-powered motion graphics system for automated product visualization and video generation. Pushing the boundaries of what's possible with generative AI in late 2025.",
    "videos": [
        {"url": "https://player.vimeo.com/video/1144077038", "title": "AI Product Shots Demo"},
    ],
    "quote": "Transforming product marketing through AI-generated motion graphics.",
    "positioning": "State-of-the-art November 2025 generation motion graphics AI technology."
}

# WAKEN AI LABS - Featured Callout
WAKEN_AI = {
    "name": "Waken AI",
    "tagline": "A New Lux — Elevating The Human Mind",
    "subtitle": "Mind Simulation Technology for Emotional Wellness",
    "description": "Waken AI Labs represents Hassan's ongoing research into artificial consciousness and mind simulation. From BTwin Friends to TwinChat and MST, this work pioneers the intersection of AI and human emotional wellness through advanced conversational companions.",
    "logo": "https://images.squarespace-cdn.com/content/v1/63bb0ee9acd2b07dec642a7b/9a4b6ba5-4ce5-4cb4-9750-7b9be4b2de0e/waken-ai-black.png?format=1500w",
    "video": "https://player.vimeo.com/video/960460813",
    "website": "https://www.wakenai.com/",
    "quote": "Our AI delves into the human essence, giving voice to silent thoughts.",
    "positioning": "Pioneering Mind Simulation Technology for emotional wellness and personal growth since 2020."
}

# AI COPYRIGHT WEIGHTS - CITATIONS
FEATURED_BOOKS = [
    {
        "title": "ClineFlow and Google's Open Knowledge Format",
        "subtitle": "Build Durable AI Memory for Developers, Lawyers, and Creatives",
        "eyebrow": "New Book · 2026",
        "image": "assets/infinite-ai-context-cover.jpg",
        "image_alt": "Cover of Infinite AI Context: ClineFlow and Google's Open Knowledge Format by Hassan Uriostegui",
        "url": "https://www.lulu.com/shop/hassan-uriostegui/infinite-ai-context-clineflow-and-googles-open-knowledge-format/paperback/product-rmkn8jg.html?page=1&pageSize=4",
        "ebook_url": "https://hassanvfx.github.io/infinite-ai-context/downloads/infinite-ai-context-web.pdf",
        "cta_url": "https://clineflow.com/",
        "cta_label": "www.ClineFlow.com",
        "description": "A practical guide to persistent AI context, ClineFlow, and Google's Open Knowledge Format—designed for people building durable AI memory across development, legal, and creative work.",
        "layout": "cover-first"
    },
    {
        "title": "AI From Tensors to Agents on Mac Silicon",
        "subtitle": "Learning Modern AI by Learning It on Apple Silicon",
        "eyebrow": "New Book · 2026",
        "image": "assets/ai-from-tensors-to-agents-cover.jpg",
        "image_alt": "Cover of AI From Tensors to Agents on Mac Silicon by Hassan Uriostegui",
        "url": "https://www.lulu.com/shop/hassan-uriostegui/ai-from-tensors-to-agents-on-mac-silicon/hardcover/product-e7qy7gy.html?page=1&pageSize=4",
        "ebook_url": "https://hassanvfx.github.io/website/assets/ai-from-tensors-to-agents-free-ebook.pdf",
        "description": "A hands-on, build-first guide to making modern AI work locally on Apple Silicon—from tensors and neural networks to retrieval, evaluation, human approval, and reliable agents.",
        "layout": "cover-first"
    },
    {
        "title": "Modern iOS Architecture: Deconstructing the $3B MemeArcade",
        "subtitle": "Modular Applications with SPM, SwiftUI and Hybrid Web",
        "eyebrow": "New Book · 2026",
        "image": "assets/modern-ios-architecture-memearcade-cover.jpg",
        "image_alt": "Cover of Modern iOS Architecture: Deconstructing the $3B MemeArcade by Hassan Uriostegui",
        "url": "https://www.lulu.com/shop/hassan-uriostegui/modern-ios-architecture-deconstructing-the-3b-memearcade/hardcover/product-yvewn4y.html?page=1&pageSize=4",
        "ebook_url": "https://hassanvfx.github.io/website/assets/modern-ios-architecture-memearcade-free-ebook-2026-08-17.pdf",
        "description": "A practical guide to the modular, hybrid iOS engineering decisions behind an application inspired by MemeArcade—covering SwiftUI, Combine, SPM, async/await, WebViews, persistence, notifications, and observability.",
        "layout": "cover-first"
    }
]

CITATIONS = {
    "title": "AI-Copyright Weights",
    "eyebrow": "Research Recognition",
    "description": "A 2023 article examining whether AI model weights may raise derivative-work and compensation questions in copyright law.",
    "article_url": "https://medium.com/twinchat/ai-copyright-weights-a-new-frontier-in-intellectual-property-law-d8ee1b6c55ee",
    "image": "assets/ai-copyright-house-task-force-report.png",
    "image_alt": "Cover of the 2024 Bipartisan House Task Force Report on Artificial Intelligence",
    "house": {
        "source": "Bipartisan House AI Task Force Report",
        "title": "2024 Bipartisan House Task Force Report on Artificial Intelligence",
        "detail": "Cited in footnote 40 of the Intellectual Property chapter (printed page 117).",
        "url": "https://www.speaker.gov/wp-content/uploads/2024/12/AI-Task-Force-Report-FINAL.pdf"
    },
    "additional": [
        {
            "source": "Epic Law",
            "title": "AI-generated derivative works: the case for mandatory disclosure of weights and prompts",
            "url": "https://epic.law/ai-generated-derivative-works-the-case-for-mandatory-disclosure-of-weights-and-prompts/"
        },
        {
            "source": "SSRN / GRUR International",
            "title": "Copyright as Affirmative Action for Human Authors Until the Singularity",
            "url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4697678"
        },
        {
            "source": "Touro Law Review",
            "title": "The Author-Ity of AI",
            "url": "https://digitalcommons.tourolaw.edu/lawreview/vol39/iss2/10/"
        },
        {
            "source": "mEDRA",
            "title": "Creatività umana e intelligenza artificiale generativa",
            "url": "https://www.medra.org/servlet/view?LANG=ita&doi=10.1422%2F109012"
        }
    ]
}

# TWINCHAT PAPER - Research Publication
TWINCHAT_PAPER = {
    "name": "TwinChat Paper",
    "tagline": "AI Mind Simulation Research",
    "subtitle": "Open Source Research on Cognitive Profiling & Digital Twins",
    "logo": "https://cdn.pixabay.com/photo/2022/01/30/13/33/github-6980894_1280.png",
    "description": "The TwinChat Paper documents the theoretical foundations and technical implementation of Mind Simulation Technology (MST). This research explores how AI can create accurate cognitive profiles for conversational simulations, enabling emotionally responsive digital companions.",
    "features": [
        "Cognitive profiling methodology",
        "Digital twin creation framework",
        "Conversational AI architecture",
        "Personality simulation techniques",
        "Ethical guidelines for AI companions"
    ],
    "github": "https://github.com/hassanvfx/twinchat-paper",
    "stars": "📄 Research Publication",
    "quote": "Understanding human cognition through the lens of artificial intelligence opens new frontiers in emotional wellness and therapeutic applications.",
    "positioning": "The scientific foundation behind BTwin Friends, TwinChat, and Waken AI Labs."
}

# CLINEFLOW - Featured Hero Project
CLINEFLOW = {
    "name": "ClineFlow",
    "website": "https://clineflow.com/",
    "installer_prompt": "Please initialize a local Git repository if needed, then install ClineFlow using the instructions at https://github.com/hassanvfx/clineflow"
}

# MEME ARCADE - Featured iPhone App
MEME_ARCADE = {
    "eyebrow": "Meme Arcade for iPhone",
    "title": "Your next favorite game is one scroll away.",
    "description": "Discover bite-size games, jump straight into the action, and build your personal arcade. Meme Arcade brings quick games and the culture around them into one lively, scrollable place.",
    "url": "https://hassanvfx.github.io/meme-arcade-book/",
    "cta": "Explore Meme Arcade",
    "icon": "assets/memearcade-arcade-icon.webp",
    "icon_alt": "Neon purple Meme Arcade cabinet with pixel sunglasses and a heart speech bubble",
    "screens": [
        {"image": "assets/memearcade-play.jpg", "alt": "Meme Arcade game screen showing a fast arcade driving game with brake and gas controls", "caption": "Play instantly"},
        {"image": "assets/memearcade-discover.jpg", "alt": "Meme Arcade discovery screen with community-made games and categories", "caption": "Discover new favorites"},
        {"image": "assets/memearcade-profile.jpg", "alt": "Meme Arcade profile screen with play history, favorites, and game cards", "caption": "Track your hype"}
    ]
}

# RESEARCH & INNOVATIONS (other projects)
INNOVATIONS = [
    {
        "id": "maxwell",
        "name": "Maxwell Lux",
        "year": "2020",
        "tagline": "Bootstrap for SwiftUI",
        "description": "First Universal Design System for iOS and macOS. Presented at WWDC20 Labs. Approved for Apple Silicon early access program.",
        "video": "https://player.vimeo.com/video/435053200"
    },
    {
        "id": "onelapse",
        "name": "Onelapse",
        "year": "2013",
        "tagline": "Live Photos 2 Years Before Apple",
        "description": "Envisioned a new media type blending high-res video with photos. 'Taking photos from videos' - Apple released similar feature in 2015.",
        "video": "https://player.vimeo.com/video/66624830"
    },
    {
        "id": "cinekolor",
        "name": "Cinekolor",
        "year": "2014",
        "tagline": "Pro Color Grading Before Adobe",
        "description": "Professional 3-stage color correction with 3D LUT export for film production. Featured by Apple worldwide.",
        "video": "https://www.youtube.com/embed/g722kzRyzPo"
    },
    {
        "id": "krommy",
        "name": "Krommy",
        "year": "2011",
        "tagline": "Face Filters 10 Years Before Snapchat",
        "description": "After releasing Kromath (first real-time Green Screen for iOS), developed early face filter concept almost a decade before Snapchat.",
        "video": "https://www.youtube.com/embed/d3hvzV9KgcE"
    },
    {
        "id": "tron",
        "name": "Tron Legacy AR Engine",
        "year": "2010",
        "tagline": "AR Before ARKit",
        "description": "High-performance Augmented Reality Engine for Disney's Tron Legacy marketing. Built before modern AR frameworks existed.",
        "video": "https://www.youtube.com/embed/YXglHq-JJYI"
    },
    {
        "id": "renderfarm",
        "name": "Renderfarm X",
        "year": "2018",
        "tagline": "Patent: Intelligent Graphical Feature Generation",
        "description": "Revolutionary backend rendering using iOS engine. Reused mobile rendering for scalable server-side video processing.",
        "video": "https://www.youtube.com/embed/GET8ncM2C84"
    },
]

# FILMOGRAPHY (2006-2010)
FILMOGRAPHY = {
    "years": "2006-2010",
    "total_films": "10+",
    "roles": ["Digital Compositor", "Technical Director", "VFX Supervisor"],
    "description": "Collaborated on 10+ feature films. Winner of Ariel Awards for visual effects. Active member of Hollywood Visual Effects Society (VES).",
    "imdb": "https://www.imdb.com/name/nm2843359/",
    "ves_member": True,
    "videos": [
        {"url": "https://www.youtube.com/embed/H1D5HITPAhc", "title": "Creative Engineering 2006-2011"},
        {"url": "https://player.vimeo.com/video/1222373985", "title": "VFX Reel 2006-2011"},
    ]
}

# BOOKS
BOOKS = [
    {
        "title": "AI From Tensors to Agents on Mac Silicon",
        "subtitle": "Learning Modern AI by Learning It on Apple Silicon",
        "year": "2026",
        "language": "English",
        "url": "https://www.lulu.com/shop/hassan-uriostegui/ai-from-tensors-to-agents-on-mac-silicon/hardcover/product-e7qy7gy.html?page=1&pageSize=4",
        "ebook_url": "https://hassanvfx.github.io/website/assets/ai-from-tensors-to-agents-free-ebook.pdf",
        "press": "A build-first guide to modern AI on Apple Silicon",
        "image": "assets/ai-from-tensors-to-agents-cover.jpg",
        "portrait_cover": True
    },
    {
        "title": "Modern iOS Architecture: Deconstructing the $3B MemeArcade",
        "subtitle": "Modular Applications with SPM, SwiftUI and Hybrid Web",
        "year": "2026",
        "language": "English",
        "url": "https://www.lulu.com/shop/hassan-uriostegui/modern-ios-architecture-deconstructing-the-3b-memearcade/hardcover/product-yvewn4y.html?page=1&pageSize=4",
        "ebook_url": "https://hassanvfx.github.io/website/assets/modern-ios-architecture-memearcade-free-ebook-2026-08-17.pdf",
        "press": "Practical hybrid iOS architecture for maintainable products",
        "image": "assets/modern-ios-architecture-memearcade-cover.jpg",
        "portrait_cover": True
    },
    {
        "title": "MST: Mind Simulation Technology",
        "subtitle": "A Comprehensive Framework for Cognitive Profiling and Digital Twin Creation",
        "year": "2024",
        "language": "English",
        "url": "https://www.amazon.com/-/he/Hassan-Uriostegui/dp/1304332993",
        "press": "The definitive guide to AI personality simulation",
        "featured": True,
        "image": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765062559/this_book_cover_in_a_foto_real_display_in_a_book_store_real_fotography_k3r65iuq1nnvj1ljkmhv_1_zrz0o2.png",
        "description": "This groundbreaking work introduces the theoretical and practical foundations of Mind Simulation Technology—the science behind BTwin Friends and TwinChat. Drawing from years of research in cognitive profiling, conversational AI, and therapeutic applications, this book provides a comprehensive framework for understanding how AI can simulate human cognition, personality, and emotional intelligence."
    },
    {
        "title": "I, AI: Nemo's Mirror",
        "subtitle": "Exploring the Singular Nature of Self-Awareness in ChatGPT",
        "year": "2023",
        "language": "English",
        "url": "https://www.amazon.com/-/en/AI-Exploring-Singular-Self-Awareness-ChatGPT/dp/1365528669",
        "press": "Featured in Korea Biz Wire",
        "image": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765062694/this_book_hold_by_this_guy_in_a_startbucks_coffee_uuoxtjvsv8tpp3imnsjj_0_yj2p6m.jpg"
    },
    {
        "title": "Yo, IA: Cyberpunks",
        "subtitle": "La Inteligencia Artificial y el Espejo de Nemo",
        "year": "2023",
        "language": "Español",
        "url": "https://www.amazon.com/Yo-IA-Cyberpunks-Inteligencia-Artificial/dp/1312446501",
        "press": "Featured on Imagen Radio Mexico",
        "image": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765062693/this_book_cover_in_a_foto_real_display_in_a_book_store_real_fotography_at_barnes__noble_07l8939fc8cxlyirqp40_0_wir41f.jpg"
    },
    {
        "title": "The Fly of the Humanized Robot",
        "subtitle": "An Algorithm to Heal the Soul",
        "year": "2020",
        "language": "English",
        "url": "book/eng.pdf",
        "local": True,
        "image": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765062693/this_book_hold_by_this_guy_in_the_woods_8h7ed2ri8wqtfycbeb16_1_kd3iwp.jpg"
    },
]

# PRESS LOGOS SHOWCASE - "In the News" section
PRESS_LOGOS = [
    {"logo": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765214479/authority_magazine_logo_on_black_kpqqs5uhydk9m839b88e_0_ahq1hk.png", "name": "Authority Magazine"},
    {"logo": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765214479/forbes_logo_on_black_958c8d0mlceji9etw3d2_0_kwbfsx.png", "name": "Forbes"},
    {"logo": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765214479/techrunch_logo_on_black_r2pskd3j2ibgflk4ape1_1_dlxfyb.png", "name": "TechCrunch"},
    {"logo": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765214479/athletechnews_logo_on_black_0sqg1tayo0zrda137byl_0_gcfdee.png", "name": "Athletechnews"},
    {"logo": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765214650/cybernews_logo_on_black_ej9hnl3fibwuffvi17hb_1_r30zmn.png", "name": "CyberNews"},
    {"logo": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765214479/yahoo_news_logo_on_black_lxx9qlheyue42r3u4rnr_0_rh3pg6.png", "name": "Yahoo News"},
]

# PRESS
PRESS = [
    {
        "publication": "TechCrunch",
        "logo": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765214479/techrunch_logo_on_black_r2pskd3j2ibgflk4ape1_1_dlxfyb.png",
        "headline": "Flyr launches an app for rapid creation of Snapchat Discover-style stories",
        "excerpt": "FlyrTV becomes the first third-party company granted access to Snapchat's content API, enabling rapid creation of professional video content for Snapchat Discover.",
        "url": "https://techcrunch.com/2017/03/13/flyr-launch/",
        "year": "2017"
    },
    {
        "publication": "Forbes",
        "logo": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765214479/forbes_logo_on_black_958c8d0mlceji9etw3d2_0_kwbfsx.png",
        "headline": "Ultrakam 4K video app arrives for iPhone 6",
        "excerpt": "Revolutionary mobile video recording technology brings 4K capabilities to iPhone 6, pushing the boundaries of mobile filmmaking.",
        "url": "https://www.forbes.com",
        "year": "2014"
    },
    {
        "publication": "Authority Magazine",
        "logo": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765214479/authority_magazine_logo_on_black_kpqqs5uhydk9m839b88e_0_ahq1hk.png",
        "headline": "Hassan Uriostegui On the Future of Artificial Intelligence",
        "excerpt": "In-depth interview exploring AI ethics, digital empathy, and the future of human-AI interaction with the Waken AI founder.",
        "url": "https://medium.com/authority-magazine/hassan-uriostegui-on-the-future-of-artificial-intelligence-a013ebee514e",
        "year": "2024"
    },
    {
        "publication": "Athletechnews",
        "logo": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765214479/athletechnews_logo_on_black_0sqg1tayo0zrda137byl_0_gcfdee.png",
        "headline": "BTwin AI Friends App: Revolutionizing Emotional Wellness",
        "excerpt": "How BTwin AI Friends is transforming emotional wellness through advanced AI companions and mind simulation technology.",
        "url": "https://athletechnews.com/btwin-ai-friends-app-emotional-wellness/",
        "year": "2024"
    },
    {
        "publication": "CyberNews",
        "logo": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765214650/cybernews_logo_on_black_ej9hnl3fibwuffvi17hb_1_r30zmn.png",
        "headline": "BTwin AI Emotional Support App: Privacy Considerations",
        "excerpt": "An in-depth analysis of privacy and data protection practices in BTwin AI's emotional support platform.",
        "url": "https://cybernews.com/privacy/btwin-ai-emotional-support-app-privacy/",
        "year": "2024"
    },
    {
        "publication": "Yahoo News",
        "logo": "https://res.cloudinary.com/dmje5xfzh/image/upload/v1765214479/yahoo_news_logo_on_black_lxx9qlheyue42r3u4rnr_0_rh3pg6.png",
        "headline": "Conscious AI Imagined: ChatGPT and Waken AI",
        "excerpt": "Exploring the boundaries of AI consciousness and the philosophical implications of ChatGPT through Waken AI's research.",
        "url": "https://finance.yahoo.com/news/conscious-ai-imagined-chatgpt-waken-190000098.html",
        "year": "2023"
    },
]

# RECOGNITION
RECOGNITION = [
    {
        "year": "2020",
        "title": "EB1A Extraordinary Ability",
        "description": "U.S. Permanent Residency for extraordinary career in computer sciences"
    },
    {
        "year": "2014",
        "title": "Apple WWDC Featured",
        "description": "Ultrakam highlighted as example of outstanding design"
    },
    {
        "year": "2018",
        "title": "Patent Granted",
        "description": "Intelligent Graphical Feature Generation for User Content"
    },
    {
        "year": "2017",
        "title": "First Snapchat API Access",
        "description": "FlyrTV: First third-party company granted exclusive access"
    },
]

# Timeline markers for section intersections
TIMELINE_MARKERS = [
    {"year": "2022-2025", "label": "AI Era"},
    {"year": "2017-2020", "label": "Silicon Valley"},
    {"year": "2013-2014", "label": "Mobile Revolution"},
    {"year": "2010-2011", "label": "Innovation"},
    {"year": "2006-2010", "label": "VFX & Film"},
]
