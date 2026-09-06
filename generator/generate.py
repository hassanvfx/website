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

SELECTED_WORK_PAGE = "selected-work.html"
PROFILE_PAGE = "profile.html"
SITE_URL = "https://hassanvfx.github.io/website"
SITE_DESCRIPTION = "Hassan Uriostegui is an AI-native principal engineer, founder, and author building agentic systems, consumer products, Swift open-source tools, and AI platforms."
SITE_LAST_MODIFIED = "2026-09-06"
SELECTED_WORK_SECTION_IDS = {"selected-work", "impact", "work", "ios-open-source", "technical-writing", "waken", "twinchat-paper", "research", "filmography", "casual-books"}
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
SELECTED_WORK_ITEMS = AI_SPARK_ITEMS + OTHER_SPARK_ITEMS + [("Innovations", "research")] + HOBBY_SPARK_ITEMS
IMAGE_MANIFEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image_manifest.json")


def load_image_manifest():
    """Load the generated-image URLs that are safe to render on the site."""
    with open(IMAGE_MANIFEST_PATH, encoding="utf-8") as manifest_file:
        return json.load(manifest_file)


IMAGE_MANIFEST = load_image_manifest()
with open(os.path.join(os.path.dirname(__file__), "video_metadata.json"), encoding="utf-8") as video_file:
    VIDEO_METADATA = json.load(video_file)


def generate_video_frame(url, title):
    """Reserve each player's provider-declared aspect ratio before network loading."""
    video = VIDEO_METADATA[url]
    width, height = int(video['width']), int(video['height'])
    if width <= 0 or height <= 0:
        raise ValueError(f"Invalid video dimensions: {url}")
    return (f'<div class="video-frame" style="--video-ratio: {width} / {height}">'
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
    if page == "selected-work":
        return {
            "title": "Selected Work | Hassan Uriostegui",
            "description": "Selected work by Hassan Uriostegui across AI innovation, iOS open source, products, startup impact, technical writing, research, and visual effects.",
            "path": SELECTED_WORK_PAGE,
        }
    if page == "profile":
        return {
            "title": "Resume | Hassan Uriostegui",
            "description": "Professional resume and profile for Hassan Uriostegui, AI-native principal and founding engineer.",
            "path": PROFILE_PAGE,
        }
    return {
        "title": "Hassan Uriostegui | AI-Native Principal Engineer & ClineFlow Creator",
        "description": SITE_DESCRIPTION,
        "path": "",
    }


def generate_structured_data(metadata):
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
    ] if metadata["path"] == SELECTED_WORK_PAGE else []
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
    ] if metadata["path"] == SELECTED_WORK_PAGE else []
    about = [{"@id": author_id}, {"@id": clineflow_id}]
    about.extend({"@id": node["@id"]} for node in foundation_nodes)
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
                "image": IMAGE_MANIFEST[IDENTITY["portrait"]]["url"],
                "jobTitle": "AI-Native Principal Engineer, Founder, and Author",
                "sameAs": [link["url"] for link in SOCIAL_LINKS],
                "knowsAbout": ["Artificial Intelligence", "Context Engineering", "Mobile Product Development", "ClineFlow"],
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
                "@type": "WebPage",
                "@id": canonical_url,
                "url": canonical_url,
                "name": metadata["title"],
                "description": metadata["description"],
                "inLanguage": "en-US",
                "author": {"@id": author_id},
                "about": about,
                "isPartOf": {"@id": f"{SITE_URL}/#website"},
            },
        ] + foundation_nodes + article_nodes,
    }
    return json.dumps(structured_data, ensure_ascii=False, separators=(",", ":"))


def generate_robots_txt():
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


def generate_sitemap_xml():
    """Expose every canonical generated page with current publishing metadata."""
    pages = (
        ("", "1.0", "weekly"),
        (SELECTED_WORK_PAGE, "0.8", "monthly"),
        (PROFILE_PAGE, "0.8", "monthly"),
    )
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
    if section_id == "contact":
        return href
    return href if page == "home" else f"index.html{href}"


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
        items.append(f'<a href="{href}"{featured_class}{target}>{nav["label"]}</a>')
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
            '<a class="sparks-return" href="#explore-sparks" aria-label="More Sparks — return to Explore Sparks on this page">'
            '<span class="sparks-return-arrow" aria-hidden="true">←</span><span>More Sparks</span></a></div>')


