#!/usr/bin/env python3
"""
Portfolio Generator v3 - Impact First Structure
"""

import os
import sys
import json
from html import escape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from portfolio_data import (
    IDENTITY, PROFESSIONAL_PROFILE, STATS, NAV_ITEMS, SUBMENU_ITEMS, SOCIAL_LINKS, CURRENT_PROJECTS,
    HISTORIC_COMPANIES, BOOKS, PRESS, PRESS_LOGOS, RECOGNITION, FILMOGRAPHY,
    INNOVATIONS,
    BIO, SECTION_QUOTES, CLINEFLOW, MEME_ARCADE, INTERVIEWS, WAKEN_AI, TWINCHAT_PAPER,
    CITATIONS, FEATURED_BOOKS, WWDC14_FEATURE, SWIFT_FOUNDATIONS
)
from templates.css import CSS_STYLES, COMPONENT_STYLES, SIGNAL_STYLES
from templates.scripts import INTERACTION_SCRIPT, RESUME_SCRIPT
from templates.icons import sparks_icon
from technical_writing import TECHNICAL_WRITING
from content_catalog import (
    ARTICLE_CATALOG, BOOK_CATALOG, GITHUB_FEATURED, GITHUB_REPOSITORIES, GITHUB_REPOSITORY_SNAPSHOT, NAVIGATION,
    MOBILE_APP_ICON_WALL, PAGE_COMPOSITIONS, PRESS_RELEASES, PROJECTS, PROJECT_CASES, PROJECT_CASES_BY_PAGE, SITE_PAGES,
    STARTUP_CASES, STARTUP_SOURCES, STARTUP_HERO_HIGHLIGHTS,
)

SELECTED_WORK_PAGE = "selected-work.html"
PROFILE_PAGE = "profile.html"
SITE_URL = "https://hassanvfx.github.io/website"
SITE_DESCRIPTION = "Hassan Uriostegui is an AI-native principal engineer and founder building agentic AI, durable context systems, mobile products, and ClineFlow."
SITE_LAST_MODIFIED = "2026-09-07"
SELECTED_WORK_SECTION_IDS = {"selected-work", "impact", "work", "ios-open-source", "technical-writing", "waken", "twinchat-paper", "research", "filmography", "casual-books"}
PROFILE_SECTION_IDS = {"press", "interviews"}
HOME_CHAPTERS = {
    "clineflow": ("Agentic AI", "work", "Durable context and tools for building agentic AI systems."),
    "memearcade": ("Mobile Apps", "ios-open-source", "Native experiences, playful products, and the engineering behind them."),
    "books": ("Books", "casual-books", "Practical guides to AI systems, persistent context, and mobile architecture."),
}
AI_SPARK_ITEMS = [
    ("Agentic & Open Source", "work"),
    ("AI Context Engineering", "clineflow"),
    ("Prompt Engineering", "twinchat-paper"),
]
OTHER_SPARK_ITEMS = [
    ("iOS & Open Source", "ios-open-source"),
    ("Impact & Exits", "impact"),
    ("Technical Writing", "technical-writing"),
]
HOBBY_SPARK_ITEMS = [
    ("Films & VFX", "filmography"),
    ("Writing About Trends", "casual-books"),
]
SELECTED_WORK_ITEMS = AI_SPARK_ITEMS + OTHER_SPARK_ITEMS + HOBBY_SPARK_ITEMS
IMAGE_MANIFEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image_manifest.json")


def load_image_manifest():
    """Load the generated-image URLs that are safe to render on the site."""
    with open(IMAGE_MANIFEST_PATH, encoding="utf-8") as manifest_file:
        return json.load(manifest_file)


IMAGE_MANIFEST = load_image_manifest()
with open(os.path.join(os.path.dirname(__file__), "video_metadata.json"), encoding="utf-8") as video_file:
    VIDEO_METADATA = json.load(video_file)


def generate_video_frame(url, title, square_preview=False):
    """Reserve each player's provider-declared aspect ratio before network loading."""
    video = VIDEO_METADATA[url]
    width, height = int(video['width']), int(video['height'])
    if width <= 0 or height <= 0:
        raise ValueError(f"Invalid video dimensions: {url}")
    preview_class = " video-frame--square-preview" if square_preview else ""
    return (f'<div class="video-frame{preview_class}" style="--video-ratio: {width} / {height}">'
            f'<iframe src="{escape(url, quote=True)}" title="{escape(title, quote=True)}" '
            f'width="{width}" height="{height}" loading="lazy" '
            'allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div>')


def image_attributes(key, loading=None, fetchpriority=None, sizes=None):
    """Return safe intrinsic image attributes for a manifest-backed asset."""
    try:
        asset = IMAGE_MANIFEST[key]
    except KeyError as error:
        raise ValueError(f"Unknown image manifest key: {key}") from error
    attributes = [
        f'src="{asset["url"]}"',
        f'width="{asset["width"]}"',
        f'height="{asset["height"]}"',
        'decoding="async"',
    ]
    small = IMAGE_MANIFEST.get(f"{key}-small")
    if small:
        sizes = sizes or {
            "portrait": "(max-width: 800px) 250px, 360px",
            "clineflow-hero": "(max-width: 800px) calc(100vw - 56px), 580px",
            "bio-profile": "(max-width: 800px) calc(100vw - 48px), 900px",
            "resume-preview": "(max-width: 800px) calc(100vw - 80px), 620px",
        }.get(key)
        if not sizes:
            raise ValueError(f"Responsive image requires sizes: {key}")
        attributes.extend([
            f'srcset="{small["url"]} {small["width"]}w, {asset["url"]} {asset["width"]}w"',
            f'sizes="{sizes}"',
        ])
    if loading:
        attributes.append(f'loading="{loading}"')
    if fetchpriority:
        attributes.append(f'fetchpriority="{fetchpriority}"')
    return " ".join(attributes)


def get_page_metadata(page):
    """Return SEO metadata for a generated page."""
    if page in SITE_PAGES:
        return SITE_PAGES[page]
    if page == "selected-work":
        return {
            "title": "AI Projects, iOS Open Source & Technical Writing | Hassan Uriostegui",
            "description": "Agentic AI, context engineering, prompt systems, iOS open-source tools, startup impact, technical writing, and visual effects by Hassan Uriostegui.",
            "path": SELECTED_WORK_PAGE,
            "schema_type": "CollectionPage",
            "robots": "noindex, follow",
        }
    if page == "profile":
        return {
            "title": "Resume, Press & Interviews | Hassan Uriostegui",
            "description": "Resume, press coverage, and interviews for Hassan Uriostegui, AI-native principal engineer and founder building agentic AI and mobile products.",
            "path": PROFILE_PAGE,
            "schema_type": "ProfilePage",
        }
    return {
        "title": "Hassan Uriostegui | Agentic AI, Mobile Products & ClineFlow",
        "description": SITE_DESCRIPTION,
        "path": "",
        "schema_type": "ProfilePage",
    }


def metadata_image(metadata):
    """Resolve a route's social and structured-data image from the route registry."""
    return IMAGE_MANIFEST[metadata.get("image", IDENTITY["portrait"])]


def metadata_robots(metadata):
    if "robots" in metadata:
        return metadata["robots"]
    return ("index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
            if metadata.get("indexable", True) else "noindex, follow")


def generate_page_item_list(page, canonical_url):
    """Expose each catalog route as an ItemList without duplicating its facts."""
    compositions = {
        "agentic-ai": PAGE_COMPOSITIONS["agentic-ai"]["projects"],
        "mobile-apps": PAGE_COMPOSITIONS["mobile-apps"]["projects"],
        "github": GITHUB_REPOSITORIES,
        "startups": (*PAGE_COMPOSITIONS["startups"]["exits"], *PAGE_COMPOSITIONS["startups"]["companies"], PAGE_COMPOSITIONS["startups"]["lab"]),
        "books": (*PAGE_COMPOSITIONS["books"]["technical"], *PAGE_COMPOSITIONS["books"]["earlier"]),
    }
    item_ids = compositions.get(page)
    if not item_ids:
        return None

    def name_for(item_id):
        if page == "github":
            return item_id
        if item_id == "waken":
            return WAKEN_AI["name"]
        if item_id in BOOK_CATALOG:
            return BOOK_CATALOG[item_id]["title"]
        return entity_name(PROJECTS[item_id])

    return {
        "@type": "ItemList",
        "@id": f"{canonical_url}#catalog",
        "name": "Portfolio catalog",
        "itemListOrder": "https://schema.org/ItemListOrderAscending",
        "numberOfItems": len(item_ids),
        "itemListElement": [
            {"@type": "ListItem", "position": position, "name": name_for(item_id)}
            for position, item_id in enumerate(item_ids, start=1)
        ],
    }


def generate_structured_data(page, metadata):
    """Generate a search-engine-readable author and site graph."""
    canonical_url = f'{SITE_URL}/{metadata["path"]}'
    author_id = f"{SITE_URL}/#hassan-uriostegui"
    clineflow_id = "https://clineflow.com/#software"
    foundation_nodes = [
        {
            "@type": "SoftwareSourceCode",
            "@id": f'{project["website"]}#source',
            "name": project["title"],
            "description": project["description"],
            "codeRepository": project["website"],
            "programmingLanguage": "Swift",
            "author": {"@id": author_id},
            "isAccessibleForFree": True,
        }
        for project in SWIFT_FOUNDATIONS
    ] if page == "selected-work" else []
    article_nodes = [
        {
            "@type": "Article",
            "@id": article["url"],
            "url": article["url"],
            "headline": article["title"],
            "description": article["description"],
            "datePublished": article["date"],
            "author": {"@id": author_id},
        }
        for article in TECHNICAL_WRITING
    ] if page == "selected-work" else []
    about = [{"@id": author_id}, {"@id": clineflow_id}]
    about.extend({"@id": node["@id"]} for node in foundation_nodes)
    page_image = metadata_image(metadata)
    page_item_list = generate_page_item_list(page, canonical_url)
    main_entity = ({"@id": author_id} if metadata["schema_type"] == "ProfilePage"
                   else {"@id": page_item_list["@id"]} if page_item_list else {"@id": author_id})
    breadcrumb = {
        "@type": "BreadcrumbList",
        "@id": f"{canonical_url}#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
            *([] if metadata["path"] == "" else [{"@type": "ListItem", "position": 2, "name": metadata["title"].rsplit(" | ", 1)[0], "item": canonical_url}]),
        ],
    }
    structured_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": f"{SITE_URL}/#website",
                "url": f"{SITE_URL}/",
                "name": IDENTITY["name"],
                "description": SITE_DESCRIPTION,
                "inLanguage": "en-US",
            },
            {
                "@type": "Person",
                "@id": author_id,
                "name": IDENTITY["name"],
                "url": f"{SITE_URL}/",
                "image": f'{SITE_URL}/{IMAGE_MANIFEST[IDENTITY["portrait"]]["url"]}',
                "jobTitle": "AI-Native Principal Engineer and Founder",
                "sameAs": [link["url"] for link in SOCIAL_LINKS],
                "knowsAbout": ["Agentic AI", "Context Engineering", "Prompt Engineering", "Mobile Product Development", "ClineFlow"],
            },
            {
                "@type": "SoftwareApplication",
                "@id": clineflow_id,
                "name": "ClineFlow",
                "url": CLINEFLOW["website"],
                "applicationCategory": "DeveloperApplication",
                "operatingSystem": "Any",
            },
            {
                "@type": metadata["schema_type"],
                "@id": canonical_url,
                "url": canonical_url,
                "name": metadata["title"],
                "description": metadata["description"],
                "inLanguage": "en-US",
                "dateModified": SITE_LAST_MODIFIED,
                "author": {"@id": author_id},
                "mainEntity": main_entity,
                "about": about,
                "primaryImageOfPage": {
                    "@type": "ImageObject",
                    "url": f'{SITE_URL}/{page_image["url"]}',
                    "width": page_image["width"],
                    "height": page_image["height"],
                },
                "isPartOf": {"@id": f"{SITE_URL}/#website"},
            },
        ] + foundation_nodes + article_nodes + ([page_item_list] if page_item_list else []) + [breadcrumb],
    }
    return json.dumps(structured_data, ensure_ascii=False, separators=(",", ":"))


