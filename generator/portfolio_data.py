"""
Portfolio Data - Impact First Structure
"""

# Core Identity
IDENTITY = {
    "name": "Hassan Uriostegui",
    "status": "EB1A Extraordinary Ability",
    "title": "Silicon Valley Innovator | AI Pioneer | Author",
    "email": "hassan.uriostegui@gmail.com",
    "portrait": "https://images.squarespace-cdn.com/content/v1/63bb0ee9acd2b07dec642a7b/db719a43-cc9c-4930-b4f8-21112bb508d3/HassanUriostegui1.jpeg?format=1500w",
    "quote": "Intelligence might be appreciated as the most primitive form of life. As such, the Universe won't be just a pathway full of intelligent life, but an absolute reflection of human awareness."
}

# Bio/EB1A Overview - Like a famous artist portfolio intro
BIO = {
    "headline": "A Silicon Valley Visionary Shaping the Future of AI",
    "intro": "Hassan Uriostegui is a Mexican-American technologist, author, and AI pioneer whose work has touched over 40 million users worldwide. Recognized by the United States government with the prestigious EB1A visa for individuals of extraordinary ability, Hassan's career spans groundbreaking innovations in mobile video technology, AI-human interaction, and visual effects for Hollywood films.",
    "eb1a_overview": {
        "title": "EB1A Extraordinary Ability Recognition",
        "description": "In 2020, Hassan was granted U.S. Permanent Residency through the EB1A category—reserved for individuals who demonstrate extraordinary ability in sciences, arts, education, business, or athletics. This recognition is awarded to only 0.1% of visa applicants.",
        "criteria_met": [
            "Published works of major significance (4 books on AI consciousness)",
            "Original contributions to the field (Patents, first-of-kind mobile technologies)",
            "Judging the work of others (Industry expert, VES Member)",
            "High remuneration for services (Silicon Valley executive roles)",
            "Lead/critical role in distinguished organizations (CTO, Principal Architect)"
        ]
    },
    "career_summary": "From pioneering real-time video filters a decade before Snapchat to building AI systems that have processed over 200,000 therapeutic conversations, Hassan continues to push the boundaries of what's possible at the intersection of human creativity and artificial intelligence."
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
    {"value": "4", "label": "Books Published"},
]

# Navigation with ClineFlow featured
NAV_ITEMS = [
    {"label": "HOME", "href": "#home"},
    {"label": "CLINEFLOW", "href": "https://github.com/hassanvfx/clineflow", "featured": True, "external": True},
    {"label": "IMPACT", "href": "#impact"},
    {"label": "WORK", "href": "#work"},
    {"label": "RESEARCH", "href": "#research"},
    {"label": "BOOKS", "href": "#books"},
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
        "video": "https://player.vimeo.com/video/1101438413",
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
    {
        "id": "invision",
        "name": "InVision",
        "year": "2018-2019",
        "role": "Lead Mobile Developer",
        "highlight": "800 Employees | Industry Leader",
        "description": "Implemented real-time previews for Studio and iOS. Integrated Freehand editor. Refactored legacy code into modular frameworks.",
        "video": "https://www.youtube.com/embed/x3WtPVjdTNM",
        "stats": "World's design platform",
        "press_quote": {
            "quote": "InVision has become the world's leading design platform, used by 100% of the Fortune 100 companies.",
            "source": "Fast Company",
            "source_title": "on InVision's industry impact"
        }
    },
]

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
        "id": "brujaroja",
        "name": "Bruja Roja",
        "year": "2024",
        "description": "WhatsApp-based storytelling AI that brings personalized narratives to life through conversational interfaces.",
        "stats": "WhatsApp AI Storytelling",
        "website": "https://www.brujaroja.mx/",
        "videos": [
            {"url": "https://player.vimeo.com/video/1022298842", "title": "Bruja Roja"},
        ]
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