def generate_selected_work_grid(page="home"):
    """Generate the small home-page gateway to the Selected Work page."""
    def links(items, modifier=""):
        return "\n          ".join(
            f'<a href="{resolve_navigation_href(f"#{section_id}", page)}" class="selected-work-link{modifier}">{sparks_icon(section_id)}<span class="sparks-label">{escape(label)}</span><span class="sparks-arrow" aria-hidden="true">→</span></a>'
            for label, section_id in items
        )

    ai_links = links(AI_SPARK_ITEMS, " selected-work-link--ai")
    other_links = links(OTHER_SPARK_ITEMS)
    hobby_links = links(HOBBY_SPARK_ITEMS)
    return f'''
  <!-- Selected Work Gateway -->
  <section class="selected-work-gateway" id="explore-sparks" tabindex="-1" aria-labelledby="selected-work-title">
    <div class="selected-work-gateway-inner">
      <span class="eyebrow">Selected Work</span>
      <h2 id="selected-work-title">Explore Sparks</h2>
      <section class="selected-work-topic-group selected-work-topic-group--ai" aria-labelledby="ai-sparks-title">
        <div class="selected-work-topic-heading">
          <p id="ai-sparks-title">AI SYSTEMS</p>
          <span>Context, prompts, and products</span>
        </div>
        <div class="selected-work-grid selected-work-grid--ai">
          {ai_links}
        </div>
      </section>
      <section class="selected-work-topic-group" aria-labelledby="more-sparks-title">
        <div class="selected-work-topic-heading">
          <p id="more-sparks-title">MORE SPARKS</p>
          <span>Open source, product impact, and shared learning</span>
        </div>
        <div class="selected-work-grid">
          {other_links}
        </div>
      </section>
      <section class="selected-work-topic-group" aria-labelledby="hobbies-sparks-title">
        <div class="selected-work-topic-heading">
          <p id="hobbies-sparks-title">HOBBIES</p>
          <span>Film, visual effects, and writing</span>
        </div>
        <div class="selected-work-grid selected-work-grid--pair">
          {hobby_links}
        </div>
      </section>
    </div>
  </section>
'''


def generate_clineflow_section():
    """Generate the focused ClineFlow installer callout."""
    return f'''
  <!-- ClineFlow Agentic Installer -->
  <section class="clineflow-callout clineflow-installer" id="clineflow">
    <div class="clineflow-installer-shell">
      <figure class="clineflow-hero clineflow-installer-hero">
        <img {image_attributes("clineflow-hero", loading="lazy")} alt="Persistent Context, Open Knowledge — ClineFlow AI coding memory now native OKE" />
      </figure>
      <div class="clineflow-installer-inner">
        {generate_section_nav()}
        <a href="{CLINEFLOW["website"]}" target="_blank" rel="noopener noreferrer" class="clineflow-wordmark">Creator of {CLINEFLOW["name"]}</a>
        <h2><span>Infinite AI Memory</span> across chats, agents and collaborators.</h2>
        <div class="clineflow-explainer">
          <p>ClineFlow gives AI coding agents durable project memory using open files instead of vendor-locked databases.</p>
          <p>A filesystem-native knowledge layer that travels with the repository, evolves through version control, and stays usable across agents and collaborators.</p>
        </div>
        <div class="clineflow-installer-panel">
          <p>Try the agentic installer</p>
          <div class="clineflow-prompt-wrap">
            <code id="clineflow-installer-prompt">{CLINEFLOW["installer_prompt"]}</code>
            <button type="button" class="clineflow-copy-button" data-copy-prompt="clineflow-installer-prompt">Copy prompt</button><span class="copy-status" role="status" aria-live="polite"></span>
          </div>
        </div>
      </div>
      <div class="clineflow-support">
        <figure class="clineflow-agent-compatibility">
          <img {image_attributes("clineflow-agent-compatibility", loading="lazy")} alt="ClineFlow compatibility with major AI coding agents" />
          <figcaption>Works across major AI coding agents.</figcaption>
        </figure>
        <div class="clineflow-masterclass">
          <p>Explore ClineFlow:</p>
          <div class="clineflow-masterclass-divider" aria-hidden="true"></div>
          <a href="{CLINEFLOW["website"]}" target="_blank" rel="noopener noreferrer" class="clineflow-masterclass-cta">View project <span aria-hidden="true">↗</span></a>
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
    """Connect the homepage Apple feature to the Swift projects on Sparks."""
    return f'''
  <section class="ios-sparks-callout" aria-labelledby="ios-sparks-heading">
    <div class="ios-sparks-callout-inner">
      <h2 id="ios-sparks-heading" class="sparks-callout-title"><span class="sparks-callout-icon">{sparks_icon("ios-open-source")}</span>More iOS Sparks</h2>
      <p>Build on three open-source Swift tools: SwiftSPM for package scaffolding, DataStore for encrypted persistence, and WebViewSwiftUI for bringing web content into native apps.</p>
      <a class="home-tooling-link" href="{SELECTED_WORK_PAGE}#ios-open-source">More iOS Sparks <span aria-hidden="true">→</span></a>
    </div>
  </section>