def generate_robots_txt():
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


def generate_sitemap_xml():
    """Expose every canonical generated page with current publishing metadata."""
    pages = tuple((metadata["path"], metadata["priority"], metadata["changefreq"])
                  for _, metadata in SITE_PAGES.items() if metadata.get("indexable", True))
    urls = "\n".join(
        f"  <url><loc>{SITE_URL}/{path}</loc><lastmod>{SITE_LAST_MODIFIED}</lastmod><changefreq>{frequency}</changefreq><priority>{priority}</priority></url>"
        for path, priority, frequency in pages
    )
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
'''


def resolve_navigation_href(href, page):
    """Resolve an in-site anchor against the page where navigation is rendered."""
    if not href.startswith("#"):
        return href

    section_id = href[1:]
    if section_id in SELECTED_WORK_SECTION_IDS:
        return href if page == "selected-work" else f"{SELECTED_WORK_PAGE}{href}"
    if section_id in PROFILE_SECTION_IDS:
        return href if page == "profile" else f"{PROFILE_PAGE}{href}"
    if section_id == "contact":
        return href
    return href if page == "home" else f"index.html{href}"


def page_href(page):
    """Return a stable relative URL for a canonical generated page."""
    return "index.html" if page == "home" else SITE_PAGES[page]["path"]


def generate_nav_html(page):
    """Generate navigation with ClineFlow featured"""
    items = []
    for nav in NAV_ITEMS:
        featured_class = ' class="featured"' if nav.get("featured") else ''
        target = ' target="_blank"' if nav.get("external") else ''
        href = resolve_navigation_href(nav["href"], page)
        items.append(f'<a href="{href}"{featured_class}{target}>{nav["label"]}</a>')
    return "\n      ".join(items)


def generate_submenu_html(page):
    """Generate submenu navigation"""
    items = []
    for item in SUBMENU_ITEMS:
        href = resolve_navigation_href(item["href"], page)
        items.append(f'<a href="{href}" class="submenu-link">{item["label"]}</a>')
    return "\n      ".join(items)


def generate_mobile_nav_html(page):
    """Generate the complete compact navigation menu for mobile."""
    items = []
    for nav in NAV_ITEMS + SUBMENU_ITEMS:
        featured_class = ' class="featured"' if nav.get("featured") else ''
        target = ' target="_blank"' if nav.get("external") else ''
        href = resolve_navigation_href(nav["href"], page)
        chapter = HOME_CHAPTERS.get(nav["href"].removeprefix('#'))
        label = chapter[0].upper() if chapter else nav['label']
        items.append(f'<a href="{href}"{featured_class}{target}>{escape(label)}</a>')
    return "\n    ".join(items)


def generate_stats_html():
    """Generate stats row HTML"""
    items = []
    for stat in STATS:
        items.append(f'''<div class="stat-item">
          <div class="value">{stat["value"]}</div>
          <div class="label">{stat["label"]}</div>
        </div>''')
    return "\n        ".join(items)


def generate_footer_bio_html():
    """Generate the footer biography from the central identity data."""
    return "\n    ".join(
        f'<p style="max-width: 700px; margin: 1.5rem auto; font-size: 1.05rem; line-height: 1.7; color: rgba(255,255,255,0.7);">{paragraph}</p>'
        for paragraph in IDENTITY["footer_bio"]
    )


def generate_section_nav(label="", label_class="eyebrow"):
    """A local return path, paired with the chapter's existing eyebrow."""
    eyebrow = f'<span class="{label_class}">{escape(label)}</span>' if label else ''
    return (f'<div class="section-wayfinding">{eyebrow}'
            '<a class="sparks-return" href="index.html#explore-work" aria-label="Back to the work overview">'
            '<span class="sparks-return-arrow" aria-hidden="true">←</span><span>Explore My Work</span></a></div>')


def generate_home_chapter_heading(section_id):
    """Keep homepage chapter headings and their menu labels in sync."""
    title, icon, description = HOME_CHAPTERS[section_id]
    return f'''<header class="home-chapter-heading">
      <div class="home-chapter-title">
        <span class="home-chapter-icon">{sparks_icon(icon)}</span>
        <h2 id="{section_id}-chapter-title">{escape(title)}</h2>
      </div>
      <p>{escape(description)}</p>
      {generate_section_nav()}
    </header>'''


def generate_selected_work_grid(page="home"):
    """A canonical topic directory, rendered wherever overview navigation helps."""
    icons = {
        "agentic-ai": "work", "mobile-apps": "ios-open-source", "github": "twinchat-paper",
        "startups": "impact", "books": "casual-books", "profile": "technical-writing",
    }
    descriptions = {
        "agentic-ai": "Context, prompts, and agentic systems", "mobile-apps": "Native products and iOS engineering",
        "github": "Public repositories and developer tools", "startups": "Product impact, exits, and Waken AI",
        "books": "Books, research, and technical writing", "profile": "Resume, evidence, press, and interviews",
    }
    links = "\n        ".join(
        f'<a href="{page_href(target)}" class="selected-work-link selected-work-link--{target}">{sparks_icon(icons[target])}<span class="sparks-label">{escape(label)}</span><span class="selected-work-description">{escape(descriptions[target])}</span><span class="sparks-arrow" aria-hidden="true">→</span></a>'
        for label, target in NAVIGATION
    )
    return f'''
  <section class="selected-work-gateway" id="explore-work" tabindex="-1" aria-labelledby="selected-work-title">
    <div class="selected-work-gateway-inner">
      <span class="eyebrow">Portfolio directory</span>
      <h2 id="selected-work-title">Explore My Work</h2>
      <p class="selected-work-intro">Choose an editorial view of the projects, products, repositories, writing, and evidence behind the work.</p>
      <div class="selected-work-grid selected-work-grid--directory">
        {links}
      </div>
    </div>
  </section>
'''


def generate_clineflow_section(include_chapter=True):
    """Generate the focused ClineFlow installer callout."""
    return f'''
  <!-- ClineFlow Agentic Installer -->
  <section class="clineflow-callout clineflow-installer" id="clineflow" aria-labelledby="{'clineflow-chapter-title' if include_chapter else 'clineflow-feature-title'}">
    {generate_home_chapter_heading('clineflow') if include_chapter else ''}
    <div class="clineflow-installer-shell">
      <figure class="clineflow-hero clineflow-installer-hero">
        <img {image_attributes("clineflow-hero", loading="lazy")} alt="Persistent Context, Open Knowledge — ClineFlow durable memory for agentic AI" />
      </figure>
      <div class="clineflow-installer-inner">
        <a href="{CLINEFLOW["website"]}" target="_blank" rel="noopener noreferrer" class="clineflow-wordmark">Creator of {CLINEFLOW["name"]}</a>
        <h3 id="clineflow-feature-title"><span>Infinite AI Memory</span> across chats, agents and collaborators.</h3>
        <div class="clineflow-explainer">
          <p>{CLINEFLOW['description']}</p>
          <p>A filesystem-native knowledge layer that travels with the repository, evolves through version control, and stays usable across agents and collaborators.</p>
        </div>
        <div class="clineflow-installer-panel">
          <p>Run this in your project folder with your preferred agentic AI tool</p>
          <div class="clineflow-prompt-wrap">
            <code id="clineflow-installer-prompt">{CLINEFLOW["installer_prompt"]}</code>
            <button type="button" class="clineflow-copy-button" data-copy-prompt="clineflow-installer-prompt">Copy prompt</button><span class="copy-status" role="status" aria-live="polite"></span>
          </div>
        </div>
      </div>
      <div class="clineflow-support">
        <figure class="clineflow-agent-compatibility">
          <img {image_attributes("clineflow-agent-compatibility", loading="lazy")} alt="ClineFlow compatibility with major agentic AI tools" />
          <figcaption>Works across major agentic AI tools.</figcaption>
        </figure>
        <div class="clineflow-masterclass">
          <p>Explore ClineFlow:</p>
          <div class="clineflow-masterclass-divider" aria-hidden="true"></div>
          <a href="{CLINEFLOW["website"]}" target="_blank" rel="noopener noreferrer" class="clineflow-masterclass-cta">Explore ClineFlow <span aria-hidden="true">↗</span></a>
        </div>
      </div>
    </div>
  </section>
'''


def generate_professional_profile(heading_tag="h2"):
    """Generate the embedded PDF.js professional profile viewer."""
    return f'''
  <section class="professional-profile" id="professional-profile">
    <div class="professional-profile-inner">
      <div class="professional-profile-copy">
        <span class="professional-profile-eyebrow">{PROFESSIONAL_PROFILE["eyebrow"]}</span>
        <{heading_tag}>{PROFESSIONAL_PROFILE["title"]}</{heading_tag}>
        <p>{PROFESSIONAL_PROFILE["summary"]}</p>
        <div class="professional-profile-actions">
          <a href="{PROFESSIONAL_PROFILE["pdf"]}" download class="professional-profile-download">{PROFESSIONAL_PROFILE["download_label"]}</a>
          <a href="{PROFESSIONAL_PROFILE["pdf"]}" target="_blank" rel="noopener noreferrer" class="professional-profile-open">{PROFESSIONAL_PROFILE["open_label"]} →</a>
        </div>
      </div>
      <div class="professional-profile-viewer" aria-label="Embedded professional profile PDF viewer">
        <div class="professional-profile-toolbar">
          <span id="resumeStatus" class="professional-profile-status" aria-live="polite">Resume preview — loading full viewer…</span>
          <div class="professional-profile-controls" aria-label="Resume viewer controls">
            <button type="button" id="resumePrevious" aria-label="Previous resume page" disabled>←</button>
            <span id="resumePageIndicator" aria-live="polite">1 / 2</span>
            <button type="button" id="resumeNext" aria-label="Next resume page" disabled>→</button>
            <button type="button" id="resumeZoomOut" aria-label="Zoom out" disabled>−</button>
            <button type="button" id="resumeZoomIn" aria-label="Zoom in" disabled>+</button>
          </div>
        </div>
        <div id="resumeCanvasWrap" class="professional-profile-canvas-wrap">
          <div class="professional-profile-page-frame">
            <img id="resumePreview" {image_attributes(PROFESSIONAL_PROFILE["preview"], loading="lazy")} alt="{PROFESSIONAL_PROFILE["preview_alt"]}" class="professional-profile-preview" />
            <canvas id="resumeCanvas" aria-label="Professional profile PDF page" hidden></canvas>
          </div>
        </div>
        <p class="professional-profile-fallback">Preview shown above. For the full two-page resume, <a href="{PROFESSIONAL_PROFILE["pdf"]}" target="_blank" rel="noopener noreferrer">open the PDF</a>.</p>
      </div>
    </div>
  </section>
