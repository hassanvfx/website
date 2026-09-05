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
    CITATIONS, FEATURED_BOOKS, WWDC14_FEATURE
)
from templates.css import CSS_STYLES, COMPONENT_STYLES, SIGNAL_STYLES
from templates.scripts import INTERACTION_SCRIPT, RESUME_SCRIPT

SELECTED_WORK_PAGE = "selected-work.html"
SITE_URL = "https://hassanvfx.github.io/website"
SITE_DESCRIPTION = "Hassan Uriostegui is an AI-native principal engineer, founder, author, and creator of ClineFlow, building agentic systems, consumer products, and AI platforms."
SELECTED_WORK_SECTION_IDS = {"selected-work", "impact", "work", "waken", "twinchat-paper", "research", "filmography"}
SELECTED_WORK_ITEMS = [
    ("Impact & Exits", "impact"),
    ("Featured Projects", "work"),
    ("TwinChat Paper", "twinchat-paper"),
    ("Innovations", "research"),
    ("Filmography & VFX", "filmography"),
]
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


def image_attributes(key, loading=None, fetchpriority=None):
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
        sizes = {
            "portrait": "(max-width: 800px) 250px, 360px",
            "clineflow-hero": "(max-width: 800px) calc(100vw - 56px), 580px",
            "bio-profile": "(max-width: 800px) calc(100vw - 48px), 900px",
            "resume-preview": "(max-width: 800px) calc(100vw - 80px), 620px",
        }[key]
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
            "description": "Selected work by Hassan Uriostegui across AI innovation, research, products, startup impact, and visual effects.",
            "path": SELECTED_WORK_PAGE,
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
                "about": [{"@id": author_id}, {"@id": clineflow_id}],
                "isPartOf": {"@id": f"{SITE_URL}/#website"},
            },
        ],
    }
    return json.dumps(structured_data, ensure_ascii=False, separators=(",", ":"))


def generate_robots_txt():
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