'''


def generate_ai_sparks_callout():
    """Bridge ClineFlow to the wider AI work on the Sparks page."""
    return f'''
  <section class="ai-sparks-callout" aria-labelledby="ai-sparks-heading">
    <div class="ai-sparks-callout-inner">
      <h2 id="ai-sparks-heading" class="sparks-callout-title"><span class="sparks-callout-icon">{sparks_icon("work")}</span>More AI Sparks</h2>
      <p>Explore agentic products, AI context systems, and prompt engineering experiments across the Sparks portfolio.</p>
      <a class="home-tooling-link" href="{SELECTED_WORK_PAGE}#work">More AI Sparks <span aria-hidden="true">→</span></a>
    </div>
  </section>
'''


def generate_technical_writing_callout():
    """Bridge published books to the longer technical articles on Sparks."""
    return f'''
  <section class="writing-sparks-callout" aria-labelledby="writing-sparks-heading">
    <div class="writing-sparks-callout-inner">
      <h2 id="writing-sparks-heading" class="sparks-callout-title"><span class="sparks-callout-icon">{sparks_icon("technical-writing")}</span>More Technical Writing</h2>
      <p>Read practical notes from building AI systems, Swift tools, and creative workflows—shared to make the decisions, trade-offs, and lessons reusable.</p>
      <a class="home-tooling-link" href="{SELECTED_WORK_PAGE}#technical-writing">More Technical Writing <span aria-hidden="true">→</span></a>
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
  <section class="citations-section" id="citations">
    <div class="citations-inner">
      <div class="citations-intro">
        {generate_section_nav(CITATIONS["eyebrow"], "citations-eyebrow")}
        <h2>{CITATIONS["title"]}</h2>
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
        <span class="featured-book-eyebrow">{book["eyebrow"]}</span>
        <h2>{book["title"]}</h2>
        <p class="featured-book-subtitle">{book["subtitle"]}</p>
        <p class="featured-book-description">{book["description"]}</p>
        {actions_html}
      </div>
      <a href="{book["url"]}" target="_blank" rel="noopener noreferrer" class="featured-book-cover-link">
        <img {image_attributes(book["image"], loading="lazy", sizes="(max-width: 800px) calc(100vw - 128px), (max-width: 1320px) calc((100vw - 280px) / 2), 520px")} alt="{book["image_alt"]}" class="featured-book-cover" />
      </a>
    </div>
  </section>