'''


def generate_impact_card(company):
    """Generate impact/company card with press quote"""
    press_quote_html = ""
    if company.get("press_quote"):
        pq = company["press_quote"]
        press_quote_html = f'''
      <div class="company-press-quote">
        <p class="quote-text">"{pq["quote"]}"</p>
        <p class="quote-source">— <strong>{pq["source"]}</strong> {pq["source_title"]}</p>
      </div>'''
    exit_html = '<span class="impact-exit">Exit</span>' if company.get("exit") else ""
    article_links_html = ""
    if company.get("article_links"):
        article_links_html = f'''<div class="impact-coverage" aria-label="{company["name"]} coverage">
        {"".join(f'<a href="{article["url"]}" target="_blank" rel="noopener noreferrer">{article["label"]} <span aria-hidden="true">↗</span></a>' for article in company["article_links"])}
      </div>'''
    
    return f'''
  <article class="impact-card" id="{company["id"]}">
    <div class="card-video">
      {generate_video_frame(company["video"], company["name"])}
    </div>
    <div class="card-content">
      <div class="impact-labels"><span class="highlight">{company["highlight"]}</span>{exit_html}</div>
      <h3>{company["name"]}</h3>
      <p class="role">{company["role"]} • {company["year"]}</p>
      <p class="description">{company["description"]}</p>
      {press_quote_html}
      {article_links_html}
    </div>
  </article>
'''


def generate_wwdc14_feature():
    """Generate the Apple WWDC14 Ultrakam recognition feature."""
    return f'''
  <section class="wwdc14-feature" id="wwdc14">
    <div class="wwdc14-inner">
      <div class="wwdc14-copy">
        {generate_section_nav(WWDC14_FEATURE["eyebrow"], "wwdc14-eyebrow")}
        <h2>{WWDC14_FEATURE["title"]}</h2>
        <p class="wwdc14-subtitle">{WWDC14_FEATURE["subtitle"]}</p>
        <p class="wwdc14-description">{WWDC14_FEATURE["description"]}</p>
        <div class="wwdc14-actions">
          <a href="{WWDC14_FEATURE["pdf_url"]}" target="_blank" rel="noopener noreferrer" class="wwdc14-btn wwdc14-btn-primary">View WWDC14 slide <span aria-hidden="true">↗</span></a>
          <a href="{WWDC14_FEATURE["medium_url"]}" target="_blank" rel="noopener noreferrer" class="wwdc14-text-link">Read the story <span aria-hidden="true">→</span></a>
        </div>
      </div>
      <div class="wwdc14-visuals">
        <a href="{WWDC14_FEATURE["pdf_url"]}" target="_blank" rel="noopener noreferrer" class="wwdc14-slide-link">
          <img {image_attributes(WWDC14_FEATURE["slide_image"], loading="lazy")} alt="{WWDC14_FEATURE["slide_alt"]}" class="wwdc14-slide" />
          <span>WWDC14 Session 709, slide 6</span>
        </a>
        <div class="wwdc14-icon-proof">
          <img {image_attributes(WWDC14_FEATURE["icon_image"], loading="lazy")} alt="{WWDC14_FEATURE["icon_alt"]}" />
          <p>Ultrakam Remote Control<br /><strong>blue clapperboard icon</strong></p>
        </div>
      </div>
    </div>
  </section>
'''


def generate_ios_open_source_callout():
    """Connect the homepage mobile work to the dedicated Mobile Apps page."""
    return f'''
  <section class="ios-sparks-callout" aria-labelledby="ios-sparks-heading">
    <div class="ios-sparks-callout-inner" data-sparks-bridge="ios">
      <span class="sparks-bridge-kicker">Build native</span>
      <h2 id="ios-sparks-heading" class="sparks-callout-title"><span class="sparks-callout-icon">{sparks_icon("ios-open-source")}</span>More Mobile Apps</h2>
      <p>Explore native products, WWDC-recognized mobile work, and the Swift foundations behind immersive commerce, social video, and instant gameplay.</p>
      <a class="home-tooling-link" href="{page_href('mobile-apps')}#projects">More Mobile Apps <span aria-hidden="true">→</span></a>
      <div class="sparks-bridge-art sparks-bridge-art--ios" aria-hidden="true"><span></span><span></span><span>{sparks_icon('ios-open-source')}</span></div>
    </div>
  </section>
'''


def generate_agentic_ai_callout():
    """Connect the Agentic AI showcase to its dedicated project catalog."""
    return f'''
  <section class="ai-sparks-callout" aria-labelledby="agentic-ai-callout-heading">
    <div class="ai-sparks-callout-inner" data-sparks-bridge="ai">
      <span class="sparks-bridge-kicker">Explore intelligent systems</span>
      <h2 id="agentic-ai-callout-heading" class="sparks-callout-title"><span class="sparks-callout-icon">{sparks_icon("work")}</span>More Agentic AI</h2>
      <p>Explore durable AI context, prompt engineering, conversational systems, and creative automation—from ClineFlow to products built around persistent knowledge and repeatable workflows.</p>
      <a class="home-tooling-link" href="{page_href('agentic-ai')}#projects">More Agentic AI <span aria-hidden="true">→</span></a>
      <div class="sparks-bridge-art sparks-bridge-art--ai" aria-hidden="true"><span></span><span></span><span>{sparks_icon('work')}</span></div>
    </div>
  </section>
'''


def generate_home_research_callout(section_id="ai-copyright-weights", heading_id="ai-copyright-title", include_overview_link=True):
    """Compact citation evidence shared by Home and the Agentic AI page."""
    house = CITATIONS["house"]
    return f'''
  <section class="citation-feature" id="{escape(section_id, quote=True)}" aria-labelledby="{escape(heading_id, quote=True)}">
    <div class="citation-feature-inner">
      <div class="citations-intro">
        <span class="citations-eyebrow">{escape(CITATIONS["eyebrow"])}</span>
        <h2 id="{escape(heading_id, quote=True)}">{escape(CITATIONS["title"])}</h2>
        <p>{escape(CITATIONS["description"])}</p>
        <p class="citations-context">The article has been cited in government, legal, and academic discussions of AI, copyright, and model weights.</p>
        <div class="citation-feature-actions"><a href="{escape(CITATIONS["article_url"], quote=True)}" target="_blank" rel="noopener noreferrer" class="citations-cta">Read the original article <span aria-hidden="true">→</span></a>{f'<a href="{page_href("agentic-ai")}#articles" class="citations-cta citation-feature-overview">Explore Agentic AI <span aria-hidden="true">→</span></a>' if include_overview_link else ''}</div>
      </div>
      <a href="{escape(house["url"], quote=True)}" target="_blank" rel="noopener noreferrer" class="citations-cover-link">
        <img {image_attributes(CITATIONS["image"], loading="lazy", sizes="(max-width: 768px) min(100vw - 48px, 315px), 420px")} alt="{escape(CITATIONS["image_alt"], quote=True)}" class="citations-cover" />
        <span>Open the House report →</span>
      </a>
    </div>
  </section>
'''


def generate_technical_writing_callout():
    """Bridge published books to the longer technical articles on Sparks."""
    return f'''
  <section class="writing-sparks-callout" aria-labelledby="writing-sparks-heading">
    <div class="writing-sparks-callout-inner" data-sparks-bridge="writing">
      <span class="sparks-bridge-kicker">Read the field notes</span>
      <h2 id="writing-sparks-heading" class="sparks-callout-title"><span class="sparks-callout-icon">{sparks_icon("technical-writing")}</span>More Technical Writing</h2>
      <p>Read practical notes from building AI systems, Swift tools, and creative workflows—shared to make the decisions, trade-offs, and lessons reusable.</p>
      <a class="home-tooling-link" href="{page_href('books')}#articles">Explore Technical Writing <span aria-hidden="true">→</span></a>
      <div class="sparks-bridge-art sparks-bridge-art--writing" aria-hidden="true"><span></span><span></span><span>{sparks_icon('technical-writing')}</span></div>
    </div>
  </section>
'''


def generate_swift_foundations():
    """Generate the dedicated iOS open-source chapter for Selected Work."""
    projects = []
    for index, project in enumerate(SWIFT_FOUNDATIONS):
        highlights = "".join(f'<li>{highlight}</li>' for highlight in project["highlights"])
        reverse = " home-tooling-project--reverse" if index % 2 else ""
        projects.append(f'''
      <article class="home-tooling-project{reverse}" id="{project["id"]}">
        <div class="home-tooling-copy">
          <span class="home-tooling-eyebrow">{project["eyebrow"]}</span>
          <h3>{project["title"]}</h3>
          <p class="home-tooling-subtitle">{project["subtitle"]}</p>
          <p class="home-tooling-description">{project["description"]}</p>
          <ul class="home-tooling-highlights">{highlights}</ul>
          <a href="{project["website"]}" target="_blank" rel="noopener noreferrer" class="home-tooling-link">View on GitHub <span aria-hidden="true">↗</span></a>
        </div>
        <div class="home-tooling-visual">
          <img {image_attributes(project["image"], loading="lazy")} alt="{escape(project["image_alt"], quote=True)}" />
        </div>
      </article>''')
    return f'''
  <section class="home-tooling-showcase" id="ios-open-source" aria-labelledby="ios-open-source-title">
    <div class="home-tooling-inner">
      <div class="home-tooling-heading">
        {generate_section_nav("Selected Work")}
        <h2 id="ios-open-source-title">iOS <em>Open Source</em></h2>
        <p>Three practical Swift tools for turning an iOS idea into a maintainable package, browser surface, and durable product state.</p>
      </div>
      {"".join(projects)}
    </div>
  </section>
'''


def generate_technical_writing():
    """Render readable article rows using the existing alternating showcase layout."""
    rows = []
    for index, article in enumerate(TECHNICAL_WRITING):
        reverse = " home-tooling-project--reverse" if index % 2 else ""
        title = escape(article["title"])
        rows.append(f'''<article class="home-tooling-project writing-article{reverse}" id="{article['id']}">
        <div class="home-tooling-copy">
          <span class="home-tooling-eyebrow">{escape(article['topic'])} · <time datetime="{article['date']}">{article['date'][:4]}</time></span>
          <h3 id="{article['id']}-title"><a href="{article['url']}" target="_blank" rel="noopener noreferrer">{title}</a></h3>
          <p class="home-tooling-description">{escape(article['description'])}</p>
          <a class="home-tooling-link" href="{article['url']}" target="_blank" rel="noopener noreferrer" aria-label="{escape('Read on Medium: ' + article['title'], quote=True)}">Read on Medium <span aria-hidden="true">↗</span></a>
        </div>
        <a class="home-tooling-visual" href="{article['url']}" target="_blank" rel="noopener noreferrer" aria-labelledby="{article['id']}-title">
          <img {image_attributes(article['id'], loading="lazy")} alt="" />
        </a>
      </article>''')
    return f'''
  <section class="technical-writing" id="technical-writing" aria-labelledby="technical-writing-title">
    <div class="home-tooling-inner">
      <div class="home-tooling-heading">
        {generate_section_nav("Notes from building")}
        <h2 id="technical-writing-title">Technical <em>Writing</em></h2>
        <p>I write to share knowledge and lessons learned from building real software. These articles turn experiments in iOS architecture, AI collaboration, and creative tools into practical workflows others can learn from and build on.</p>
      </div>
      {''.join(rows)}
    </div>
  </section>
