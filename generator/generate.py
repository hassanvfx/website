#!/usr/bin/env python3
"""
Portfolio Generator v3 - Impact First Structure
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from portfolio_data import (
    IDENTITY, STATS, NAV_ITEMS, SOCIAL_LINKS, CURRENT_PROJECTS,
    HISTORIC_COMPANIES, BOOKS, PRESS, RECOGNITION, FILMOGRAPHY,
    INNOVATIONS, AI_SHOWCASE_VIDEOS, TIMELINE_MARKERS, AI_ART_PLAYLISTS,
    BIO, SECTION_QUOTES, CLINEFLOW, INTERVIEWS, WAKEN_AI, TWINCHAT_PAPER
)
from templates import CSS_STYLES


def generate_nav_html():
    """Generate navigation with ClineFlow featured"""
    items = []
    for nav in NAV_ITEMS:
        featured_class = ' class="featured"' if nav.get("featured") else ''
        target = ' target="_blank"' if nav.get("external") else ''
        items.append(f'<a href="{nav["href"]}"{featured_class}{target}>{nav["label"]}</a>')
    return "\n      ".join(items)


def generate_stats_html():
    """Generate stats row HTML"""
    items = []
    for stat in STATS:
        items.append(f'''<div class="stat-item">
          <div class="value">{stat["value"]}</div>
          <div class="label">{stat["label"]}</div>
        </div>''')
    return "\n        ".join(items)


def generate_timeline_marker(year, label):
    """Generate timeline intersection marker"""
    return f'''
  <section class="timeline-marker">
    <div class="marker-line"></div>
    <div class="marker-circle">{year}</div>
    <div class="marker-label">{label}</div>
    <div class="marker-line"></div>
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
    
    return f'''
  <article class="impact-card" id="{company["id"]}">
    <div class="card-video">
      <iframe src="{company["video"]}?autoplay=0&muted=1&controls=1" 
              frameborder="0" allowfullscreen allow="autoplay"></iframe>
    </div>
    <div class="card-content">
      <span class="highlight">{company["highlight"]}</span>
      <h3>{company["name"]}</h3>
      <p class="role">{company["role"]} • {company["year"]}</p>
      <p class="description">{company["description"]}</p>
      {press_quote_html}
    </div>
  </article>
'''


def generate_ai_showcase():
    """Generate AI videos showcase grid - first 4 visible, rest hidden"""
    visible = []
    hidden = []
    for i, video in enumerate(AI_SHOWCASE_VIDEOS):
        html = f'''<div class="showcase-video">
        <iframe src="{video["url"]}?autoplay=0&muted=1&controls=1" frameborder="0" allowfullscreen allow="autoplay"></iframe>
      </div>'''
        if i < 4:
            visible.append(html)
        else:
            hidden.append(html)
    
    return "\n      ".join(visible), "\n      ".join(hidden)


def generate_current_project_card(project):
    """Generate current AI project card"""
    video_url = project["videos"][0]["url"] if project.get("videos") else ""
    website_btn = f'<a href="{project["website"]}" target="_blank" class="btn btn-outline">Visit Website</a>' if project.get("website") else ""
    quote = f'<p class="quote">"{project["quote"]}"</p>' if project.get("quote") else ""
    
    return f'''
  <article class="project-card" id="{project["id"]}">
    <div class="card-video">
      <iframe src="{video_url}?autoplay=0&muted=1&controls=1" 
              frameborder="0" allowfullscreen allow="autoplay"></iframe>
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
      <iframe src="{innovation["video"]}?autoplay=0&muted=1&controls=1" 
              frameborder="0" allowfullscreen allow="autoplay"></iframe>
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
        <iframe src="{video["url"]}?autoplay=0&muted=1&controls=1" frameborder="0" allowfullscreen></iframe>
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


def generate_books_html():
    """Generate books section"""
    items = []
    for book in BOOKS:
        press_html = f'<p class="press">{book["press"]}</p>' if book.get("press") else ""
        target = "" if book.get("local") else ' target="_blank"'
        
        items.append(f'''<article class="book-card">
        <span class="year">{book["year"]} • {book.get("language", "English")}</span>
        <h3>{book["title"]}</h3>
        <p class="subtitle">{book["subtitle"]}</p>
        {press_html}
        <a href="{book["url"]}"{target} class="btn btn-outline">Read More</a>
      </article>''')
    
    return "\n      ".join(items)


def generate_press_html():
    """Generate press section"""
    items = []
    for article in PRESS:
        items.append(f'''<a href="{article["url"]}" target="_blank" class="press-card">
        <span class="publication">{article["publication"]}</span>
        <h4>{article["headline"]}</h4>
        <p>{article["excerpt"]}</p>
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
        <iframe src="{i["url"]}?autoplay=0&muted=1&controls=1" frameborder="0" allowfullscreen></iframe>
        <div class="interview-info">
          <h4>{i["title"]}</h4>
          <p>{i["context"]}</p>
        </div>
      </div>''')
    return "\n      ".join(items)


def generate_portfolio():
    """Main generation function - Impact First"""
    print("Generating Impact-First Portfolio v3...")
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{IDENTITY["name"]} - {IDENTITY["status"]}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
  <style>
{CSS_STYLES}

/* Hero Portrait */
.hero-portrait {{
  margin-bottom: 2.5rem;
}}
.hero-portrait img {{
  width: 280px;
  height: 350px;
  border-radius: 16px;
  object-fit: cover;
  object-position: top center;
  border: 3px solid rgba(0, 212, 255, 0.3);
  box-shadow: 0 0 50px rgba(0, 212, 255, 0.25), 0 0 100px rgba(139, 92, 246, 0.15);
  transition: all 0.3s ease;
}}
.hero-portrait img:hover {{
  border-color: rgba(0, 212, 255, 0.6);
  box-shadow: 0 0 70px rgba(0, 212, 255, 0.4), 0 0 120px rgba(139, 92, 246, 0.25);
  transform: scale(1.02);
}}

/* Timeline Markers */
.timeline-marker {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  padding: 3rem 0;
  background: #000;
}}
.marker-line {{
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, #333, transparent);
  max-width: 200px;
}}
.marker-circle {{
  background: #1a1a1a;
  border: 2px solid #333;
  border-radius: 50px;
  padding: 0.75rem 1.5rem;
  color: #fff;
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 0.9rem;
}}
.marker-label {{
  color: #666;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}}

/* Featured Nav Link - Neon Cyan */
nav a.featured {{
  background: linear-gradient(135deg, #00D4FF, #8B5CF6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 600;
  text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
}}
nav a.featured:hover {{
  text-shadow: 0 0 40px rgba(0, 212, 255, 0.8), 0 0 60px rgba(139, 92, 246, 0.5);
}}
nav a:hover {{
  color: #00D4FF !important;
}}

/* Hamburger Menu Button */
.hamburger {{
  display: none;
  flex-direction: column;
  justify-content: center;
  gap: 5px;
  width: 30px;
  height: 30px;
  cursor: pointer;
  z-index: 1002;
  position: relative;
}}
.hamburger span {{
  display: block;
  width: 100%;
  height: 2px;
  background: #fff;
  transition: all 0.3s ease;
}}
.hamburger.active span:nth-child(1) {{
  transform: rotate(45deg) translate(5px, 5px);
}}
.hamburger.active span:nth-child(2) {{
  opacity: 0;
}}
.hamburger.active span:nth-child(3) {{
  transform: rotate(-45deg) translate(5px, -5px);
}}

/* Mobile Menu Modal */
.mobile-menu {{
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.98);
  z-index: 1001;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, visibility 0.3s ease;
}}
.mobile-menu.active {{
  opacity: 1;
  visibility: visible;
}}
.mobile-menu a {{
  font-size: 24px;
  font-weight: 500;
  color: rgba(255,255,255,0.8);
  text-decoration: none;
  padding: 16px 32px;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  transition: all 0.3s ease;
}}
.mobile-menu a:hover {{
  color: #00D4FF;
}}
.mobile-menu a.featured {{
  background: linear-gradient(135deg, #00D4FF, #8B5CF6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 600;
}}

/* Mobile Nav Responsive */
@media (max-width: 768px) {{
  .hamburger {{
    display: flex;
  }}
  .nav-inner a {{
    display: none;
  }}
  .mobile-menu {{
    display: flex;
  }}
  .scroll-nav .nav-inner {{
    justify-content: space-between;
    padding: 0 20px;
  }}
}}

/* Impact Cards */
.impact-card {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  background: #0a0a0a;
  padding: 2rem;
  margin-bottom: 1px;
}}
.impact-card:nth-child(even) {{
  direction: rtl;
}}
.impact-card:nth-child(even) > * {{
  direction: ltr;
}}
.impact-card .card-video iframe {{
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: 8px;
}}
.impact-card .highlight {{
  display: inline-block;
  background: linear-gradient(135deg, rgba(0,212,255,0.15), rgba(139,92,246,0.15));
  color: #00D4FF;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-size: 0.85rem;
  font-weight: 500;
  margin-bottom: 1rem;
  border: 1px solid rgba(0,212,255,0.2);
}}
.impact-card h3 {{
  font-family: 'Playfair Display', serif;
  font-size: 2rem;
  margin: 0.5rem 0;
  color: #fff;
}}
.impact-card .role {{
  color: #888;
  margin-bottom: 1rem;
}}

/* Company Press Quotes */
.company-press-quote {{
  margin-top: 1.5rem;
  padding: 1rem;
  background: rgba(0,212,255,0.05);
  border-left: 3px solid #00D4FF;
  border-radius: 0 8px 8px 0;
}}
.company-press-quote .quote-text {{
  font-family: 'Playfair Display', serif;
  font-style: italic;
  color: rgba(255,255,255,0.8);
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 0.5rem;
}}
.company-press-quote .quote-source {{
  color: rgba(255,255,255,0.5);
  font-size: 0.8rem;
}}
.company-press-quote .quote-source strong {{
  color: #00D4FF;
}}

/* AI Showcase Grid - 2 columns max */
.ai-showcase {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  padding: 2rem;
  background: #000;
  max-width: 1000px;
  margin: 0 auto;
}}
.showcase-video {{
  border-radius: 12px;
  overflow: hidden;
}}
.showcase-video iframe {{
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: 8px;
}}
.showcase-video.hidden {{
  display: none;
}}
.showcase-video.shown {{
  display: block;
}}

/* Project Cards */
.project-card {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  background: #0a0a0a;
  padding: 2rem;
  margin-bottom: 1px;
}}
.project-card:nth-child(odd) {{
  direction: rtl;
}}
.project-card:nth-child(odd) > * {{
  direction: ltr;
}}
.project-card .card-video iframe {{
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: 8px;
}}
.project-card .highlight {{
  display: inline-block;
  background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(139,92,246,0.1));
  color: #00D4FF;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-size: 0.85rem;
  margin-bottom: 1rem;
  border: 1px solid rgba(0,212,255,0.2);
}}
.project-card h3 {{
  font-family: 'Playfair Display', serif;
  font-size: 1.75rem;
  margin: 0.5rem 0;
  color: #fff;
}}
.project-card .quote {{
  font-style: italic;
  color: #888;
  border-left: 2px solid #333;
  padding-left: 1rem;
  margin: 1rem 0;
}}

/* Innovation Cards */
.innovation-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1rem;
  padding: 2rem;
}}
.innovation-card {{
  background: #0a0a0a;
  border-radius: 12px;
  overflow: hidden;
}}
.innovation-card.featured {{
  grid-column: 1 / -1;
  background: linear-gradient(135deg, rgba(0,212,255,0.05), rgba(139,92,246,0.08));
  border: 1px solid rgba(0,212,255,0.2);
  padding: 2rem;
}}
.innovation-card .badge {{
  display: inline-block;
  background: linear-gradient(135deg, rgba(0,212,255,0.15), rgba(139,92,246,0.15));
  color: #00D4FF;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-size: 0.85rem;
  margin-bottom: 1rem;
  border: 1px solid rgba(0,212,255,0.2);
}}
.innovation-card .year-badge {{
  display: inline-block;
  background: rgba(0,212,255,0.1);
  color: #00D4FF;
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-size: 0.75rem;
  border: 1px solid rgba(0,212,255,0.15);
}}
.innovation-card h3 {{
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  margin: 0.5rem 0;
  color: #fff;
}}
.innovation-card .tagline {{
  background: linear-gradient(135deg, #00D4FF, #8B5CF6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 500;
  margin-bottom: 0.5rem;
}}
.innovation-card .card-content {{
  padding: 1.5rem;
}}
.innovation-card .card-video iframe {{
  width: 100%;
  aspect-ratio: 16/9;
}}

/* Filmography */
.filmography .film-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 2rem;
  padding: 2rem;
}}
.film-video iframe {{
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: 8px;
}}
.film-video .video-title {{
  color: #888;
  text-align: center;
  margin-top: 0.5rem;
}}
.film-links {{
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  padding: 2rem;
}}
.ves-badge {{
  background: linear-gradient(135deg, #b8860b, #daa520);
  color: #000;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-weight: 600;
  font-size: 0.85rem;
}}

/* Books */
.books-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
  padding: 2rem;
}}
.book-card {{
  background: #0a0a0a;
  border-radius: 12px;
  padding: 2rem;
}}
.book-card .year {{
  color: #666;
  font-size: 0.85rem;
}}
.book-card h3 {{
  font-family: 'Playfair Display', serif;
  font-size: 1.25rem;
  margin: 0.5rem 0;
  color: #fff;
}}
.book-card .subtitle {{
  color: #888;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}}
.book-card .press {{
  color: #00D4FF;
  font-size: 0.85rem;
  margin-bottom: 1rem;
}}

/* Press */
.press-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
  padding: 2rem;
}}
.press-card {{
  background: #0a0a0a;
  border-radius: 8px;
  padding: 1.5rem;
  text-decoration: none;
  transition: all 0.3s ease;
  border: 1px solid transparent;
}}
.press-card:hover {{
  background: #111;
  transform: translateY(-2px);
  border-color: rgba(0,212,255,0.2);
  box-shadow: 0 0 20px rgba(0, 212, 255, 0.1);
}}
.press-card .publication {{
  color: #00D4FF;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
}}

/* Show More Button */
.show-more-container {{
  text-align: center;
  padding: 2rem;
}}
.show-more-btn {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 28px;
  font-size: 14px;
  font-weight: 500;
  text-decoration: none;
  border-radius: 50px;
  background: transparent;
  color: #00D4FF;
  border: 1px solid rgba(0, 212, 255, 0.3);
  cursor: pointer;
  transition: all 0.3s ease;
}}
.show-more-btn:hover {{
  border-color: #00D4FF;
  box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
  background: rgba(0, 212, 255, 0.05);
}}
.show-more-btn .arrow {{
  transition: transform 0.3s ease;
}}
.show-more-btn.expanded .arrow {{
  transform: rotate(180deg);
}}

/* Hidden content */
.more-content {{
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.5s ease;
}}
.more-content.expanded {{
  max-height: 2000px;
}}

/* AI Playlist cards */
.playlist-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 1.5rem;
  padding: 2rem;
}}
.playlist-card {{
  background: #0a0a0a;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(0,212,255,0.1);
}}
.playlist-card iframe {{
  width: 100%;
  aspect-ratio: 16/9;
}}
.playlist-card .playlist-info {{
  padding: 1rem;
  text-align: center;
}}
.playlist-card .playlist-info h4 {{
  color: #fff;
  margin-bottom: 0.5rem;
}}
.playlist-card .playlist-info a {{
  color: #00D4FF;
  text-decoration: none;
  font-size: 0.9rem;
}}
.playlist-card .playlist-info a:hover {{
  text-decoration: underline;
}}
.press-card h4 {{
  color: #fff;
  font-size: 1rem;
  margin: 0.5rem 0;
}}
.press-card p {{
  color: #888;
  font-size: 0.85rem;
}}

/* Bio/Artist Intro Section */
.bio-section {{
  padding: 6rem 4rem;
  background: linear-gradient(180deg, #000 0%, #0a0a0a 100%);
}}
.bio-content {{
  max-width: 900px;
  margin: 0 auto;
}}
.bio-headline {{
  font-family: 'Playfair Display', serif;
  font-size: 2.5rem;
  color: #fff;
  margin-bottom: 2rem;
  text-align: center;
}}
.bio-intro {{
  font-size: 1.2rem;
  line-height: 1.8;
  color: rgba(255,255,255,0.8);
  margin-bottom: 3rem;
  text-align: center;
}}
.eb1a-card {{
  background: linear-gradient(135deg, rgba(0,212,255,0.08), rgba(139,92,246,0.08));
  border: 1px solid rgba(0,212,255,0.2);
  border-radius: 16px;
  padding: 2.5rem;
  margin-bottom: 2rem;
}}
.eb1a-card h3 {{
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  color: #fff;
  margin-bottom: 1rem;
}}
.eb1a-card .eb1a-description {{
  color: rgba(255,255,255,0.7);
  margin-bottom: 1.5rem;
  line-height: 1.7;
}}
.eb1a-criteria {{
  list-style: none;
  padding: 0;
}}
.eb1a-criteria li {{
  color: rgba(255,255,255,0.8);
  padding: 0.5rem 0;
  padding-left: 2rem;
  position: relative;
  font-size: 0.95rem;
}}
.eb1a-criteria li::before {{
  content: "✓";
  position: absolute;
  left: 0;
  color: #00D4FF;
  font-weight: bold;
}}
.bio-summary {{
  font-size: 1.1rem;
  line-height: 1.8;
  color: rgba(255,255,255,0.7);
  text-align: center;
  font-style: italic;
}}

/* Press Quote Dividers */
.press-quote-divider {{
  padding: 4rem 2rem;
  background: linear-gradient(180deg, #050505 0%, #0a0a0a 50%, #050505 100%);
  text-align: center;
}}
.press-quote-divider blockquote {{
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  font-style: italic;
  color: rgba(255,255,255,0.8);
  max-width: 800px;
  margin: 0 auto 1rem;
  line-height: 1.6;
}}
.press-quote-divider .source {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}}
.press-quote-divider .source-name {{
  color: #00D4FF;
  font-weight: 600;
  font-size: 0.9rem;
}}
.press-quote-divider .source-context {{
  color: rgba(255,255,255,0.5);
  font-size: 0.85rem;
}}
.press-quote-divider a {{
  color: #00D4FF;
  text-decoration: none;
}}
.press-quote-divider a:hover {{
  text-decoration: underline;
}}

/* ClineFlow Featured Callout */
.clineflow-callout {{
  padding: 6rem 4rem;
  background: linear-gradient(180deg, #000 0%, #050510 50%, #000 100%);
  position: relative;
  overflow: hidden;
}}
.clineflow-callout::before {{
  content: "";
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(0,212,255,0.1) 0%, transparent 70%);
  pointer-events: none;
}}
.clineflow-inner {{
  max-width: 900px;
  margin: 0 auto;
  text-align: center;
  position: relative;
  z-index: 1;
}}
.clineflow-logo {{
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin-bottom: 1.5rem;
  filter: invert(1);
  transition: all 0.3s ease;
}}
.clineflow-logo:hover {{
  transform: scale(1.1);
  filter: invert(1) drop-shadow(0 0 20px rgba(0,212,255,0.5));
}}
.clineflow-badge {{
  display: inline-block;
  background: linear-gradient(135deg, rgba(0,212,255,0.2), rgba(139,92,246,0.2));
  color: #00D4FF;
  padding: 0.5rem 1.5rem;
  border-radius: 50px;
  font-size: 0.85rem;
  font-weight: 600;
  margin-bottom: 2rem;
  border: 1px solid rgba(0,212,255,0.3);
  letter-spacing: 0.1em;
}}
.clineflow-title {{
  font-family: 'Playfair Display', serif;
  font-size: 3.5rem;
  margin-bottom: 0.5rem;
  background: linear-gradient(135deg, #00D4FF, #8B5CF6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}}
.clineflow-tagline {{
  font-size: 1.4rem;
  color: rgba(255,255,255,0.9);
  margin-bottom: 0.5rem;
}}
.clineflow-subtitle {{
  color: rgba(255,255,255,0.5);
  font-size: 1rem;
  margin-bottom: 2rem;
}}
.clineflow-description {{
  font-size: 1.15rem;
  line-height: 1.8;
  color: rgba(255,255,255,0.75);
  margin-bottom: 2.5rem;
}}
.clineflow-features {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 2.5rem;
  text-align: left;
}}
.clineflow-feature {{
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 0.75rem;
  background: rgba(0,212,255,0.05);
  border-radius: 8px;
  border: 1px solid rgba(0,212,255,0.1);
}}
.clineflow-feature::before {{
  content: "→";
  color: #00D4FF;
  font-weight: bold;
}}
.clineflow-feature span {{
  color: rgba(255,255,255,0.8);
  font-size: 0.9rem;
}}
.clineflow-quote {{
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-size: 1.15rem;
  color: rgba(255,255,255,0.6);
  margin-bottom: 2rem;
  padding: 0 2rem;
}}
.clineflow-positioning {{
  font-size: 1rem;
  color: #00D4FF;
  font-weight: 500;
  margin-bottom: 2.5rem;
}}
.clineflow-cta {{
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 16px 36px;
  font-size: 1.1rem;
  font-weight: 600;
  text-decoration: none;
  border-radius: 50px;
  background: linear-gradient(135deg, #00D4FF, #8B5CF6);
  color: #000;
  transition: all 0.3s ease;
  box-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
}}
.clineflow-cta:hover {{
  transform: translateY(-2px);
  box-shadow: 0 0 50px rgba(0, 212, 255, 0.5), 0 0 80px rgba(139, 92, 246, 0.3);
}}
.clineflow-stars {{
  display: block;
  margin-top: 1.5rem;
  color: rgba(255,255,255,0.5);
  font-size: 0.9rem;
}}

/* Waken AI Featured Callout */
.waken-callout {{
  padding: 6rem 4rem;
  background: linear-gradient(180deg, #000 0%, #051015 50%, #000 100%);
  position: relative;
  overflow: hidden;
  border-top: 1px solid rgba(0,212,255,0.15);
  border-bottom: 1px solid rgba(0,212,255,0.15);
}}
.waken-callout::before {{
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 800px;
  height: 800px;
  background: radial-gradient(ellipse at center, rgba(0,212,255,0.08) 0%, transparent 60%);
  pointer-events: none;
}}
.waken-inner {{
  max-width: 1000px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}}
.waken-header {{
  text-align: center;
  margin-bottom: 3rem;
}}
.waken-logo {{
  max-width: 280px;
  height: auto;
  filter: invert(1) brightness(1.2);
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
}}
.waken-logo:hover {{
  filter: invert(1) brightness(1.4);
  transform: scale(1.02);
}}
.waken-tagline {{
  font-family: 'Playfair Display', serif;
  font-size: 1.8rem;
  color: rgba(255,255,255,0.9);
  margin-bottom: 0.5rem;
}}
.waken-subtitle {{
  color: rgba(255,255,255,0.5);
  font-size: 1rem;
  margin-bottom: 1.5rem;
}}
.waken-description {{
  font-size: 1.1rem;
  line-height: 1.8;
  color: rgba(255,255,255,0.7);
  max-width: 700px;
  margin: 0 auto 2rem;
  text-align: center;
}}
.waken-video-container {{
  position: relative;
  padding-top: 56.25%;
  background: linear-gradient(135deg, #0a0a0a 0%, #0a1520 100%);
  border-radius: 16px;
  overflow: hidden;
  max-width: 900px;
  margin: 0 auto 2rem;
  box-shadow: 0 20px 60px rgba(0,212,255,0.15);
  border: 1px solid rgba(0,212,255,0.2);
}}
.waken-video-container iframe {{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: none;
}}
.waken-quote {{
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-size: 1.2rem;
  color: rgba(255,255,255,0.6);
  text-align: center;
  margin-bottom: 1.5rem;
  padding: 0 2rem;
}}
.waken-positioning {{
  font-size: 0.95rem;
  color: #00D4FF;
  font-weight: 500;
  text-align: center;
  margin-bottom: 2rem;
}}
.waken-cta {{
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 14px 32px;
  font-size: 1rem;
  font-weight: 600;
  text-decoration: none;
  border-radius: 50px;
  background: linear-gradient(135deg, rgba(0,212,255,0.15), rgba(139,92,246,0.15));
  color: #00D4FF;
  border: 1px solid rgba(0,212,255,0.3);
  transition: all 0.3s ease;
}}
.waken-cta:hover {{
  background: linear-gradient(135deg, rgba(0,212,255,0.25), rgba(139,92,246,0.25));
  box-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
  transform: translateY(-2px);
}}
.waken-footer {{
  text-align: center;
  margin-top: 2rem;
}}

/* Waken Callout Mobile */
@media (max-width: 768px) {{
  .waken-callout {{
    padding: 3rem 16px;
  }}
  .waken-logo {{
    max-width: 200px;
  }}
  .waken-tagline {{
    font-size: 1.4rem;
  }}
  .waken-video-container {{
    border-radius: 0;
    margin: 0 -16px 2rem;
    max-width: calc(100% + 32px);
  }}
}}

/* AI Art Row (before Books) */
.ai-art-row {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  padding: 2rem;
  max-width: 1000px;
  margin: 0 auto;
}}
.art-video {{
  border-radius: 12px;
  overflow: hidden;
}}
.art-video iframe {{
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: 8px;
}}

/* Interviews Section */
.interviews-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1.5rem;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}}
.interview-card {{
  background: #0a0a0a;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(0,212,255,0.1);
  transition: all 0.3s ease;
}}
.interview-card:hover {{
  border-color: rgba(0,212,255,0.3);
  box-shadow: 0 0 20px rgba(0, 212, 255, 0.1);
}}
.interview-card iframe {{
  width: 100%;
  aspect-ratio: 16/9;
}}
.interview-info {{
  padding: 1rem;
}}
.interview-info h4 {{
  color: #fff;
  font-family: 'Playfair Display', serif;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}}
.interview-info p {{
  color: #888;
  font-size: 0.85rem;
}}

/* Responsive - Mobile Full Width for Video Sections */
@media (max-width: 768px) {{
  /* Hero portrait - larger on mobile */
  .hero-portrait img {{
    width: 220px;
    height: 300px;
    border-radius: 12px;
  }}
  
  /* Full width cards - NO padding, full bleed */
  .impact-card, .project-card {{
    grid-template-columns: 1fr;
    direction: ltr !important;
    padding: 0;
    gap: 0;
    margin: 0;
  }}
  .impact-card > *, .project-card > * {{
    direction: ltr !important;
  }}
  .impact-card .card-content,
  .project-card .card-content {{
    padding: 16px;
  }}
  
  /* Full width video iframes - truly edge to edge */
  .impact-card .card-video,
  .project-card .card-video,
  .innovation-card .card-video {{
    margin: 0;
    width: 100%;
  }}
  .impact-card .card-video iframe,
  .project-card .card-video iframe,
  .innovation-card .card-video iframe {{
    border-radius: 0;
  }}
  
  /* Innovation grid - full width */
  .innovation-grid {{
    grid-template-columns: 1fr;
    padding: 0;
    gap: 0;
  }}
  .innovation-card {{
    border-radius: 0;
    margin: 0;
    width: 100%;
  }}
  .innovation-card .card-content {{
    padding: 16px;
  }}
  
  /* AI Showcase full width */
  .ai-showcase {{
    grid-template-columns: 1fr;
    padding: 0;
    gap: 0;
    max-width: 100%;
  }}
  .showcase-video {{
    border-radius: 0;
  }}
  .showcase-video iframe {{
    border-radius: 0;
  }}
  
  /* Interviews grid full width */
  .interviews-grid {{
    grid-template-columns: 1fr;
    padding: 0;
    gap: 0;
    max-width: 100%;
  }}
  .interview-card {{
    border-radius: 0;
    margin: 0;
    width: 100%;
  }}
  .interview-card iframe {{
    border-radius: 0;
  }}
  .interview-info {{
    padding: 12px 16px;
  }}
  
  /* Filmography full width */
  .filmography .film-grid {{
    grid-template-columns: 1fr;
    padding: 0;
    gap: 0;
  }}
  .film-video {{
    margin: 0;
    width: 100%;
  }}
  .film-video iframe {{
    border-radius: 0;
  }}
  .film-video .video-title {{
    padding: 8px 16px;
  }}
  
  /* Playlist grid full width */
  .playlist-grid {{
    grid-template-columns: 1fr;
    padding: 0;
    gap: 0;
  }}
  .playlist-card {{
    border-radius: 0;
    margin: 0;
    width: 100%;
  }}
  
  /* Bio section padding */
  .bio-section {{
    padding: 3rem 16px;
  }}
  .bio-headline {{
    font-size: 1.8rem;
  }}
  
  /* ClineFlow padding */
  .clineflow-callout {{
    padding: 3rem 16px;
  }}
  .clineflow-title {{
    font-size: 2.5rem;
  }}
  .clineflow-features {{
    grid-template-columns: 1fr;
  }}
  
  /* Section headers - minimal padding */
  .section-header {{
    padding: 0 16px;
  }}
  
  /* Section padding */
  .section {{
    padding: 60px 0;
  }}
  
  /* AI Art Row full width */
  .ai-art-row {{
    grid-template-columns: 1fr;
    padding: 0;
    gap: 0;
    max-width: 100%;
  }}
  .art-video {{
    border-radius: 0;
    margin: 0;
    width: 100%;
  }}
  .art-video iframe {{
    border-radius: 0;
  }}
  
  /* Books/Press grids - some padding */
  .books-grid, .press-grid {{
    padding: 0 16px;
  }}
}}
  </style>
</head>
<body>

  <!-- Navigation -->
  <nav class="scroll-nav">
    <div class="nav-inner">
      {generate_nav_html()}
      <div class="hamburger" onclick="toggleMobileMenu()">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
  </nav>

  <!-- Mobile Menu Modal -->
  <div class="mobile-menu" id="mobileMenu">
    {generate_nav_html()}
  </div>

  <!-- Hero -->
  <section class="hero" id="home">
    <div class="hero-portrait">
      <img src="{IDENTITY["portrait"]}" alt="{IDENTITY["name"]}" />
    </div>
    <span class="eyebrow">{IDENTITY["status"]}</span>
    <h1>{IDENTITY["name"]}</h1>
    <p class="subtitle">{IDENTITY["title"]}</p>
    <div class="stats-row">
      {generate_stats_html()}
    </div>
  </section>

  <!-- Quote -->
  <section class="quote-section">
    <blockquote>"{IDENTITY["quote"]}"</blockquote>
    <cite>— {IDENTITY["name"]}</cite>
  </section>

  <!-- ClineFlow Featured Callout -->
  <section class="clineflow-callout" id="clineflow">
    <div class="clineflow-inner">
      <img src="{CLINEFLOW["logo"]}" alt="GitHub" class="clineflow-logo" />
      <span class="clineflow-badge">🚀 OPEN SOURCE PROJECT</span>
      <h2 class="clineflow-title">{CLINEFLOW["name"]}</h2>
      <p class="clineflow-tagline">{CLINEFLOW["tagline"]}</p>
      <p class="clineflow-subtitle">{CLINEFLOW["subtitle"]}</p>
      
      <p class="clineflow-description">{CLINEFLOW["description"]}</p>
      
      <div class="clineflow-features">
        {"".join(f'<div class="clineflow-feature"><span>{f}</span></div>' for f in CLINEFLOW["features"])}
      </div>
      
      <p class="clineflow-quote">"{CLINEFLOW["quote"]}"</p>
      
      <p class="clineflow-positioning">{CLINEFLOW["positioning"]}</p>
      
      <a href="{CLINEFLOW["github"]}" target="_blank" class="clineflow-cta">
        View on GitHub →
      </a>
      
      <span class="clineflow-stars">{CLINEFLOW["stars"]}</span>
    </div>
  </section>

  <!-- Waken AI Featured Callout -->
  <section class="waken-callout" id="waken">
    <div class="waken-inner">
      <div class="waken-header">
        <img src="{WAKEN_AI["logo"]}" alt="{WAKEN_AI["name"]}" class="waken-logo" />
        <h2 class="waken-tagline">{WAKEN_AI["tagline"]}</h2>
        <p class="waken-subtitle">{WAKEN_AI["subtitle"]}</p>
        <p class="waken-description">{WAKEN_AI["description"]}</p>
      </div>
      
      <div class="waken-video-container">
        <iframe src="{WAKEN_AI["video"]}?autoplay=0&muted=1&controls=1" 
                frameborder="0" allowfullscreen allow="autoplay"></iframe>
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

  <!-- Bio / Artist Introduction -->
  <section class="bio-section" id="about">
    <div class="bio-content">
      <h2 class="bio-headline">{BIO["headline"]}</h2>
      <p class="bio-intro">{BIO["intro"]}</p>
      
      <div class="eb1a-card">
        <h3>{BIO["eb1a_overview"]["title"]}</h3>
        <p class="eb1a-description">{BIO["eb1a_overview"]["description"]}</p>
        <ul class="eb1a-criteria">
          {"".join(f'<li>{c}</li>' for c in BIO["eb1a_overview"]["criteria_met"])}
        </ul>
      </div>
      
      <p class="bio-summary">{BIO["career_summary"]}</p>
    </div>
  </section>

  <!-- Press Quote: TechCrunch -->
  <section class="press-quote-divider">
    <blockquote>"{SECTION_QUOTES[0]["quote"]}"</blockquote>
    <div class="source">
      <a href="{SECTION_QUOTES[0]["url"]}" target="_blank" class="source-name">{SECTION_QUOTES[0]["source"]}</a>
      <span class="source-context">— {SECTION_QUOTES[0]["context"]}</span>
    </div>
  </section>

  {generate_timeline_marker("2012-2020", "Track Record")}

  <!-- Impact Section -->
  <section class="section" id="impact">
    <div class="section-header white">
      <span class="eyebrow">Proven Success</span>
      <h2>Impact & Exits</h2>
      <p class="lead">A decade of building products that reached millions and raised millions.</p>
    </div>
    
    {"".join(generate_impact_card(c) for c in HISTORIC_COMPANIES)}
  </section>

  <!-- Press Quote: Korea Biz Wire -->
  <section class="press-quote-divider">
    <blockquote>"{SECTION_QUOTES[1]["quote"]}"</blockquote>
    <div class="source">
      <a href="{SECTION_QUOTES[1]["url"]}" target="_blank" class="source-name">{SECTION_QUOTES[1]["source"]}</a>
      <span class="source-context">— {SECTION_QUOTES[1]["context"]}</span>
    </div>
  </section>

  {generate_timeline_marker("2022-2025", "AI Era")}

  <!-- AI Video Showcase -->
  <section class="section" id="ai-showcase">
    <div class="section-header">
      <span class="eyebrow">Visual AI</span>
      <h2>AI-Generated Content</h2>
    </div>
    <div class="ai-showcase" id="ai-showcase-grid">
      {generate_ai_showcase()[0]}
    </div>
    
    <!-- Show More - Hidden Videos + Playlists -->
    <div class="show-more-container">
      <button class="show-more-btn" onclick="toggleShowMore('ai-more', this)">
        Show More AI Art <span class="arrow">▼</span>
      </button>
    </div>
    <div id="ai-more" class="more-content">
      <div class="ai-showcase" style="padding-top: 0;">
        {generate_ai_showcase()[1]}
      </div>
      <div class="playlist-grid">
        <div class="playlist-card">
          <iframe src="https://www.youtube.com/embed/videoseries?list=PLU5i6V0edOss46SaZSO58FqrregrTb9WB" frameborder="0" allowfullscreen></iframe>
          <div class="playlist-info">
            <h4>AI Art Collection</h4>
            <a href="https://www.youtube.com/playlist?list=PLU5i6V0edOss46SaZSO58FqrregrTb9WB" target="_blank">View Full Playlist →</a>
          </div>
        </div>
        <div class="playlist-card">
          <iframe src="https://www.youtube.com/embed/videoseries?list=PLU5i6V0edOsvxXJq_7PMeBYudX69s_EQl" frameborder="0" allowfullscreen></iframe>
          <div class="playlist-info">
            <h4>AI Art Series 2</h4>
            <a href="https://www.youtube.com/playlist?list=PLU5i6V0edOsvxXJq_7PMeBYudX69s_EQl" target="_blank">View Full Playlist →</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Current Work -->
  <section class="section" id="work">
    <div class="section-header white">
      <span class="eyebrow">Current Focus</span>
      <h2>AI Innovation</h2>
      <p class="lead">Building the future of AI-human interaction through ethical, ergonomic technology.</p>
    </div>
    
    {"".join(generate_current_project_card(p) for p in CURRENT_PROJECTS)}
  </section>

  <!-- TwinChat Paper Callout -->
  <section class="clineflow-callout" id="twinchat-paper">
    <div class="clineflow-inner">
      <img src="{TWINCHAT_PAPER["logo"]}" alt="GitHub" class="clineflow-logo" />
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
        View on GitHub →
      </a>
      
      <span class="clineflow-stars">{TWINCHAT_PAPER["stars"]}</span>
    </div>
  </section>

  {generate_timeline_marker("2010-2020", "Innovation")}

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

  {generate_timeline_marker("2006-2010", "VFX & Film")}

  <!-- Filmography -->
  {generate_filmography_section()}

  <!-- AI Art Before Books -->
  <section class="section" id="ai-art-highlight">
    <div class="section-header">
      <span class="eyebrow">Visual Creativity</span>
      <h2>AI Art Highlights</h2>
    </div>
    <div class="ai-art-row">
      <div class="art-video">
        <iframe src="https://player.vimeo.com/video/457716566?autoplay=0&muted=1&controls=1" frameborder="0" allowfullscreen allow="autoplay"></iframe>
      </div>
      <div class="art-video">
        <iframe src="https://player.vimeo.com/video/426521636?autoplay=0&muted=1&controls=1" frameborder="0" allowfullscreen allow="autoplay"></iframe>
      </div>
    </div>
  </section>

  <!-- Books -->
  <section class="section" id="books">
    <div class="section-header white">
      <span class="eyebrow">Published Works</span>
      <h2>Books</h2>
    </div>
    <div class="books-grid">
      {generate_books_html()}
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
  <section class="section" id="press">
    <div class="section-header">
      <span class="eyebrow">Media Coverage</span>
      <h2>Press</h2>
    </div>
    <div class="press-grid">
      {generate_press_html()}
    </div>
  </section>

  <!-- Footer -->
  <footer id="contact">
    <h2>{IDENTITY["name"]}</h2>
    <p>{IDENTITY["status"]}</p>
    <a href="mailto:{IDENTITY["email"]}" class="email">{IDENTITY["email"]}</a>
    <div class="social-links">
      {generate_social_links()}
    </div>
    <p class="copyright">© 2025 Hassan Uriostegui. All rights reserved.</p>
  </footer>

  <script>
    // Scroll-synced navigation
    const sections = document.querySelectorAll('section[id], footer[id]');
    const navLinks = document.querySelectorAll('.scroll-nav a[href^="#"]');
    
    function updateNav() {{
      let current = '';
      sections.forEach(section => {{
        const rect = section.getBoundingClientRect();
        if (rect.top <= 150 && rect.bottom >= 150) {{
          current = section.id;
        }}
      }});
      
      navLinks.forEach(link => {{
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + current) {{
          link.classList.add('active');
        }}
      }});
    }}
    
    window.addEventListener('scroll', updateNav);
    updateNav();
    
    // Show More toggle function
    function toggleShowMore(contentId, btn) {{
      const content = document.getElementById(contentId);
      const isExpanded = content.classList.contains('expanded');
      
      if (isExpanded) {{
        content.classList.remove('expanded');
        btn.classList.remove('expanded');
        btn.innerHTML = 'Show More AI Art <span class="arrow">▼</span>';
      }} else {{
        content.classList.add('expanded');
        btn.classList.add('expanded');
        btn.innerHTML = 'Show Less <span class="arrow">▲</span>';
      }}
    }}
    
    // Mobile Menu Toggle
    function toggleMobileMenu() {{
      const hamburger = document.querySelector('.hamburger');
      const mobileMenu = document.getElementById('mobileMenu');
      
      hamburger.classList.toggle('active');
      mobileMenu.classList.toggle('active');
      
      // Prevent body scroll when menu is open
      if (mobileMenu.classList.contains('active')) {{
        document.body.style.overflow = 'hidden';
      }} else {{
        document.body.style.overflow = '';
      }}
    }}
    
    // Close mobile menu when clicking a link
    document.querySelectorAll('.mobile-menu a').forEach(link => {{
      link.addEventListener('click', () => {{
        const hamburger = document.querySelector('.hamburger');
        const mobileMenu = document.getElementById('mobileMenu');
        hamburger.classList.remove('active');
        mobileMenu.classList.remove('active');
        document.body.style.overflow = '';
      }});
    }});
  </script>

</body>
</html>
'''
    
    output_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "index.html")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"Portfolio generated: {output_path}")
    print(f"Total size: {len(html):,} bytes")
    return output_path


if __name__ == "__main__":
    generate_portfolio()