'''


def generate_meme_arcade_callout():
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
  <section class="meme-arcade-callout" id="memearcade">
    <div class="meme-arcade-inner">
      <div class="meme-arcade-copy">
      <div class="meme-app-icon"><img {image_attributes(MEME_ARCADE["icon"], loading="lazy")} alt="{MEME_ARCADE["icon_alt"]}" class="meme-arcade-icon" /></div>
      {generate_section_nav("IPHONE GAME ARCADE", "meme-arcade-badge")}
      <h2>{MEME_ARCADE["title"]}</h2>
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
      {website_btn}
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
        <span class="year">{book["year"]} • {book.get("language", "English")}</span>
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


def render_portfolio(page="home"):
    """Render a portfolio page from the shared generator source."""
    if page not in {"home", "selected-work", "profile"}:
        raise ValueError(f"Unsupported portfolio page: {page}")
    metadata = get_page_metadata(page)
    canonical_url = f'{SITE_URL}/{metadata["path"]}'
    structured_data = generate_structured_data(metadata)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{metadata["title"]}</title>
  <meta name="description" content="{metadata["description"]}">
  <meta name="author" content="{IDENTITY["name"]}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <meta name="googlebot" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="{canonical_url}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{IDENTITY["name"]}">
  <meta property="og:title" content="{metadata["title"]}">
  <meta property="og:description" content="{metadata["description"]}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:image" content="{SITE_URL}/{IMAGE_MANIFEST[IDENTITY["portrait"]]["url"]}">
  <meta property="og:image:alt" content="Portrait of {IDENTITY["name"]}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{metadata["title"]}">
  <meta name="twitter:description" content="{metadata["description"]}">
  <meta name="twitter:image" content="{SITE_URL}/{IMAGE_MANIFEST[IDENTITY["portrait"]]["url"]}">
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
        "selected-work": generate_selected_content,
        "profile": generate_profile_content,
    }[page]()
    resume_script = f'<script type="module">{RESUME_SCRIPT}</script>' if page == "profile" else ''
    return (html + generate_header(page) + '<main id="main-content" tabindex="-1">'
            + content + '</main>' + generate_contact() +
            f'<script>{INTERACTION_SCRIPT}</script>' + resume_script + '</body></html>')


def generate_home_content():
    return (generate_hero() + generate_proof() + generate_selected_work_grid()
            + generate_clineflow_section() + generate_ai_sparks_callout() + generate_meme_arcade_callout()
            + generate_wwdc14_feature() + generate_ios_open_source_callout() + generate_citations_section()
            + generate_books_media()
            + generate_about() + generate_quote() + generate_recognition())


def generate_profile_content():
    """Generate the focused professional resume page."""
    return (generate_professional_profile(heading_tag="h1")
            + generate_selected_work_grid(page="profile"))


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

  <!-- Research & Innovations -->
  <section class="section" id="research">
    <div class="section-header white">
      {generate_section_nav("Research & Development")}
      <h2>Innovations</h2>
      <p class="lead">Selected products and technical work spanning mobile video, AR, generative systems, and AI.</p>
    </div>
    
    <div class="innovation-grid">
      {"".join(generate_innovation_card(i) for i in INNOVATIONS)}
    </div>
  </section>

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
  <section class="section" id="books">
    <div class="section-header white">
      {generate_section_nav("Published Works")}
      <h2>Books &amp; Technical Writing</h2>
    </div>
    {generate_featured_book(FEATURED_BOOKS[0]).strip()}
    <div class="books-grid">
      {generate_books_html(BOOKS[:2])}
    </div>
  </section>

  {generate_technical_writing_callout().strip()}

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
    desktop_links = [
        ('Resume', PROFILE_PAGE),
        ('AI coding', '#clineflow'),
        ('Apps', '#memearcade'),
        ('Citations', '#citations'),
        ('Books', '#books'),
        ('Press', '#press'),
        ('Sparks', '#selected-work'),
    ]
    links = ''.join(
        f'<a href="{resolve_navigation_href(href, page)}">{label}</a>'
        for label, href in desktop_links
    )
    links += (f'<a href="{CLINEFLOW["website"]}" target="_blank" rel="noopener noreferrer" '
              'class="desktop-clineflow">ClineFlow <span aria-hidden="true">↗</span></a>')
    mobile_links = generate_mobile_nav_html(page)
    return f'''
    <a class="skip-link" href="#main-content">Skip to content</a>
    <header class="site-header">
      <nav class="site-nav" aria-label="Main navigation">
        <a class="site-identity" href="{resolve_navigation_href('#home', page)}"><span class="identity-mark" aria-hidden="true">hu.</span><span>Hassan Uriostegui</span></a>
        <div class="desktop-links">{links}</div>
        <a class="header-book" href="https://intro.co/hassanuriostegui" target="_blank" rel="noopener noreferrer">Book a call <span aria-hidden="true">↗</span></a>
        <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobileMenu" hidden>Menu <span aria-hidden="true">＋</span></button>
      </nav>
    </header>
    <dialog id="mobileMenu" class="signal-menu" aria-labelledby="menu-title">
      <div class="menu-heading"><h2 id="menu-title">Explore</h2><button type="button" class="menu-close" aria-label="Close navigation menu">Close ×</button></div>
      <nav aria-label="All sections">{mobile_links}</nav>
      <a class="signal-button" href="https://intro.co/hassanuriostegui" target="_blank" rel="noopener noreferrer">Book a consultation ↗</a>
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
          <p class="signal-position">Principal Engineer.<br />Founder. <span>Author.</span></p>
          <p class="signal-summary">I build AI-native products from prototype to production—agentic systems, consumer platforms, and high-performance mobile applications.</p>
          <div class="signal-actions">
            <a class="signal-button" href="https://intro.co/hassanuriostegui" target="_blank" rel="noopener noreferrer">Book a consultation <span aria-hidden="true">↗</span></a>
            <a class="signal-text-link" href="{SELECTED_WORK_PAGE}">Explore selected work <span aria-hidden="true">→</span></a>
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
        <div class="press-strip-heading"><a href="#press">IN THE PRESS ↗</a><button type="button" class="press-pause" hidden>Pause logos</button></div>
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
        "index.html": render_portfolio("home"),
        SELECTED_WORK_PAGE: render_portfolio("selected-work"),
        PROFILE_PAGE: render_portfolio("profile"),
        "robots.txt": generate_robots_txt(),
        "sitemap.xml": generate_sitemap_xml(),
    }
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