'''


def generate_citations_section():
    """Generate the AI Copyright Weights citations section."""
    additional_citations = "\n        ".join(
        f'''<a href="{citation["url"]}" target="_blank" rel="noopener noreferrer" class="citation-card">
          <span class="citation-source">{citation["source"]}</span>
          <h3>{citation["title"]}</h3>
          <span class="citation-link">View citation →</span>
        </a>'''
        for citation in CITATIONS["additional"]
    )

    house = CITATIONS["house"]
    return f'''
  <section class="citations-section" id="citations" aria-labelledby="citations-chapter-title">
    <header class="catalog-section-header"><span class="eyebrow">Evidence</span><h2 id="citations-chapter-title">Citations &amp; recognition</h2><p>Research referenced in government, legal, and academic discussions.</p></header>
    <div class="citations-inner">
      <div class="citations-intro">
        <span class="citations-eyebrow">{CITATIONS["eyebrow"]}</span>
        <h3>{CITATIONS["title"]}</h3>
        <p>{CITATIONS["description"]}</p>
        <p class="citations-context">The article has been cited in government, legal, and academic discussions of AI, copyright, and model weights.</p>
        <a href="{CITATIONS["article_url"]}" target="_blank" rel="noopener noreferrer" class="citations-cta">Read the original article →</a>
      </div>

      <a href="{CITATIONS["article_url"]}" target="_blank" rel="noopener noreferrer" class="citations-cover-link">
        <img {image_attributes(CITATIONS["image"], loading="lazy")} alt="{CITATIONS["image_alt"]}" class="citations-cover" />
        <span>Read the original article on Medium →</span>
      </a>

      <a href="{house["url"]}" target="_blank" rel="noopener noreferrer" class="citation-house-card" id="white-house">
        <span class="citation-source">Featured government citation</span>
        <h3>{house["title"]}</h3>
        <p>{house["detail"]}</p>
        <span class="citation-link">Open the House report →</span>
      </a>

      <div class="citation-grid">
        {additional_citations}
      </div>
    </div>
  </section>
'''


def generate_featured_book(book):
    """Generate a citation-adjacent editorial feature for a recent book."""
    if book.get("cta_url"):
        actions_html = f'''<div class="featured-book-actions">
          <a href="{book["cta_url"]}" target="_blank" rel="noopener noreferrer" class="featured-book-cta">{book["cta_label"]} <span aria-hidden="true">→</span></a>
        </div>'''
    else:
        actions_html = f'''<div class="featured-book-actions">
          <a href="{book["url"]}" target="_blank" rel="noopener noreferrer" class="featured-book-cta">{book.get("purchase_label", "Printed Edition")} <span aria-hidden="true">→</span></a>
          <a href="{book["ebook_url"]}" target="_blank" rel="noopener noreferrer" class="featured-book-ebook">Free Ebook <span aria-hidden="true">↗</span></a>
        </div>'''
    return f'''
  <section class="featured-book-section featured-book-section--{book["layout"]}">
    <div class="featured-book-inner">
      <div class="featured-book-copy">
        <div class="featured-book-heading">
        <span class="featured-book-eyebrow">{book["eyebrow"]}</span>
        <h2>{book["title"]}</h2>
        </div>
        <div class="featured-book-details">
        <p class="featured-book-subtitle">{book["subtitle"]}</p>
        <p class="featured-book-description">{book["description"]}</p>
        {actions_html}
        </div>
      </div>
      <a href="{book["url"]}" target="_blank" rel="noopener noreferrer" class="featured-book-cover-link">
        <img {image_attributes(book["image"], loading="lazy", sizes="(max-width: 700px) min(280px, calc(100vw - 48px)), (max-width: 900px) 320px, (max-width: 1200px) 36vw, 440px")} alt="{book["image_alt"]}" class="featured-book-cover" />
      </a>
    </div>
  </section>
'''


def generate_meme_arcade_callout(include_chapter=True):
    """Generate the featured MemeArcade app promotion."""
    screens = "\n        ".join(
        f'''<figure class="meme-arcade-screen-card" role="group" aria-roledescription="slide" aria-label="{index + 1} of {len(MEME_ARCADE['screens'])}">
          <img {image_attributes(screen["image"], loading="lazy")} alt="{screen["alt"]}" />
          <figcaption>{screen["caption"]}</figcaption>
        </figure>'''
        for index, screen in enumerate(MEME_ARCADE["screens"])
    )
    pagination = ''.join(
        f'<button type="button" class="carousel-dot" aria-label="Show app screen {index + 1}: {screen["caption"]}" aria-current="{"true" if index == 0 else "false"}" data-slide="{index}"><span aria-hidden="true"></span></button>'
        for index, screen in enumerate(MEME_ARCADE["screens"])
    )
    return f'''
  <section class="meme-arcade-callout" id="memearcade" aria-labelledby="{'memearcade-chapter-title' if include_chapter else 'memearcade-feature-title'}">
    {generate_home_chapter_heading('memearcade') if include_chapter else ''}
    <div class="meme-arcade-inner">
      <div class="meme-arcade-copy">
      <div class="meme-app-icon"><img {image_attributes(MEME_ARCADE["icon"], loading="lazy")} alt="{MEME_ARCADE["icon_alt"]}" class="meme-arcade-icon" /></div>
      <span class="meme-arcade-badge">IPHONE GAME ARCADE</span>
      <h3 id="memearcade-feature-title">{MEME_ARCADE["title"]}</h3>
      <p class="meme-arcade-description">{MEME_ARCADE["description"]}</p>
      <p class="meme-arcade-technology">{MEME_ARCADE["technology"]}</p>
      <a href="{MEME_ARCADE["url"]}" target="_blank" rel="noopener noreferrer" class="meme-arcade-cta">{MEME_ARCADE["cta"]} <span aria-hidden="true">→</span></a>
      </div>
      <div class="meme-carousel" role="region" aria-roledescription="carousel" aria-label="Meme Arcade app screens">
        <div class="carousel-controls" hidden>
          <button type="button" class="carousel-pause" aria-label="Pause slideshow">Pause</button>
          <button type="button" class="carousel-prev" aria-label="Previous app screen">←</button>
          <div class="carousel-dots">{pagination}</div>
          <button type="button" class="carousel-next" aria-label="Next app screen">→</button>
        </div>
        <div class="meme-arcade-gallery" aria-live="off">{screens}</div>
        <span class="carousel-position">1 / {len(MEME_ARCADE['screens'])}</span>
        <p class="carousel-status" role="status" aria-live="polite"></p>
      </div>
    </div>
  </section>
'''


def generate_current_project_card(project):
    """Generate current AI project card"""
    video_url = project["videos"][0]["url"] if project.get("videos") else ""
    if video_url:
        media = f'''<div class="card-video">
      {generate_video_frame(video_url, project["name"])}
    </div>'''
    elif project.get("image"):
        media = f'''<div class="card-video project-card-image-wrap">
      <img {image_attributes(project["image"], loading="lazy")} alt="{escape(project["image_alt"], quote=True)}" class="project-card-image" />
    </div>'''
    else:
        art_label = escape(project.get("art_label", project["name"])).replace("\n", "<br />")
        media = f'''<div class="card-video project-card-art" aria-hidden="true">
      <span>{art_label}</span>
    </div>'''
    link_label = escape(project.get("link_label", "Visit Website"))
    website_btn = f'<a href="{project["website"]}" target="_blank" rel="noopener noreferrer" class="btn btn-outline">{link_label}</a>' if project.get("website") else ""
    press_release_btn = (f'<a href="{project["press_release"]}" target="_blank" rel="noopener noreferrer" class="btn btn-outline">View Press Release</a>'
                         if project.get("press_release") else "")
    actions = f'<div class="project-card-actions">{website_btn}{press_release_btn}</div>' if (website_btn or press_release_btn) else ""
    quote = f'<p class="quote">"{project["quote"]}"</p>' if project.get("quote") else ""
    
    return f'''
  <article class="project-card" id="{project["id"]}">
    {media}
    <div class="card-content">
      <span class="highlight">{project["stats"]}</span>
      <h3>{project["name"]}</h3>
      <p class="year">{project["year"]}</p>
      <p class="description">{project["description"]}</p>
      {quote}
      {actions}
    </div>
  </article>
'''


def generate_innovation_card(innovation):
    """Generate innovation/research card"""
    if innovation.get("featured"):
        # ClineFlow - special featured card
        return f'''
  <article class="innovation-card featured" id="{innovation["id"]}">
    <div class="card-content">
      <span class="badge">⭐ Featured Open Source</span>
      <h3>{innovation["name"]}</h3>
      <p class="tagline">{innovation["tagline"]}</p>
      <p class="description">{innovation["description"]}</p>
      <a href="{innovation["link"]}" target="_blank" class="btn btn-primary">View on GitHub</a>
    </div>
  </article>
'''
    else:
        video_html = ""
        if innovation.get("video"):
            video_html = f'''<div class="card-video">
      {generate_video_frame(innovation["video"], innovation["name"])}
    </div>'''
        
        return f'''
  <article class="innovation-card" id="{innovation["id"]}">
    {video_html}
    <div class="card-content">
      <span class="year-badge">{innovation["year"]}</span>
      <h3>{innovation["name"]}</h3>
      <p class="tagline">{innovation["tagline"]}</p>
      <p class="description">{innovation["description"]}</p>
    </div>
  </article>
'''


def generate_filmography_section():
    """Generate filmography section with VES mention"""
    videos_html = ""
    for video in FILMOGRAPHY["videos"]:
        videos_html += f'''<div class="film-video">
        {generate_video_frame(video["url"], video["title"])}
        <p class="video-title">{video["title"]}</p>
      </div>
'''
    
    return f'''
  <section class="section filmography" id="filmography">
    <div class="section-header">
      {generate_section_nav(FILMOGRAPHY["years"])}
      <h2>Filmography & VFX</h2>
      <p class="lead">{FILMOGRAPHY["description"]}</p>
    </div>
    
    <div class="film-grid">
      {videos_html}
    </div>
    
    <div class="film-links">
      <a href="{FILMOGRAPHY["imdb"]}" target="_blank" class="btn btn-outline">View IMDB Profile</a>
      <span class="ves-badge">VES Member</span>
    </div>
  </section>
