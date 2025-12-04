// Complete portfolio data with ALL content from CONTENT_MASTER.md

export const portfolioData = {
  hero: {
    name: "Hassan Uriostegui",
    title: "EB1A Extraordinary Ability | Principal Engineer",
    tagline: "Silicon Valley Innovator • AI Pioneer • Author",
    bio: "Mexican-born Silicon Valley entrepreneur, AI researcher, and author pioneering the intersection of artificial intelligence and human emotional wellness. Over a decade-long career contributing to high-profile tech ventures and authoring innovative works bridging technology and emotional health.",
    image: "https://placehold.co/600x600/0a0a0a/4A90E2?text=Hassan+Uriostegui", // Placeholder
    stats: [
      { value: "40M+", label: "Users Impacted" },
      { value: "$6M+", label: "Funding Raised" },
      { value: "10K+", label: "Products Launched" },
      { value: "10+", label: "Years Silicon Valley" },
      { value: "4", label: "Books Published" },
      { value: "1", label: "Patent" }
    ],
    links: [
      { label: "Waken.ai", url: "https://www.wakenai.com" },
      { label: "GitHub", url: "https://github.com/hassanvfx" },
      { label: "LinkedIn", url: "https://www.linkedin.com/in/bensabbah" },
      { label: "Medium", url: "https://uriostegui.medium.com" }
    ]
  },

  wakenEcosystem: {
    title: "Waken AI Ecosystem",
    subtitle: "Elevating Humanity through Ergonomic and Ethical AI",
    description: "Founded in 2023, Waken AI Labs pioneers Mind Simulation Therapy (MST), a revolutionary framework combining psychometric profiling with AI 'digital twins' for continuous empathetic support.",
    projects: [
      {
        id: "mst",
        title: "Mind Simulation Therapy",
        subtitle: "Revolutionary AI Therapy Framework",
        year: "2023",
        description: "Production-validated framework with 20,000 conversations and 200,000 messages generated. Five specialized prompts create comprehensive psychological profiles, recursively injected into every conversation turn.",
        metrics: [
          "20,000 conversations",
          "200,000 messages",
          "8 use cases deployed",
          "85% cache hit rate"
        ],
        link: "https://hassanvfx.github.io/twinchat-paper/"
      },
      {
        id: "twinchat",
        title: "TwinChat",
        year: "2023",
        description: "First implementation of Mind Simulation Therapy with production metrics proving viability of AI personality simulation for therapeutic and entertainment purposes.",
        videos: [
          { title: "Main Demo", url: "https://player.vimeo.com/video/833069637" },
          { title: "Tutorial", url: "https://player.vimeo.com/video/839937602" },
          { title: "Overview", url: "https://player.vimeo.com/video/831097799" },
          { title: "App Store", url: "https://player.vimeo.com/video/831097785" },
          { title: "Demo 1", url: "https://player.vimeo.com/video/834125073" },
          { title: "Demo 2", url: "https://player.vimeo.com/video/839063252" },
          { title: "Demo 3", url: "https://player.vimeo.com/video/837409367" }
        ],
        interviews: [
          { title: "Cyberpunks Book - David Paramo & Paul Lara", url: "https://player.vimeo.com/video/843499496" },
          { title: "Familiar AI - Fernanda & Paul Lara", url: "https://player.vimeo.com/video/843495231" }
        ]
      },
      {
        id: "btwin",
        title: "BTwin Friends",
        year: "2024",
        website: "https://btwinai.com/",
        description: "Entertainment + Wellness platform merging engaging AI interactions with therapeutic benefits, offering continuous personalized emotional care for the Gen Z generation.",
        videos: [
          { title: "Main Video", url: "https://player.vimeo.com/video/1101438413" },
          { title: "It's Not Therapy", url: "https://player.vimeo.com/video/1005370967" },
          { title: "Q&A", url: "https://player.vimeo.com/video/1003088113" },
          { title: "Famous Characters", url: "https://player.vimeo.com/video/1004812787" }
        ]
      },
      {
        id: "brb2me",
        title: "BRB2Me",
        year: "2023-2024",
        description: "Groundbreaking emotional wellness AI platform inspired by Black Mirror. AI cloning of loved ones for grief support, loneliness, and emotional wellness using GPT-4 based personality simulation.",
        quote: "Our cutting-edge AI delves into the human essence, giving voice to silent thoughts and offering comfort through dialogues that transcend the bounds of time and existence."
      },
      {
        id: "bruja-roja",
        title: "Bruja Roja",
        year: "2024",
        website: "https://www.brujaroja.mx/",
        description: "WhatsApp storytelling AI project combining narrative entertainment with AI personality simulation.",
        videos: [
          { title: "Demo 1", url: "https://player.vimeo.com/video/1022298842" },
          { title: "Demo 2", url: "https://player.vimeo.com/video/1023079085" },
          { title: "Demo 3", url: "https://player.vimeo.com/video/1023078988" },
          { title: "Demo 4", url: "https://player.vimeo.com/video/1023079032" }
        ]
      },
      {
        id: "coachtotal",
        title: "CoachTotal",
        year: "2025",
        website: "https://coachtotal.app/",
        description: "AI emotional coaching platform delivered via WhatsApp, providing 24/7 personalized support and guidance."
      },
      {
        id: "sendkarma",
        title: "SendKarma",
        year: "2025",
        website: "https://www.sendkarma.app/",
        description: "Sadhguru-inspired spiritual wellness AI platform.",
        videos: [
          { title: "Main Demo", url: "https://player.vimeo.com/video/1138631992" }
        ]
      },
      {
        id: "youchews",
        title: "YouChews",
        year: "2025",
        description: "Latest AI innovation project.",
        videos: [
          { title: "Demo 1", url: "https://player.vimeo.com/video/1136377813" },
          { title: "Demo 2", url: "https://player.vimeo.com/video/1137579881" },
          { title: "Demo 3", url: "https://player.vimeo.com/video/1115280799" },
          { title: "Demo 4", url: "https://player.vimeo.com/video/1137973511" },
          { title: "Demo 5", url: "https://player.vimeo.com/video/1137579986" }
        ]
      }
    ]
  },

  currentVentures: [
    {
      id: "jabali",
      title: "JabaliAI",
      role: "Principal Engineer",
      year: "2025",
      location: "San Francisco Bay Area",
      description: "Architecting AI-driven systems that convert text prompts into playable mobile games. Also Lead Product Designer for SimZApp.com."
    },
    {
      id: "joy-and-song",
      title: "Joy and Song",
      role: "Music Production House",
      year: "2020-Present",
      website: "https://pidetucancion.com",
      youtube: "https://www.youtube.com/@pidetucancion",
      description: "Music production house creating personalized songs and musical content.",
      videos: [
        { title: "Short 1", url: "https://www.youtube.com/embed/_lGTqk8Fyqs" },
        { title: "Short 2", url: "https://www.youtube.com/embed/LYXQj3jE5cY" },
        { title: "Demo", url: "https://player.vimeo.com/video/1120321917" }
      ]
    }
  ],

  historicCompanies: [
    {
      id: "viddy",
      title: "Viddy",
      role: "Director of Video Engineering",
      years: "2012-2013",
      highlight: "40M Users | $370-480M Valuation",
      description: "Architected cutting-edge VFX rendering engine for iOS and Android when Instagram was photo-only. Built mobile video editing features that propelled Viddy to 40 MILLION users at peak. Dubbed the 'Instagram of video' with celebrity investors. Acquired by Fullscreen in 2014.",
      videoUrl: "https://www.youtube.com/embed/avccq32KfOE",
      stats: ["40M users", "$370-480M valuation", "First social video VFX"]
    },
    {
      id: "ultrakam",
      title: "Ultrakam",
      role: "iOS Architect & Indie Founder",
      years: "2013-2014",
      highlight: "Featured at WWDC 2014 | Forbes Coverage",
      description: "Created the FIRST mobile application enabling 2K film-resolution recording on smartphones. Surpassed Apple's implementation with custom configurations. Live 2K preview featured by Apple at WWDC 2014 as outstanding design example.",
      videoUrl: "https://www.youtube.com/embed/fhgSC6TvnoM",
      stats: ["First 2K mobile recording", "WWDC 2014", "Forbes featured"]
    },
    {
      id: "flyr",
      title: "FlyrTV",
      role: "CTO & Co-founder",
      years: "2014-2018",
      highlight: "$6M Raised | Acquired by POND5",
      description: "Secured $6 million funding, assembled team of 30 professionals. Launched 10,000+ HD video templates. FIRST third-party company granted Snapchat content API access. Acquired by POND5 (Accel/Google backed) in 2018.",
      videoUrl: "https://www.youtube.com/embed/7GQm8h70PRg",
      stats: ["$6M raised", "10K+ templates", "Snapchat API first"],
      pressUrl: "https://techcrunch.com/2017/03/13/flyr-launch/"
    },
    {
      id: "community",
      title: "Community",
      role: "Principal iOS Architect",
      years: "2019-2020",
      highlight: "Backed by Madonna & Ashton Kutcher",
      description: "Built iOS app and scalable backend for celebrity mass-messaging platform. Millions of users engaging with public figures via SMS. Implemented Princeton CS Ph.D. paper in Swift.",
      videoUrl: "https://www.youtube.com/embed/ZOWuy-HhQxE",
      stats: ["Celebrity backed", "Millions of users", "Princeton CS implementation"]
    },
    {
      id: "invision",
      title: "InVision",
      role: "Lead Mobile Developer",
      years: "2018-2019",
      description: "Part of world's largest remote organization (800 employees). Contributed to Studio and Freehand products. Navigated complex Objective-C codebase, custom WebKit integrations.",
      stats: ["800 employees", "Remote-first culture"]
    },
    {
      id: "spreeai",
      title: "SpreeAI / MyDubble",
      role: "Senior iOS Architect",
      years: "2020-2023",
      description: "Led development of AR fashion platform with hyperreal avatars. Architected modular SwiftUI codebase with ARKit, Metal, SceneKit. Established CI/CD pipelines.",
      stats: ["AR fashion platform", "SwiftUI architecture"]
    }
  ],

  innovations: [
    {
      title: "Mind Simulation Therapy (MST)",
      year: "2023",
      category: "AI Research",
      description: "Revolutionary therapeutic framework using AI personality simulation. Production validated with 20,000 conversations.",
      impact: "First therapeutic framework using AI digital twins"
    },
    {
      title: "Déjà Vu Algorithm",
      year: "2011",
      category: "AI Research",
      description: "Emotional semantic search algorithm created 12+ years before modern LLMs. Evolved into personality simulation by 2022.",
      impact: "Emotional AI pioneer - decade ahead"
    },
    {
      title: "First 2K Mobile Recording",
      year: "2013",
      category: "Mobile Innovation",
      description: "Ultrakam - first app enabling film-resolution recording on smartphones. Featured at WWDC 2014.",
      impact: "Revolutionized mobile videography"
    },
    {
      title: "Live Photos Concept",
      year: "2013",
      category: "Mobile Innovation",
      description: "Onelapse - 'taking photos from videos' concept. Apple productized this 2 years later as Live Photos (2015).",
      videoUrl: "https://player.vimeo.com/video/66624830",
      impact: "Predicted Apple feature by 2 years"
    },
    {
      title: "Snap Filters",
      year: "2011",
      category: "Computer Vision",
      description: "Krommy - Face filters and real-time effects almost a decade before Snapchat popularized them.",
      videoUrl: "https://www.youtube.com/embed/d3hvzV9KgcE",
      impact: "Face filters 10 years early"
    },
    {
      title: "Maxwell Lux",
      year: "2020",
      category: "Development Tools",
      description: "First Universal Design System for SwiftUI. Presented at WWDC20 Labs, approved for Apple Silicon early access.",
      videoUrl: "https://player.vimeo.com/video/433462410",
      impact: "Bootstrap for SwiftUI"
    },
    {
      title: "Renderfarm X",
      year: "2018",
      category: "Patent",
      description: "Patent-pending video rendering platform. Revolutionary architecture reusing iOS rendering engine for scalable backend.",
      videoUrl: "https://www.youtube.com/embed/GET8ncM2C84",
      patent: "Intelligent Graphical Feature Generation for User Content"
    },
    {
      title: "Tron Legacy AR Engine",
      year: "2010",
      category: "Augmented Reality",
      description: "High-performance AR for Disney before mobile devices could handle real-time computer vision.",
      videoUrl: "https://www.youtube.com/embed/YXglHq-JJYI",
      impact: "Mobile AR years before ARKit"
    }
  ],

  books: [
    {
      title: "I, AI: Nemo's Mirror",
      subtitle: "Exploring the Singular Nature of Self-Awareness in ChatGPT",
      year: "2023",
      language: "English",
      description: "Is ChatGPT sentient? Groundbreaking exploration of AI consciousness and self-awareness, bridging technology and philosophy.",
      amazonUrl: "https://www.amazon.com/-/he/Hassan-Uriostegui/dp/1304332993",
      pressUrl: "http://koreabizwire.com/is-chatgpt-sentient-the-question-is-answered-in-i-ai-by-waken-ai-founder-hassan-uriostegui",
      cover: "https://placehold.co/400x600/1a1a1a/4A90E2?text=I,+AI:+Nemo's+Mirror"
    },
    {
      title: "I, AI: Exploring ChatGPT",
      subtitle: "The Singular Nature of Self-Awareness",
      year: "2023",
      language: "English",
      description: "Deep dive into artificial intelligence, consciousness, and what it means for an AI to be aware of itself.",
      amazonUrl: "https://www.amazon.com.mx/AI-Exploring-Singular-Self-Awareness-ChatGPT/dp/1365528669",
      cover: "https://placehold.co/400x600/1a1a1a/8B5CF6?text=I,+AI:+Exploring"
    },
    {
      title: "Yo, IA: Cyberpunks",
      subtitle: "La Inteligencia Artificial y el Espejo de Nemo",
      year: "2023",
      language: "Español",
      description: "Spanish edition exploring AI consciousness and implications for humanity's future.",
      amazonUrl: "https://www.amazon.com/Yo-IA-Cyberpunks-Inteligencia-Artificial/dp/1312446501",
      mediaUrl: "https://www.imagenradio.com.mx/david-paramo/yo-inteligencia-artificial-cyberpuks-2023",
      cover: "https://placehold.co/400x600/1a1a1a/06B6D4?text=Yo,+IA:+Cyberpunks"
    },
    {
      title: "The Fly of the Humanized Robot",
      subtitle: "An Algorithm to Heal the Soul",
      year: "2020",
      language: "English",
      description: "Interactive book/app in Instagram Stories format. AI-guided introspective journey reimagining social media to enhance humanity's values.",
      cover: "https://placehold.co/400x600/1a1a1a/4A90E2?text=Humanized+Robot"
    }
  ],

  press: [
    {
      publication: "TechCrunch",
      title: "Flyr launches an app for rapid creation of Snapchat Discover-style stories",
      url: "https://techcrunch.com/2017/03/13/flyr-launch/",
      date: "March 2017",
      type: "Feature",
      logo: "https://placehold.co/200x60/000000/00D400?text=TechCrunch"
    },
    {
      publication: "Forbes",
      title: "Ultrakam 4K video app arrives for iPhone 6",
      date: "2014",
      type: "Review",
      logo: "https://placehold.co/200x60/000000/FFFFFF?text=FORBES"
    },
    {
      publication: "Authority Magazine",
      title: "Hassan Uriostegui On the Future of Artificial Intelligence",
      url: "https://medium.com/authority-magazine/hassan-uriostegui-on-the-future-of-artificial-intelligence-a013ebee514e",
      date: "August 2024",
      type: "Interview",
      logo: "https://placehold.co/200x60/000000/4A90E2?text=Authority+Magazine"
    },
    {
      publication: "Korea Biz Wire",
      title: "Is ChatGPT Sentient? The Question is Answered in 'I, AI'",
      url: "http://koreabizwire.com/is-chatgpt-sentient-the-question-is-answered-in-i-ai-by-waken-ai-founder-hassan-uriostegui",
      date: "2023",
      type: "Feature"
    },
    {
      publication: "Imagen Radio (Mexico)",
      title: "Yo, Inteligencia Artificial: Cyberpunks 2023",
      url: "https://www.imagenradio.com.mx/david-paramo/yo-inteligencia-artificial-cyberpuks-2023",
      date: "2023",
      type: "Radio Interview"
    },
    {
      publication: "Excelsior",
      title: "Inteligencia artificial: ¿amenaza o solución?",
      url: "https://www.excelsior.com.mx/expresiones/inteligencia-artificial-amenaza-o-solucion/1597982",
      date: "2023",
      type: "Opinion"
    }
  ],

  recognition: [
    {
      title: "EB1A Extraordinary Ability",
      year: "2020",
      description: "U.S. Permanent Residency via prestigious EB1A program recognizing extraordinary career in computer sciences. Only granted to those at the very top of their field.",
      icon: "🏆"
    },
    {
      title: "Apple WWDC 2014",
      year: "2014",
      description: "Ultrakam's live 2K preview featured as example of outstanding design",
      icon: "🍎"
    },
    {
      title: "Visual Effects Society",
      year: "2010-Present",
      description: "Active member of Hollywood VES, recognizing film industry contributions",
      icon: "🎬"
    },
    {
      title: "Patent Holder",
      year: "2018",
      description: "Intelligent Graphical Feature Generation for User Content",
      icon: "💡"
    },
    {
      title: "Snapchat API Pioneer",
      year: "2017",
      description: "FlyrTV - first third-party company granted access to Snapchat content API",
      icon: "⚡"
    },
    {
      title: "Ariel Awards",
      year: "2006-2010",
      description: "Winner for film visual effects in early career",
      icon: "🏅"
    }
  ],

  quote: {
    text: "Intelligence might be appreciated as the most primitive form of life. As such, the Universe won't be just a pathway full of intelligent life, but an absolute reflection of human awareness.",
    author: "Hassan Uriostegui"
  },

  contact: {
    email: "hassan.uriostegui@gmail.com",
    linkedin: "https://www.linkedin.com/in/bensabbah",
    github: "https://github.com/hassanvfx",
    medium: "https://uriostegui.medium.com",
    chatgpt: "https://chatgpt.com/g/g-encZOxBLw-uriosteguigpt"
  }
};