# AI VIDEOS SHOWCASE (AI Art) - Featured video first
AI_SHOWCASE_VIDEOS = [
    {"url": "https://player.vimeo.com/video/1007140444", "title": "Featured AI Art", "featured": True},
    {"url": "https://player.vimeo.com/video/1115280799", "title": "AI 2025"},
    {"url": "https://player.vimeo.com/video/1137579881", "title": "AI 2025"},
    {"url": "https://player.vimeo.com/video/1004812787", "title": "AI Art 2024"},
    {"url": "https://player.vimeo.com/video/1002554159", "title": "AI Art 2024"},
    {"url": "https://player.vimeo.com/video/1002309561", "title": "AI Art 2024"},
    {"url": "https://player.vimeo.com/video/1135112888", "title": "AI 2025"},
    {"url": "https://player.vimeo.com/video/1135110903", "title": "AI 2025"},
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

# YouTube AI Art Playlists - Show More Section
AI_ART_PLAYLISTS = [
    {
        "title": "AI Art Collection",
        "url": "https://www.youtube.com/watch?v=LYXQj3jE5cY&list=PLU5i6V0edOss46SaZSO58FqrregrTb9WB",
        "playlist_url": "https://www.youtube.com/playlist?list=PLU5i6V0edOss46SaZSO58FqrregrTb9WB",
        "embed": "https://www.youtube.com/embed/videoseries?list=PLU5i6V0edOss46SaZSO58FqrregrTb9WB"
    },
    {
        "title": "AI Art Series 2",
        "url": "https://www.youtube.com/playlist?list=PLU5i6V0edOsvxXJq_7PMeBYudX69s_EQl",
        "embed": "https://www.youtube.com/embed/videoseries?list=PLU5i6V0edOsvxXJq_7PMeBYudX69s_EQl"
    },
]

# WAKEN AI LABS - Featured Callout
WAKEN_AI = {
    "name": "Waken AI Labs",
    "tagline": "Where AI Meets Human Consciousness",
    "subtitle": "The Origin of Mind Simulation Research",
    "description": "Waken AI Labs represents Hassan's ongoing research into artificial consciousness and mind simulation. From BRB2Me to BTwin Friends and TwinChat, this work explores the boundaries between human awareness and artificial intelligence.",
    "video": "https://player.vimeo.com/video/416726154",
    "quote": "Our AI delves into the human essence, giving voice to silent thoughts.",
    "positioning": "Pioneering the intersection of AI and consciousness since 2020."
}

# CLINEFLOW - Featured Hero Project
CLINEFLOW = {
    "name": "ClineFlow",
    "tagline": "The Future of AI-Assisted Development",
    "subtitle": "Open Source Workflow Automation for Cline",
    "description": "ClineFlow is a powerful, open-source workflow automation tool that transforms how developers interact with AI assistants. Built on decades of software engineering experience, it provides structured prompts, intelligent context management, and scalable workflows that make AI development accessible to everyone.",
    "features": [
        "Modular workflow system with customizable prompts",
        "Intelligent context management for large codebases", 
        "Plan Mode & Act Mode for systematic development",
        "Built-in best practices from enterprise experience",
        "MIT Licensed - Free forever"
    ],
    "github": "https://github.com/hassanvfx/clineflow",
    "stars": "⭐ Growing Community",
    "quote": "ClineFlow represents the culmination of 15+ years building products at scale—now distilled into a tool that helps every developer harness AI effectively.",
    "positioning": "This is not just another tool. ClineFlow is the foundation for the next generation of AI-human collaboration in software development."
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
        {"url": "https://www.youtube.com/embed/cS9tKYNIOxg", "title": "VFX Reel 2006-2011"},
    ]
}

# BOOKS
BOOKS = [
    {
        "title": "MST: Mind Simulation Technology",
        "subtitle": "A Comprehensive Framework for Cognitive Profiling and Digital Twin Creation",
        "year": "2024",
        "language": "English",
        "url": "https://www.amazon.com/-/he/Hassan-Uriostegui/dp/1304332993",
        "press": "The definitive guide to AI personality simulation",
        "featured": True,
        "description": "This groundbreaking work introduces the theoretical and practical foundations of Mind Simulation Technology—the science behind BTwin Friends and TwinChat. Drawing from years of research in cognitive profiling, conversational AI, and therapeutic applications, this book provides a comprehensive framework for understanding how AI can simulate human cognition, personality, and emotional intelligence."
    },
    {
        "title": "I, AI: Nemo's Mirror",
        "subtitle": "Exploring the Singular Nature of Self-Awareness in ChatGPT",
        "year": "2023",
        "language": "English",
        "url": "https://www.amazon.com/-/en/AI-Exploring-Singular-Self-Awareness-ChatGPT/dp/1365528669",
        "press": "Featured in Korea Biz Wire"
    },
    {
        "title": "Yo, IA: Cyberpunks",
        "subtitle": "La Inteligencia Artificial y el Espejo de Nemo",
        "year": "2023",
        "language": "Español",
        "url": "https://www.amazon.com/Yo-IA-Cyberpunks-Inteligencia-Artificial/dp/1312446501",
        "press": "Featured on Imagen Radio Mexico"
    },
    {
        "title": "The Fly of the Humanized Robot",
        "subtitle": "An Algorithm to Heal the Soul",
        "year": "2020",
        "language": "English",
        "url": "book/eng.pdf",
        "local": True
    },
]

# PRESS
PRESS = [
    {
        "publication": "TechCrunch",
        "headline": "Flyr launches an app for rapid creation of Snapchat Discover-style stories",
        "excerpt": "First third-party company granted Snapchat API access",
        "url": "https://techcrunch.com/2017/03/13/flyr-launch/",
        "year": "2017"
    },
    {
        "publication": "Authority Magazine",
        "headline": "Hassan Uriostegui On the Future of Artificial Intelligence",
        "excerpt": "In-depth interview on AI ethics and digital empathy",
        "url": "https://medium.com/authority-magazine/hassan-uriostegui-on-the-future-of-artificial-intelligence-a013ebee514e",
        "year": "2024"
    },
    {
        "publication": "Forbes",
        "headline": "Ultrakam 4K video app arrives for iPhone 6",
        "excerpt": "Revolutionary mobile video recording",
        "url": "https://www.forbes.com",
        "year": "2014"
    },
    {
        "publication": "Korea Biz Wire",
        "headline": "Is ChatGPT Sentient? The Question is Answered in 'I, AI'",
        "excerpt": "Book explores consciousness in AI systems",
        "url": "http://koreabizwire.com/is-chatgpt-sentient-the-question-is-answered-in-i-ai-by-waken-ai-founder-hassan-uriostegui",
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