def generate_sitemap_xml():
    pages = ("", SELECTED_WORK_PAGE)
    urls = "\n".join(
        f"  <url><loc>{SITE_URL}/{page}</loc><priority>{'1.0' if not page else '0.8'}</priority></url>"
        for page in pages
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


def generate_selected_work_grid():
    """Generate the small home-page gateway to the Selected Work page."""
    links = "\n        ".join(
        f'<a href="{SELECTED_WORK_PAGE}#{section_id}" class="selected-work-link">{label}<span aria-hidden="true">→</span></a>'
        for label, section_id in SELECTED_WORK_ITEMS
    )
    return f'''
  <!-- Selected Work Gateway -->
  <section class="selected-work-gateway" aria-labelledby="selected-work-title">
    <div class="selected-work-gateway-inner">
      <span class="eyebrow">Selected Work</span>
      <h2 id="selected-work-title">Explore Portfolio Highlights</h2>
      <div class="selected-work-grid">
        {links}
      </div>
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
        <a href="{CLINEFLOW["website"]}" target="_blank" rel="noopener noreferrer" class="clineflow-wordmark">{CLINEFLOW["name"]}</a>
        <h2><span>Infinite AI Memory</span> across chats, agents and collaborators.</h2>
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
          <figcaption>ClineFlow is supported by all major Agents</figcaption>
        </figure>
        <div class="clineflow-masterclass">
          <p>Learn More about ClineFlow:</p>
          <div class="clineflow-masterclass-divider" aria-hidden="true"></div>
          <a href="{CLINEFLOW["website"]}" target="_blank" rel="noopener noreferrer" class="clineflow-masterclass-cta">www.ClineFlow.com <span aria-hidden="true">→</span></a>
        </div>
      </div>
    </div>
  </section>
'''


def generate_professional_profile():
    """Generate the embedded PDF.js professional profile viewer."""
    return f'''
  <section class="professional-profile" id="professional-profile">
    <div class="professional-profile-inner">
      <div class="professional-profile-copy">
        <span class="professional-profile-eyebrow">{PROFESSIONAL_PROFILE["eyebrow"]}</span>
        <h2>{PROFESSIONAL_PROFILE["title"]}</h2>
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
        <span class="wwdc14-eyebrow">{WWDC14_FEATURE["eyebrow"]}</span>
        <h2>{WWDC14_FEATURE["title"]}</h2>
        <p class="wwdc14-subtitle">{WWDC14_FEATURE["subtitle"]}</p>
        <p class="wwdc14-description">{WWDC14_FEATURE["description"]}</p>
        <blockquote>{WWDC14_FEATURE["quote"]}</blockquote>
        <div class="wwdc14-actions">
          <a href="{WWDC14_FEATURE["medium_url"]}" target="_blank" rel="noopener noreferrer" class="wwdc14-btn wwdc14-btn-primary">Read the Story on Medium →</a>
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
        <span class="citations-eyebrow">{CITATIONS["eyebrow"]}</span>
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
        <img {image_attributes(book["image"], loading="lazy")} alt="{book["image_alt"]}" class="featured-book-cover" />
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
      <span class="meme-arcade-badge">IPHONE GAME ARCADE</span>
      <h2>{MEME_ARCADE["title"]}</h2>
      <p class="meme-arcade-description">{MEME_ARCADE["description"]}</p>
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
    website_btn = f'<a href="{project["website"]}" target="_blank" class="btn btn-outline">Visit Website</a>' if project.get("website") else ""
    quote = f'<p class="quote">"{project["quote"]}"</p>' if project.get("quote") else ""
    
    return f'''
  <article class="project-card" id="{project["id"]}">
    <div class="card-video">
      {generate_video_frame(video_url, project["name"])}
    </div>
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
      <span class="eyebrow">{FILMOGRAPHY["years"]}</span>
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
        image_html = f'<img {image_attributes(book["image"], loading="lazy")} alt="{book["title"]}" class="{cover_class}" />' if book.get("image") else ""
        
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
    if page not in {"home", "selected-work"}:
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
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
  <style>
{CSS_STYLES}
{COMPONENT_STYLES}
{SIGNAL_STYLES}

  </style>
</head>
<body>


'''
    content = generate_home_content() if page == "home" else generate_selected_content()
    resume_script = f'<script type="module">{RESUME_SCRIPT}</script>' if page == "home" else ''
    return (html + generate_header(page) + '<main id="main-content" tabindex="-1">'
            + content + '</main>' + generate_contact() +
            f'<script>{INTERACTION_SCRIPT}</script>' + resume_script + '</body></html>')


def generate_home_content():
    return (generate_hero() + generate_proof() + generate_professional_profile()
            + generate_clineflow_section() + generate_meme_arcade_callout()
            + generate_wwdc14_feature() + generate_citations_section()
            + generate_books_media()
            + generate_about() + generate_quote() + generate_selected_work_grid() + generate_recognition())


def generate_selected_content():
    return generate_work_intro() + f'''
  <!-- Selected Work Sequence -->
  <!-- Impact Section -->
  <section class="section" id="impact">
    <div class="section-header white">
      <span class="eyebrow">Proven Success</span>
      <h2>Impact & Exits</h2>
      <p class="lead">A decade of building products that reached millions and raised millions.</p>
    </div>
    
    {"".join(generate_impact_card(c) for c in HISTORIC_COMPANIES)}
  </section>

  <!-- Waken AI Featured Callout -->
  <section class="waken-callout" id="waken">
    <div class="waken-inner">
      <div class="waken-header">
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
      <span class="eyebrow">Current Focus</span>
      <h2>Featured Projects</h2>
      <p class="lead">Building the future of AI-human interaction through ethical, ergonomic technology.</p>
    </div>

    {"".join(generate_current_project_card(p) for p in CURRENT_PROJECTS)}
  </section>

  <!-- TwinChat Paper Callout -->
  <section class="clineflow-callout" id="twinchat-paper">
    <div class="clineflow-inner">
      <img {image_attributes(TWINCHAT_PAPER["logo"], loading="lazy")} alt="GitHub" class="clineflow-logo" />
      <span class="clineflow-badge">📄 RESEARCH PUBLICATION</span>
      <h2 class="clineflow-title">{TWINCHAT_PAPER["name"]}</h2>
      <p class="clineflow-tagline">{TWINCHAT_PAPER["tagline"]}</p>
      <p class="clineflow-subtitle">{TWINCHAT_PAPER["subtitle"]}</p>
      
      <p class="clineflow-description">{TWINCHAT_PAPER["description"]}</p>
      
      <div class="clineflow-features">
        {"".join(f'<div class="clineflow-feature"><span>{f}</span></div>' for f in TWINCHAT_PAPER["features"])}
      </div>
      
      <p class="clineflow-quote">"{TWINCHAT_PAPER["quote"]}"</p>
      
      <p class="clineflow-positioning">{TWINCHAT_PAPER["positioning"]}</p>
      
      <a href="{TWINCHAT_PAPER["github"]}" target="_blank" class="clineflow-cta">
        Read TwinChat Paper →
      </a>
      
      <span class="clineflow-stars">{TWINCHAT_PAPER["stars"]}</span>
    </div>
  </section>

  <!-- Research & Innovations -->
  <section class="section" id="research">
    <div class="section-header white">
      <span class="eyebrow">Research & Development</span>
      <h2>Innovations</h2>
      <p class="lead">Building tomorrow's technology, years before the industry catches up.</p>
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
      <span class="eyebrow">Published Works</span>
      <h2>Writing About Trends</h2>
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
      <span class="eyebrow">Published Works</span>
      <h2>Books</h2>
    </div>
    {generate_featured_book(FEATURED_BOOKS[0]).strip()}
    <div class="books-grid">
      {generate_books_html(BOOKS[:2])}
    </div>
  </section>

  <!-- Interviews -->
  <section class="section" id="interviews">
    <div class="section-header">
      <span class="eyebrow">Media & Speaking</span>
      <h2>Interviews</h2>
    </div>
    <div class="interviews-grid">
      {generate_interviews_html()}
    </div>
  </section>

  <!-- Press -->
  <section class="section" id="press" style="padding-top: 0;">
    <div class="section-header" style="margin-bottom: 40px; margin-top: 24px;">
      <h2>Press</h2>
    </div>
    <div class="press-grid">
      {generate_press_html()}
    </div>
  </section>

'''


def generate_about():
    return f'''
  <!-- Bio / Artist Introduction -->
  <section class="bio-section" id="about">
    <div class="bio-content">
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
        ('Profile', '#professional-profile'),
        ('AI coding', '#clineflow'),
        ('Apps', '#memearcade'),
        ('Citations', '#white-house'),
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
          <p class="signal-eyebrow"><span aria-hidden="true"></span>ENGINEER · FOUNDER · AUTHOR</p>
          <h1 id="hero-title">Hassan<br /><em>Uriostegui.</em></h1>
          <p class="signal-position">Ambitious ideas.<br />Engineered for <span>real impact.</span></p>
          <p class="signal-summary">AI systems, mobile products, and the engineering decisions that move them forward. Work directly with a principal engineer who has built for millions.</p>
          <div class="signal-actions">
            <a class="signal-button" href="https://intro.co/hassanuriostegui" target="_blank" rel="noopener noreferrer">Book a consultation <span aria-hidden="true">↗</span></a>
            <a class="signal-text-link" href="{SELECTED_WORK_PAGE}">Explore selected work <span aria-hidden="true">→</span></a>
          </div>
          <p class="hero-footnote">Silicon Valley experience. Independent perspective.</p>
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
    links = ''.join(f'<a href="#{section}">{label}<span aria-hidden="true">↓</span></a>' for label, section in SELECTED_WORK_ITEMS)
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
    <nav class="work-index" aria-label="Selected Work sections">{links}</nav>
    '''


def generate_contact():
    return f'''
    <footer id="contact" class="signal-footer">
      <div class="contact-callout">
        <div><p class="signal-eyebrow">LET’S BUILD WHAT’S NEXT</p><h2>A clearer path<br /><em>from idea to product.</em></h2><p>Bring your AI, mobile, or product engineering challenge. Let’s work through it together.</p></div>
        <div class="contact-actions"><a class="signal-button" href="https://intro.co/hassanuriostegui" target="_blank" rel="noopener noreferrer">Book a consultation ↗</a><a href="https://unidosus.org/" target="_blank" rel="noopener noreferrer">50% goes to UnidosUS ↗</a></div>
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