'''


def generate_books_html(books=None):
    """Generate book cards for the requested collection."""
    books = BOOKS if books is None else books
    items = []
    for book in books:
        press_html = f'<p class="press">{book["press"]}</p>' if book.get("press") else ""
        target = "" if book.get("local") else ' target="_blank"'
        cover_class = "book-cover book-cover--portrait" if book.get("portrait_cover") else "book-cover"
        image_html = (
            f'<a href="{book["url"]}"{target} rel="noopener noreferrer" class="book-cover-link" aria-label="View {book["title"]}">'
            f'<img {image_attributes(book["image"], loading="lazy", sizes="(max-width: 800px) calc(100vw - 128px), (max-width: 1320px) calc((100vw - 280px) / 2), 520px")} alt="{book["title"]}" class="{cover_class}" />'
            '</a>'
            if book.get("image") else ""
        )
        
        ebook_html = (
            f'<a href="{book["ebook_url"]}" target="_blank" rel="noopener noreferrer" class="btn btn-outline">Free Ebook ↗</a>'
            if book.get("ebook_url") else ""
        )
        primary_label = "Printed Edition" if ebook_html else "Read More"
        primary_class = "btn btn-primary" if ebook_html else "btn btn-outline"
        primary_action = f'<a href="{book["url"]}"{target} class="{primary_class}">{primary_label}</a>'
        actions_html = (
            f'<div class="book-actions">{primary_action}{ebook_html}</div>'
            if ebook_html else primary_action
        )

        items.append(f'''<article class="book-card">{image_html}
        <span class="year">{book.get("year", "2026")} • {book.get("language", "English")}</span>
        <h3>{book["title"]}</h3>
        <p class="subtitle">{book["subtitle"]}</p>
        {press_html}
        {actions_html}
      </article>''')
    
    return "\n      ".join(items)


def generate_press_html():
    """Generate press section"""
    items = []
    for article in PRESS:
        items.append(f'''<a href="{article["url"]}" target="_blank" class="press-card">
        <img {image_attributes(article["logo"], loading="lazy")} alt="{article["publication"]}" class="press-logo" />
        <span class="publication">{article["publication"]}</span>
        <h4>{article["headline"]}</h4>
        <p class="excerpt">{article["excerpt"]}</p>
      </a>''')
    return "\n      ".join(items)


def generate_social_links():
    """Generate social links"""
    items = []
    for link in SOCIAL_LINKS:
        items.append(f'<a href="{link["url"]}" target="_blank" class="btn btn-outline">{link["label"]}</a>')
    return "\n      ".join(items)


def generate_interviews_html():
    """Generate interviews section"""
    items = []
    for i in INTERVIEWS:
        items.append(f'''<div class="interview-card">
        {generate_video_frame(i["url"], i["title"])}
        <div class="interview-info">
          <h4>{i["title"]}</h4>
          <p>{i["context"]}</p>
        </div>
      </div>''')
    return "\n      ".join(items)


def entity_name(entity):
    return entity.get("name") or entity.get("title") or "Project"


def entity_url(entity):
    return entity.get("website") or entity.get("url") or entity.get("github")


def generate_mobile_icon_wall():
    """Render the career's mobile products as a compact, source-backed app wall."""
    tiles = []
    for item in MOBILE_APP_ICON_WALL:
        project_id = item["project_id"]
        name = item.get("label") or entity_name(PROJECTS[project_id])
        if item.get("image"):
            visual = f'<img {image_attributes(item["image"], loading="eager", sizes="(max-width: 480px) 160px, 140px")} alt="" />'
        else:
            visual = sparks_icon(item["icon"])
        tiles.append(f'<figure class="app-wall-item"><div class="app-wall-art">{visual}</div><figcaption>{escape(name)}</figcaption></figure>')
    return "".join(tiles)


def mobile_app_icon_asset(project_id):
    """Return the canonical app-wall asset for a mobile project, when present."""
    return next((item.get("image") for item in MOBILE_APP_ICON_WALL if item["project_id"] == project_id), None)


def generate_press_hero_loop():
    """One lightweight press image at a time, with a static first-frame fallback."""
    logos = ''.join(
        f'<img {image_attributes(item["logo"], loading="eager", sizes="(max-width: 700px) 320px, 440px")} alt="" class="press-display-image{" is-active" if index == 0 else ""}" />'
        for index, item in enumerate(PRESS_LOGOS)
    )
    return f'<div class="press-hero-loop" data-press-display>{logos}</div><p class="press-display-caption">In the press</p>'


def generate_topic_hero(eyebrow, title, description, icon="work", icon_wall=False, action=None, image=None, press_loop=False, square_image=False, hero_variant=None):
    if image:
        wall = f'<img {image_attributes(image, loading="eager", sizes="(max-width: 900px) calc(100vw - 48px), 420px")} alt="" />'
        art_class = " topic-hero-art--image" + (" topic-hero-art--square-image" if square_image else "")
    elif press_loop:
        wall = generate_press_hero_loop()
        art_class = " topic-hero-art--press-loop"
    else:
        wall = generate_mobile_icon_wall() if icon_wall else f'<span>{sparks_icon(icon)}</span>'
        art_class = " topic-hero-art--mobile-wall" if icon_wall else ""
    action_html = ""
    if action:
        action_html = f'<div class="topic-hero-actions"><a class="topic-hero-action" href="{escape(action["href"], quote=True)}" target="_blank" rel="noopener noreferrer">{escape(action["label"])} <span aria-hidden="true">↗</span></a></div>'
    variant_class = f" topic-hero--{escape(hero_variant, quote=True)}" if hero_variant else ""
    return f'''<section class="topic-hero{variant_class}" id="overview" aria-labelledby="topic-title">
      <div class="topic-hero-copy"><span class="eyebrow">{escape(eyebrow)}</span><h1 id="topic-title">{escape(title)}</h1><p>{escape(description)}</p>{action_html}</div>
      <div class="{'mobile-app-wall' if icon_wall else 'topic-hero-art' + art_class}" aria-hidden="true">{wall}</div>
    </section>'''


def generate_topic_index(items):
    return '<nav class="topic-index" aria-label="On this page">' + ''.join(
        f'<a href="#{anchor}">{escape(label)}</a>' for anchor, label in items) + '</nav>'


PROJECT_VISUALS = {
    "clineflow": "clineflow-hero",
    "meme-arcade": "meme-arcade-product-panels",
    "wwdc14": "wwdc14-slide",
    "twinchat-paper": "writing-agent-alignment",
    "swift-spm": "swift-spm-hero",
    "datastore": "datastore-hero",
    "webview-swiftui": "webview-swiftui-hero",
}

ARTICLE_VISUALS = {
    "ai-copyright-weights": "clineflow-hero",
    "writing-demystify-swiftui": "writing-modular-swift",
    "writing-datastore": "datastore-hero",
    "writing-securevault": "securevault-article",
    "writing-swiftwallet": "swiftwallet-article",
    "writing-wwdc14": "wwdc14-slide",
}


def generate_showcase_media(entity_id, entity, alt, square_video_preview=False):
    """Use existing project video first, then manifest-backed artwork."""
    videos = entity.get("videos") or ()
    video_url = videos[0].get("url") if videos else entity.get("video")
    if video_url:
        return generate_video_frame(video_url, alt, square_preview=square_video_preview)
    image_key = entity.get("image") or entity.get("slide_image") or PROJECT_VISUALS.get(entity_id)
    if not image_key:
        raise ValueError(f"A showcase visual is required for {entity_id}")
    return f'''<figure class="showcase-media"><img {image_attributes(image_key, loading="lazy", sizes="(max-width: 700px) calc(100vw - 48px), 560px")} alt="{escape(alt, quote=True)}" /><figcaption>{escape(alt)}</figcaption></figure>'''


def generate_legacy_row(row_id, title, eyebrow, description, media, actions, index=0, variant=""):
    """The deployed Swift/article row: alternating columns, media first on mobile."""
    reverse = " home-tooling-project--reverse" if index % 2 == 0 else ""
    return f'''<article class="home-tooling-project portfolio-row{reverse} {variant}" id="{escape(row_id)}">
      <div class="home-tooling-copy">
        <span class="home-tooling-eyebrow">{escape(eyebrow)}</span>
        <h3>{escape(title)}</h3>
        <p class="home-tooling-description">{escape(description)}</p>
        <div class="portfolio-row-actions">{actions}</div>
      </div>
      <div class="home-tooling-visual">{media}</div>
    </article>'''


def generate_showcase_project_card(entity_id, kind="project", index=0):
    entity = PROJECTS[entity_id]
    name = entity_name(entity)
    description = entity.get("description") or entity.get("subtitle") or entity.get("tagline") or ""
    details = entity.get("stats") or entity.get("highlight") or entity.get("role") or entity.get("eyebrow") or ""
    url = entity_url(entity)
    action = (f'<a class="home-tooling-link" href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">View project <span aria-hidden="true">↗</span></a>'
              if url else "")
    return generate_legacy_row(f"{entity_id}-{kind}", name, details, description,
                               generate_showcase_media(entity_id, entity, name), action, index)


def generate_showcase_article_card(article_id, index=0):
    article = ARTICLE_CATALOG[article_id]
    image_key = article.get("image") or ARTICLE_VISUALS.get(article_id) or article_id
    media = f'<a class="showcase-media" href="{escape(article["url"], quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="Read {escape(article["title"], quote=True)}"><img {image_attributes(image_key, loading="lazy", sizes="(max-width: 700px) calc(100vw - 48px), 560px")} alt="" /><span>{escape(article["title"])}</span></a>'
    action = f'<a class="home-tooling-link" href="{escape(article["url"], quote=True)}" target="_blank" rel="noopener noreferrer">Read article <span aria-hidden="true">↗</span></a>'
    return generate_legacy_row(article_id, article["title"], f'{article["topic"]} · {article["date"][:4]}',
                               article["description"], media, action, index, "writing-article")


def generate_catalog_section(section_id, eyebrow, title, description, cards, grid_class="catalog-grid"):
    return f'''<section class="catalog-section" id="{section_id}" aria-labelledby="{section_id}-title">
      <header class="catalog-section-header"><span class="eyebrow">{escape(eyebrow)}</span><h2 id="{section_id}-title">{escape(title)}</h2><p>{escape(description)}</p><a class="catalog-back" href="#overview">← Back to overview</a></header>
      <div class="{grid_class}">{''.join(cards)}</div>
    </section>'''


def generate_showcase_section(section_id, eyebrow, title, description, cards):
    return generate_catalog_section(section_id, eyebrow, title, description, cards, "portfolio-rows")


def generate_book_shelf(section_id, eyebrow, title, description, book_ids):
    rows = []
    for index, book_id in enumerate(book_ids):
        book = book_by_id(book_id)
        media = f'<a href="{escape(book["url"], quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="View {escape(book["title"], quote=True)}"><img {image_attributes(book["image"], loading="lazy", sizes="(max-width: 700px) calc(100vw - 48px), 480px")} alt="{escape(book.get("image_alt", book["title"]), quote=True)}" /></a>'
        url = book.get("cta_url") or book["url"]
        label = book.get("cta_label") or ("Printed Edition" if book.get("ebook_url") else "View book")
        actions = f'<a class="home-tooling-link" href="{escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">{escape(label)} <span aria-hidden="true">↗</span></a>'
        if book.get("ebook_url"):
            actions += f'<a class="home-tooling-link" href="{escape(book["ebook_url"], quote=True)}" target="_blank" rel="noopener noreferrer">Free Ebook <span aria-hidden="true">↗</span></a>'
        rows.append(generate_legacy_row(book_id, book["title"], book.get("eyebrow", str(book.get("year", "2026"))),
                    book.get("description") or book["subtitle"], media, actions, index, "portfolio-row--book"))
    return f'''<section class="catalog-section book-shelf" id="{section_id}" aria-labelledby="{section_id}-title">
      <header class="catalog-section-header"><span class="eyebrow">{escape(eyebrow)}</span><h2 id="{section_id}-title">{escape(title)}</h2><p>{escape(description)}</p><a class="catalog-back" href="#overview">← Back to overview</a></header>
      <div class="portfolio-rows">{''.join(rows)}</div>
    </section>'''


def generate_topic_project_cases(project_ids, page, include_related_publications=False):
    """A single project catalog can render as technical case studies per topic."""
    return [generate_project_case(item, index, include_related_publications, page) for index, item in enumerate(project_ids)]


def generate_agentic_page():
    composition = PAGE_COMPOSITIONS["agentic-ai"]
    return (generate_topic_hero("Agentic AI", "Agentic AI, context, and prompts", "Systems for preserving project knowledge, shaping agent behavior, and turning repeatable workflows into durable tools.", image="infinite-ai-context-cover")
            + generate_topic_index((("projects", "Projects"), ("open-source", "Open Source"), ("ai-copyright-weights-feature", "Research"), ("articles", "Articles & Books")))
            + generate_catalog_section("projects", "Selected systems", "Agentic AI projects", "Five product explorations across context, companions, and creative automation.", generate_topic_project_cases(composition["projects"], "agentic-ai", include_related_publications=True), "startup-cases project-cases")
            + generate_catalog_section("open-source", "Public source", "Open-source projects", "Repository-backed tools for context and creative automation.", [generate_repository_collection_card(item, card_id=f"{item}-source", title=("KIE CLI & MCP" if item == "kie-api-python" else entity_name(PROJECTS[item]))) for item in composition["open_source"]], "repository-deck")
            + generate_home_research_callout("ai-copyright-weights-feature", "ai-copyright-weights-feature-title", include_overview_link=False)
            + generate_showcase_section("articles", "Field notes", "Agentic articles", "Writing about prompt engineering, provenance, and durable AI context.", [generate_showcase_article_card(item, index) for index, item in enumerate(item for item in composition["articles"] if item != "ai-copyright-weights")])
            + generate_book_shelf("books", "Reading", "Agentic books", "Practical guides to durable AI context and on-device intelligence.", composition["books"]))


def generate_mobile_page():
    composition = PAGE_COMPOSITIONS["mobile-apps"]
    return (generate_topic_hero("Mobile Apps", "Pocket Magic", "Native experiences, real-time products, and iOS engineering from app architecture to WWDC recognition.", "ios-open-source", icon_wall=True, hero_variant="mobile")
            + generate_topic_index((("projects", "Projects"), ("open-source", "Open Source"), ("articles", "Articles & Books")))
            + generate_catalog_section("projects", "Selected mobile work", "Mobile app projects", "Consumer products and native product systems across video, social, AI, and games.", generate_topic_project_cases(composition["projects"], "mobile-apps"), "startup-cases project-cases")
            + generate_catalog_section("open-source", "Swift tools", "iOS open source", "Three distinct Swift projects for packages, persistence, and web surfaces.", [generate_swift_tool_card(item) for item in composition["open_source"]], "repository-deck")
            + generate_showcase_section("articles", "Technical writing", "Mobile articles", "A practical archive of SwiftUI, modular architecture, iOS persistence, security, and mobile product lessons.", [generate_showcase_article_card(item, index) for index, item in enumerate(composition["articles"])])
            + generate_book_shelf("books", "Reading", "Mobile books", "A field guide to mobile architecture and the product systems behind it.", composition["books"]))


def generate_swift_tool_card(tool_id, index=0):
    entity = next(item for item in SWIFT_FOUNDATIONS if item["id"] == tool_id)
    name = entity["website"].rstrip("/").rsplit("/", 1)[-1]
    return generate_repository_collection_card(name, card_id=tool_id, title=entity["title"],
                                                description=entity["description"], fallback_facts="Swift")


def generate_repository_collection_card(name, card_id=None, title=None, description=None, fallback_facts=""):
    repo = next((item for item in GITHUB_REPOSITORY_SNAPSHOT if item["name"] == name), None)
    facts = [fallback_facts] if fallback_facts else []
    if repo:
        facts = ["Public · archived" if repo["archived"] else "Public · active", repo["language"]]
        if repo["license"]:
            facts.append(f'{repo["license"]} license')
    description = description if description is not None else repo["description"]
    return f'''<article class="repository-card" id="{escape(card_id or f"repo-{name}")}">
      <div class="repository-visual" aria-hidden="true"><img {image_attributes("github-logo", loading="lazy")} alt="" /><code><span>git</span> clone<br />hassanvfx/{escape(name)}</code></div>
      <div class="repository-copy"><span class="repository-kicker">Repository</span><h3>{escape(title or name)}</h3><p>{escape(description)}</p><small>{escape(' · '.join(facts))}</small><a href="https://github.com/hassanvfx/{escape(name, quote=True)}" target="_blank" rel="noopener noreferrer">Open on GitHub <span aria-hidden="true">↗</span></a></div>
    </article>'''


def book_by_id(book_id):
    return BOOK_CATALOG[book_id]


def generate_github_page():
    repositories = {item["name"]: item for item in GITHUB_REPOSITORY_SNAPSHOT}

    def repository_card(name, featured=False, index=0):
        repo = repositories[name]
        status = "Public · archived" if repo["archived"] else "Public · active"
        facts = [status, repo["language"]]
        if repo["license"]:
            facts.append(f'{repo["license"]} license')
        card_id = f"repo-{name}-featured" if featured else f"repo-{name}"
        if featured:
            visual, title = {
                "clineflow": ("clineflow-hero", "ClineFlow"),
                "kie-api-python": ("kie-api-hero", "KIE CLI & MCP"),
                "ios-framework": ("swift-spm-hero", "SwiftSPM"),
                "ios-storage": ("datastore-hero", "DataStore"),
            }[name]
            media = f'<img {image_attributes(visual, loading="lazy", sizes="(max-width: 700px) calc(100vw - 48px), 560px")} alt="{escape(title, quote=True)}" />'
            action = f'<a class="home-tooling-link" href="https://github.com/hassanvfx/{escape(name, quote=True)}" target="_blank" rel="noopener noreferrer">Open on GitHub <span aria-hidden="true">↗</span></a>'
            return generate_legacy_row(card_id, title, ' · '.join(facts), repo["description"], media, action, index)
        return generate_repository_collection_card(name)

    featured = [repository_card(name, featured=True, index=index) for index, name in enumerate(GITHUB_FEATURED)]
    all_repos = [repository_card(name) for name in GITHUB_REPOSITORIES]
    return (generate_topic_hero("GitHub", "Open Source. AI-Native", "A public catalog of portfolio-linked repositories, developer tools, and product foundations.", action={"label": "Open GitHub", "href": "https://github.com/hassanvfx"}, image="github-terminal-hero")
            + generate_topic_index((("featured", "Featured"), ("repositories", "Repositories")))
            + generate_showcase_section("featured", "Selected repositories", "Featured GitHub work", "ClineFlow, KIE CLI & MCP, and reusable Swift foundations.", featured)
            + generate_catalog_section("repositories", "Portfolio repositories", "Repository collection", "The seven repositories already connected to this portfolio: agentic tools, creative automation, and Swift foundations.", all_repos, "repository-deck"))


def generate_startup_source(source_id):
    source = STARTUP_SOURCES[source_id]
    return f'<a class="startup-source" href="{escape(source["url"], quote=True)}" target="_blank" rel="noopener noreferrer">{escape(source["label"])} <span aria-hidden="true">↗</span><span class="startup-source-kind">{escape(source["kind"])}</span></a>'


def generate_enriched_case(project_id, case, index=0, kind="company", narrative_label="My contribution", include_project_action=False, include_related_publication=False, icon_image=None):
    entity = WAKEN_AI if project_id == "waken" else PROJECTS[project_id]
    name = case.get("name") or entity_name(entity)
    role = entity.get("role") or case.get("role") or "Independent project"
    year = entity.get("year") or case.get("year") or "Current"
    source_links = generate_startup_source(case["contribution_source"])
    if case.get("additional_source"):
        source_links += generate_startup_source(case["additional_source"])
    if include_project_action:
        project_url = entity_url(entity)
        if project_url:
            action_label = entity.get("link_label") or "Explore project"
            source_links += f'<a class="startup-case-action" href="{escape(project_url, quote=True)}" target="_blank" rel="noopener noreferrer">{escape(action_label)} <span aria-hidden="true">↗</span></a>'
    if include_related_publication and case.get("related_publication"):
        publication = case["related_publication"]
        publication_id = publication["catalog_id"]
        publication_url = entity_url(PROJECTS[publication_id]) if publication_id in PROJECTS else book_by_id(publication_id)["url"]
        source_links += f'<a class="startup-case-action startup-case-publication" href="{escape(publication_url, quote=True)}" target="_blank" rel="noopener noreferrer">{escape(publication["label"])} <span aria-hidden="true">↗</span></a>'
    highlights = ''.join(f'''<li class="startup-highlight">
        <span class="startup-highlight-scope">{escape(item["scope"])}</span>
        <strong class="startup-highlight-value{' startup-highlight-value--words' if len(item['value']) > 7 else ''}">{escape(item["value"])}</strong>
        <h4>{escape(item["label"])}</h4><p>{escape(item["detail"])}</p>
        {generate_startup_source(item["source"])}
      </li>''' for item in case["highlights"])
    header_icon = (f'<img {image_attributes(icon_image, loading="lazy", sizes="52px")} alt="" />'
                   if icon_image else sparks_icon(case['icon']))
    return f'''<article class="startup-case startup-case--{case['accent']}{' startup-case--reverse' if index % 2 else ''}" id="{project_id}-{kind}" aria-labelledby="{project_id}-case-title">
      <header class="startup-case-header">
        <div class="startup-case-identity"><span class="startup-case-icon{' startup-case-icon--app' if icon_image else ''}" aria-hidden="true">{header_icon}</span><div><span class="eyebrow">{escape(case['category'])}</span><h3 id="{project_id}-case-title">{escape(name)}</h3></div></div>
        <p class="startup-case-role">{escape(role)}<span>{escape(year)}</span></p>
      </header>
      <div class="startup-case-body">
        <div class="startup-case-media">{generate_showcase_media(project_id, entity, name, square_video_preview=kind == "project")}</div>
        <div class="startup-case-contribution"><span class="eyebrow">{escape(narrative_label)}</span><h4>{escape(case['thesis'])}</h4><p>{escape(case['contribution'])}</p><div class="startup-contribution-sources">{source_links}</div></div>
      </div>
      <ul class="startup-highlights" aria-label="{escape(name)} contribution and outcome highlights">{highlights}</ul>
    </article>'''


def generate_startup_case(project_id, index=0, kind="company"):
    # Reuse the Mobile Apps visual identity wherever the startup has a shipped
    # app, so the same product is immediately recognisable across the site.
    return generate_enriched_case(
        project_id,
        STARTUP_CASES[project_id],
        index,
        kind,
        icon_image=mobile_app_icon_asset(project_id),
    )


def generate_project_case(project_id, index=0, include_related_publication=False, page=None):
    """Project-page case study using the Startup evidence format and technical lens."""
    case = PROJECT_CASES_BY_PAGE.get(page, {}).get(project_id, PROJECT_CASES[project_id])
    icon_image = mobile_app_icon_asset(project_id) if page in {"mobile-apps", "agentic-ai"} else None
    return generate_enriched_case(project_id, case, index, "project", "Technical contribution", include_project_action=True, include_related_publication=include_related_publication, icon_image=icon_image)


def generate_startup_metrics():
    """Startup company milestones in the landing-page counter layout."""
    items = []
    for project_id, item_index in STARTUP_HERO_HIGHLIGHTS:
        item = STARTUP_CASES[project_id]["highlights"][item_index]
        source = STARTUP_SOURCES[item["source"]]
        items.append(f'''<div class="stat-item">
          <div class="startup-counter-company">{escape(entity_name(PROJECTS[project_id]))}</div>
          <div class="value">{escape(item["value"])}</div>
          <div class="label">{escape(item["label"])}</div>
          <a class="startup-counter-source" href="{escape(source["url"], quote=True)}" target="_blank" rel="noopener noreferrer">{escape(source["label"])} ↗</a>
        </div>''')
    return f'<section class="startup-hero-stats" aria-label="Sourced company milestones"><div class="stats-row">{"".join(items)}</div></section>'


def generate_startups_page():
    exits = [generate_startup_case(item, index, "exit") for index, item in enumerate(PAGE_COMPOSITIONS["startups"]["exits"])]
    companies = [generate_startup_case(item, index) for index, item in enumerate(PAGE_COMPOSITIONS["startups"]["companies"])]
    releases = ''.join(f'<li><span>{escape(item["date"])}</span><a href="{escape(item["url"], quote=True)}" target="_blank" rel="noopener noreferrer">{escape(item["title"])} ↗</a><small>{escape(item["source"])}</small></li>' for item in PRESS_RELEASES)
    return (generate_topic_hero("Startups", "Built to ship. Engineered to scale.", "From first prototype to platforms used by millions. Founder-led products, mobile engineering, and the company milestones behind the work.", press_loop=True, hero_variant="startups")
            + generate_startup_metrics()
            + generate_topic_index((("exits", "Exits"), ("companies", "Product work"), ("waken", "Waken AI"), ("press-releases", "Press releases"), ("press", "Press & interviews")))
            + generate_catalog_section("exits", "Product creation & acquisitions", "From first build to lasting impact", "Independent products and acquisition stories, from professional capture to social video at scale.", exits, "startup-cases")
            + generate_catalog_section("companies", "Architecture at scale", "Inside ambitious product teams", "Native platforms for immersive commerce and direct audience relationships. Each case connects engineering ownership with dated, sourced company outcomes.", companies, "startup-cases")
            + generate_catalog_section("waken", "Founder-led research & products", "Waken AI", "A bootstrapped lab connecting conversational products, persistent context, and agentic engineering.", [generate_startup_case("waken", kind="lab")], "startup-cases")
            + f'''<section class="catalog-section" id="press-releases"><header class="catalog-section-header"><span class="eyebrow">Company-issued news</span><h2>Press releases</h2><p>Original issuer links, separated from independent coverage and syndicated copies.</p><a class="catalog-back" href="#overview">← Back to overview</a></header><ul class="release-list">{releases}</ul></section>'''
            + generate_press_and_interviews())


def generate_books_page():
    composition = PAGE_COMPOSITIONS["books"]
    all_articles = [generate_showcase_article_card(item, index) for index, item in enumerate(ARTICLE_CATALOG)]
    return (generate_topic_hero("Books & writing", "Books for builders and curious minds", "Technical field notes alongside books about AI, mobile systems, fiction, and reflective practice.", image="three-technical-books-hero", square_image=True)
            + generate_topic_index((("technical-books", "Technical books"), ("articles", "Technical articles"), ("earlier-books", "Earlier books")))
            + generate_book_shelf("technical-books", "Technical books", "Books for builders", "Three practical books on durable AI context, Apple Silicon, and mobile architecture.", composition["technical"])
            + generate_showcase_section("articles", "Technical writing", "Articles", "Long-form notes that make implementation decisions and lessons reusable.", all_articles)
            + generate_book_shelf("earlier-books", "Earlier books", "AI, fiction & journaling", "Earlier published work across research, fiction, and reflective writing.", composition["earlier"]))


def generate_legacy_selected_page():
    return f'''<section class="compatibility-page"><span class="eyebrow">Portfolio update</span><h1>Explore My Work</h1><p>This former portfolio route now points to dedicated pages for each practice.</p>{generate_selected_work_grid("selected-work")}</section>'''


def render_portfolio(page="home"):
    """Render a portfolio page from the shared generator source."""
    if page not in {*SITE_PAGES, "selected-work"}:
        raise ValueError(f"Unsupported portfolio page: {page}")
    metadata = get_page_metadata(page)
    canonical_url = f'{SITE_URL}/{metadata["path"]}'
    structured_data = generate_structured_data(page, metadata)
    metadata_title = escape(metadata["title"])
    metadata_description = escape(metadata["description"])
    social_image = metadata_image(metadata)
    social_image_url = f'{SITE_URL}/{social_image["url"]}'
    social_image_alt = escape(metadata.get("image_alt", f'Portrait of {IDENTITY["name"]}'))
    robots = metadata_robots(metadata)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{metadata_title}</title>
  <meta name="description" content="{metadata_description}">
  <meta name="author" content="{IDENTITY["name"]}">
  <meta name="robots" content="{robots}">
  <meta name="googlebot" content="{robots}">
  <link rel="canonical" href="{canonical_url}">
  <meta property="og:type" content="{metadata.get('og_type', 'website')}">
  <meta property="og:locale" content="en_US">
  <meta property="og:site_name" content="{IDENTITY["name"]}">
  <meta property="og:title" content="{metadata_title}">
  <meta property="og:description" content="{metadata_description}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{social_image_url}">
  <meta property="og:image:alt" content="{social_image_alt}">
  <meta property="og:image:width" content="{social_image["width"]}">
  <meta property="og:image:height" content="{social_image["height"]}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{metadata_title}">
  <meta name="twitter:description" content="{metadata_description}">
  <meta name="twitter:image" content="{social_image_url}">
  <meta name="twitter:image:alt" content="{social_image_alt}">
  <script type="application/ld+json">{structured_data}</script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
  <style>
{CSS_STYLES}
{COMPONENT_STYLES}
{SIGNAL_STYLES}

  </style>
</head>
<body>


'''
    content = {
        "home": generate_home_content,
        "selected-work": generate_legacy_selected_page,
        "profile": generate_profile_content,
        "agentic-ai": generate_agentic_page,
        "mobile-apps": generate_mobile_page,
        "github": generate_github_page,
        "startups": generate_startups_page,
        "books": generate_books_page,
    }[page]()
    resume_script = f'<script type="module">{RESUME_SCRIPT}</script>' if page == "profile" else ''
    return (html + generate_header(page) + '<main id="main-content" tabindex="-1">'
            + content + '</main>' + generate_contact() +
            f'<script>{INTERACTION_SCRIPT}</script>' + resume_script + '</body></html>')


def generate_home_content():
    return (generate_hero() + generate_proof() + generate_selected_work_grid()
            + generate_clineflow_section() + generate_home_research_callout() + generate_agentic_ai_callout()
            + generate_meme_arcade_callout() + generate_wwdc14_feature() + generate_ios_open_source_callout()
            + generate_books_media()
            + generate_about() + generate_quote())


def generate_profile_content():
    """Generate the focused professional resume page."""
    return (generate_professional_profile(heading_tag="h1")
            + generate_recognition() + generate_citations_section()
            + generate_selected_work_grid(page="profile") + generate_press_and_interviews()
            + generate_about())


def generate_selected_content():
    return generate_work_intro() + f'''
  <!-- Selected Work Sequence -->
  <!-- Impact Section -->
  <section class="section" id="impact">
    <div class="section-header white">
      {generate_section_nav("Proven Success")}
      <h2>Impact & Exits</h2>
      <p class="lead">A decade of building products that reached millions and raised millions.</p>
    </div>
    
    {"".join(generate_impact_card(c) for c in HISTORIC_COMPANIES)}
  </section>

  <!-- Waken AI Featured Callout -->
  <section class="waken-callout" id="waken">
    <div class="waken-inner">
      <div class="waken-header">
        {generate_section_nav()}
        <img {image_attributes(WAKEN_AI["logo"], loading="lazy")} alt="{WAKEN_AI["name"]}" class="waken-logo" />
        <h2 class="waken-tagline">{WAKEN_AI["tagline"]}</h2>
        <p class="waken-subtitle">{WAKEN_AI["subtitle"]}</p>
        <p class="waken-description">{WAKEN_AI["description"]}</p>
      </div>

      <div class="waken-video-container">
        {generate_video_frame(WAKEN_AI["video"], WAKEN_AI["name"])}
      </div>

      <p class="waken-quote">"{WAKEN_AI["quote"]}"</p>
      <p class="waken-positioning">{WAKEN_AI["positioning"]}</p>

      <div class="waken-footer">
        <a href="{WAKEN_AI["website"]}" target="_blank" class="waken-cta">
          Visit Waken AI →
        </a>
      </div>
    </div>
  </section>

  <!-- Current Work -->
  <section class="section" id="work">
    <div class="section-header white">
      {generate_section_nav("Current Focus")}
      <h2>AI Projects</h2>
      <p class="lead">Building the future of AI-human interaction through ethical, ergonomic technology.</p>
    </div>

    {"".join(generate_current_project_card(p) for p in CURRENT_PROJECTS)}
  </section>

  <!-- TwinChat Paper -->
  <section class="paper-chapter" id="twinchat-paper" aria-labelledby="paper-title">
    <div class="paper-inner">
      <div class="paper-copy">
        {generate_section_nav("Research Publication")}
        <h2 id="paper-title">{TWINCHAT_PAPER["name"]}</h2>
        <p class="paper-subtitle">{TWINCHAT_PAPER["subtitle"]}</p>
        <p class="paper-description">{TWINCHAT_PAPER["description"]}</p>
        <a href="{TWINCHAT_PAPER["github"]}" target="_blank" rel="noopener noreferrer" class="home-tooling-link">Read TwinChat Paper <span aria-hidden="true">↗</span></a>
      </div>
      <div class="paper-topics">
        <span class="eyebrow">{TWINCHAT_PAPER["tagline"]}</span>
        <h3>Inside the paper</h3>
        <ol>
          {"".join(f'<li><span aria-hidden="true">{i:02d}</span>{escape(topic)}</li>' for i, topic in enumerate(TWINCHAT_PAPER["features"], 1))}
        </ol>
      </div>
      <div class="paper-perspective">
        <blockquote>{TWINCHAT_PAPER["quote"]}</blockquote>
        <p>{TWINCHAT_PAPER["positioning"]}</p>
      </div>
    </div>
  </section>

  <!-- Technical Writing -->
  {generate_technical_writing()}

  <!-- iOS Open Source -->
  {generate_swift_foundations()}

  <!-- Early Innovations -->
  <details class="early-innovations" id="research">
    <summary><span>View Early Innovations</span><span class="early-innovations-icon" aria-hidden="true">+</span></summary>
    <section class="section early-innovations-content" aria-labelledby="early-innovations-title">
      <div class="section-header white">
        {generate_section_nav("Early Work")}
        <h2 id="early-innovations-title">Early Innovations</h2>
        <p class="lead">Selected experiments and production work across mobile video, AR, and rendering systems.</p>
      </div>
      <div class="innovation-grid">
        {"".join(generate_innovation_card(i) for i in INNOVATIONS)}
      </div>
    </section>
  </details>

  <!-- Filmography -->
  {generate_filmography_section()}

  <!-- Writing About Trends -->
  <section class="section" id="casual-books">
    <div class="section-header white">
      {generate_section_nav("Published Works")}
      <h2>Writing Fiction &amp; Journaling</h2>
    </div>
    <div class="books-grid">
      {generate_books_html(BOOKS[2:])}
    </div>
  </section>

'''


def generate_books_media():
    return f'''
  <!-- Books -->
  <section class="section" id="books" aria-labelledby="books-chapter-title">
    {generate_home_chapter_heading('books')}
    {generate_featured_book(FEATURED_BOOKS[0]).strip()}
    <div class="books-grid">
      {generate_books_html(BOOKS[:2])}
    </div>
  </section>

  {generate_technical_writing_callout().strip()}

'''


def generate_press_and_interviews():
    """Render media coverage beside the resume, after the shared Sparks gateway."""
    return f'''

  <!-- Press -->
  <section class="section" id="press" style="padding-top: 0;">
    <div class="section-header" style="margin-bottom: 40px; margin-top: 24px;">
      {generate_section_nav()}
      <h2>Press</h2>
    </div>
    <div class="press-grid">
      {generate_press_html()}
    </div>
  </section>

  <!-- Interviews -->
  <section class="section" id="interviews">
    <div class="section-header">
      {generate_section_nav("Media & Speaking")}
      <h2>Interviews</h2>
    </div>
    <div class="interviews-grid">
      {generate_interviews_html()}
    </div>
  </section>

'''


def generate_about():
    return f'''
  <!-- Bio / Artist Introduction -->
  <section class="bio-section" id="about">
    <div class="bio-content">
      {generate_section_nav()}
      <h2 class="bio-headline">{BIO["headline"]}</h2>
      <figure class="bio-profile-image">
        <img {image_attributes(BIO["image"], loading="lazy")} alt="{BIO["image_alt"]}" />
      </figure>
      <div class="bio-featured-article">
        <div class="article-label">Featured Profile</div>
        <a href="{BIO["headline_link"]}" target="_blank" rel="noopener noreferrer" class="article-title">On the Future of Artificial Intelligence</a>
        <a href="{BIO["headline_link"]}" target="_blank" rel="noopener noreferrer" class="bio-read-button">Read Bio</a>
        <div class="article-source">Authority Magazine</div>
      </div>
    </div>
  </section>

'''


def generate_recognition():
    return f'''
  <!-- EB1A Recognition -->
  <section class="bio-section" id="eb1a">
    <div class="bio-content">
      <div class="eb1a-card">
        {generate_section_nav()}
        <h3>{BIO["eb1a_overview"]["title"]}</h3>
        <p class="eb1a-description">{BIO["eb1a_overview"]["description"]}</p>
        <ul class="eb1a-criteria">
          {"".join(f'<li>{c}</li>' for c in BIO["eb1a_overview"]["criteria_met"])}
        </ul>
        <a href="{BIO["eb1a_overview"]["wikipedia_url"]}" target="_blank" rel="noopener noreferrer" class="eb1a-wikipedia-link">EB1A on Wikipedia →</a>
      </div>
    </div>
  </section>

'''


def generate_quote():
    return f'''
  <!-- Quote -->
  <section class="quote-section">
    <blockquote>"{IDENTITY["quote"]}"</blockquote>
    <cite>— {IDENTITY["name"]}</cite>
  </section>

'''

def generate_header(page):
    def navigation_link(label, href, target_page=None, external=False):
        current = target_page == page
        classes = "nav-link is-current" if current else "nav-link"
        current_attribute = ' aria-current="page"' if current else ""
        external_attributes = ' target="_blank" rel="noopener noreferrer"' if external else ""
        return f'<a class="{classes}" href="{href}"{current_attribute}{external_attributes}>{label}</a>'

    links = ''.join(navigation_link(label, page_href(target), target) for label, target in NAVIGATION)
    mobile_links = (
        navigation_link("Home", "index.html", "home")
        + navigation_link("Book a call", "https://intro.co/hassanuriostegui", external=True)
        + ''.join(navigation_link(label, page_href(target), target) for label, target in NAVIGATION)
    )
    return f'''
    <a class="skip-link" href="#main-content">Skip to content</a>
    <header class="site-header">
      <nav class="site-nav" aria-label="Main navigation">
        <a class="site-identity" href="index.html"><span class="identity-mark" aria-hidden="true">hu.</span><span>Hassan Uriostegui</span></a>
        <div class="desktop-links">{links}</div>
        <a class="desktop-clineflow" href="{CLINEFLOW['website']}" target="_blank" rel="noopener noreferrer">ClineFlow <span aria-hidden="true">↗</span></a>
        <a class="header-book" href="https://intro.co/hassanuriostegui" target="_blank" rel="noopener noreferrer">Book a call <span aria-hidden="true">↗</span></a>
        <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobileMenu" hidden>Menu <span aria-hidden="true">＋</span></button>
      </nav>
    </header>
    <dialog id="mobileMenu" class="signal-menu" aria-labelledby="menu-title">
      <div class="menu-heading"><h2 id="menu-title">Explore</h2><button type="button" class="menu-close" aria-label="Close navigation menu">Close ×</button></div>
      <nav aria-label="All sections">{mobile_links}</nav>
      <div class="mobile-menu-actions">
        <a class="signal-button" href="https://intro.co/hassanuriostegui" target="_blank" rel="noopener noreferrer">Book a consultation ↗</a>
        <a class="signal-button mobile-clineflow" href="{CLINEFLOW['website']}" target="_blank" rel="noopener noreferrer">ClineFlow <span aria-hidden="true">↗</span></a>
      </div>
    </dialog>
    <noscript><nav class="noscript-nav" aria-label="All sections">{mobile_links}</nav></noscript>
    '''


def generate_hero():
    return f'''
    <section class="signal-hero" id="home" aria-labelledby="hero-title">
      <div class="signal-hero-inner">
        <div class="signal-copy">
          <p class="signal-eyebrow"><span aria-hidden="true"></span>EB-1A · EXTRAORDINARY ABILITY</p>
          <h1 id="hero-title">Hassan<br /><em>Uriostegui.</em></h1>
          <p class="signal-position">Principal Engineer.<br />Founder. <span>AI-Native.</span></p>
          <p class="signal-summary">I build AI-native products from prototype to production—agentic systems, consumer platforms, and high-performance mobile applications.</p>
          <div class="signal-actions">
            <a class="signal-button" href="https://intro.co/hassanuriostegui" target="_blank" rel="noopener noreferrer">Book a consultation <span aria-hidden="true">↗</span></a>
            <a class="signal-text-link" href="#explore-work">Explore my work <span aria-hidden="true">→</span></a>
          </div>
        </div>
        <figure class="portrait-stage">
          <div class="depth-rig" aria-hidden="true"><span class="depth-plane plane-back"></span><span class="depth-plane plane-middle"></span><span class="depth-plane plane-front"></span></div>
          <div class="portrait-window"><img {image_attributes(IDENTITY['portrait'], fetchpriority='high')} alt="Portrait of Hassan Uriostegui" /></div>
          <figcaption><span>HASSAN URIOSTEGUI</span><span>AI-native principal engineer</span></figcaption>
          <span class="stage-index" aria-hidden="true">01 / HUMAN IN THE LOOP</span>
        </figure>
      </div>
      <div class="hero-baseline"><span>AI & CONTEXT ENGINEERING</span><span>MOBILE & CONSUMER PRODUCTS</span><a href="#proof">THE WORK SPEAKS <span aria-hidden="true">↓</span></a></div>
    </section>
    '''


def generate_proof():
    logos = ''.join(f'<div class="press-logo-item"><img {image_attributes(logo["logo"], loading="lazy")} alt="{logo["name"]}" /></div>' for logo in PRESS_LOGOS)
    repeats = ''.join(f'<div class="press-logo-item"><img {image_attributes(logo["logo"], loading="lazy")} alt="" /></div>' for logo in PRESS_LOGOS)
    return f'''
    <section id="proof" class="proof-section" aria-label="Experience and recognition">
      <div class="stats-row">{generate_stats_html()}</div>
      <div class="proof-press">
        <div class="press-strip-heading"><a href="{resolve_navigation_href('#press', 'home')}">IN THE PRESS ↗</a><button type="button" class="press-pause" hidden>Pause logos</button></div>
        <div class="proof-marquee"><div class="proof-track"><div class="proof-logo-group">{logos}</div><div class="proof-logo-group logo-repeat" aria-hidden="true">{repeats}</div></div></div>
      </div>
    </section>'''


def generate_work_intro():
    return f'''
    <section class="work-intro" id="selected-work" aria-labelledby="work-title">
      <div class="work-intro-inner">
        <p class="signal-eyebrow">SELECTED WORK / HASSAN URIOSTEGUI</p>
        <h1 id="work-title">Ideas into<br /><em>impact.</em></h1>
        <p>From real-time visual effects to mobile platforms and AI systems. A body of work built at the intersection of engineering and imagination.</p>
        <div class="work-intro-meta"><span>ENGINEERING</span><span>ENTREPRENEURSHIP</span><span>RESEARCH</span></div>
      </div>
      <div class="work-orbit" aria-hidden="true"><span></span><span></span><span></span></div>
    </section>
    {generate_selected_work_grid("selected-work")}
    '''


def generate_contact():
    return f'''
    <footer id="contact" class="signal-footer">
      <div class="contact-callout">
        <div><p class="signal-eyebrow">LET’S BUILD WHAT’S NEXT</p><h2>Building an<br /><em>AI-native product?</em></h2><p>Bring your AI, mobile, or product engineering challenge. Let’s work through it together.</p></div>
        <div class="contact-actions"><a class="signal-button" href="https://intro.co/hassanuriostegui" target="_blank" rel="noopener noreferrer">Book a consultation <span aria-hidden="true">↗</span></a><a href="https://unidosus.org/" target="_blank" rel="noopener noreferrer">50% goes to UnidosUS <span aria-hidden="true">↗</span></a></div>
      </div>
      <div class="footer-details"><div><strong>{IDENTITY['name']}</strong><p>{IDENTITY['status']}</p>{generate_footer_bio_html()}</div><div class="footer-links">{generate_social_links()}<a href="mailto:{IDENTITY['email']}">Email ↗</a><button type="button" id="motion-toggle" aria-pressed="false" hidden>Reduce motion</button></div></div>
      <p class="copyright">© 2026 Hassan Uriostegui. All rights reserved.</p>
    </footer>'''


def generate_portfolio():
    """Generate all static portfolio pages from the Python source."""
    print("Generating portfolio pages...")
    root = os.path.dirname(os.path.dirname(__file__))
    outputs = {
        ("index.html" if page == "home" else metadata["path"]): render_portfolio(page)
        for page, metadata in SITE_PAGES.items()
    }
    outputs.update({
        SELECTED_WORK_PAGE: render_portfolio("selected-work"),
        "robots.txt": generate_robots_txt(),
        "sitemap.xml": generate_sitemap_xml(),
    })
    for filename, content in outputs.items():
        if filename.endswith(".html"):
            content = "\n".join(line.rstrip() for line in content.splitlines()) + "\n"
        output_path = os.path.join(root, filename)
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(content)
        print(f"Portfolio generated: {output_path} ({len(content):,} bytes)")
    return [os.path.join(root, filename) for filename in outputs]


if __name__ == "__main__":
    generate_portfolio()
