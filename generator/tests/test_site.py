"""Regression tests for the route registry and central portfolio catalog."""
from html.parser import HTMLParser
from pathlib import Path
import sys
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "generator"))
import generate
from content_catalog import GITHUB_REPOSITORIES, GITHUB_REPOSITORY_SNAPSHOT, MOBILE_APP_ICON_WALL, NAVIGATION, PAGE_COMPOSITIONS, PROJECTS, SITE_PAGES


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.ids, self.links, self.images, self.h1 = [], [], [], 0
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "img":
            self.images.append(attrs)
        if tag == "h1":
            self.h1 += 1


class SiteTests(unittest.TestCase):
    def setUp(self):
        self.routes = {"index.html": "home", **{meta["path"]: page for page, meta in SITE_PAGES.items() if page != "home"}, "selected-work.html": "selected-work"}
        self.pages = {name: generate.render_portfolio(page) for name, page in self.routes.items()}
        self.docs = {name: Document(page) for name, page in self.pages.items()}

    def test_outputs_match_generator(self):
        for name, html in self.pages.items():
            expected = "\n".join(line.rstrip() for line in html.splitlines()) + "\n"
            self.assertEqual((ROOT / name).read_text(), expected, name)

    def test_routes_have_one_heading_unique_ids_and_local_anchors(self):
        for name, document in self.docs.items():
            self.assertEqual(document.h1, 1, name)
            self.assertEqual(len(document.ids), len(set(document.ids)), name)
            for href in document.links:
                if href.startswith("#"):
                    self.assertIn(href[1:], document.ids, f"{name}: {href}")
                elif ".html#" in href and not href.startswith("http"):
                    route, anchor = href.split("#", 1)
                    self.assertIn(anchor, self.docs[route].ids, f"{name}: {href}")

    def test_navigation_is_shared_and_uses_canonical_pages(self):
        for page_name, page in self.pages.items():
            current_page = self.routes[page_name]
            header = page[page.index("<header"):page.index("</header>")]
            for label, target in NAVIGATION:
                expected = (f'<a class="nav-link is-current" href="{generate.page_href(target)}" aria-current="page">{label}</a>'
                            if target == current_page else f'<a class="nav-link" href="{generate.page_href(target)}">{label}</a>')
                self.assertIn(expected, header)
            self.assertIn('<a class="desktop-clineflow" href="https://clineflow.com/" target="_blank" rel="noopener noreferrer">ClineFlow <span aria-hidden="true">↗</span></a>', header)
            if current_page == "home":
                self.assertIn('<a class="nav-link is-current" href="index.html" aria-current="page">Home</a>', page)
            self.assertIn("Book a call", page)
            self.assertNotIn(">Sparks<", page)
            self.assertNotIn("Explore Sparks", page)

    def test_home_uses_the_requested_editorial_sequence(self):
        home = self.pages["index.html"]
        self.assertLess(home.index('id="clineflow"'), home.index('id="ai-copyright-weights"'))
        self.assertLess(home.index('id="ai-copyright-weights"'), home.index('id="memearcade"'))
        self.assertLess(home.index('id="memearcade"'), home.index('id="wwdc14"'))
        self.assertLess(home.index('id="wwdc14"'), home.index('id="books"'))
        self.assertNotIn('id="citations"', home)
        self.assertIn('>More Agentic AI<', home)
        self.assertIn('href="agentic-ai.html#projects">More Agentic AI', home)
        self.assertIn('>More Mobile Apps<', home)
        self.assertIn('href="mobile-apps.html#projects">More Mobile Apps', home)

    def test_resume_places_evidence_after_eb1a(self):
        profile = self.pages["profile.html"]
        self.assertLess(profile.index('id="eb1a"'), profile.index('id="citations"'))
        self.assertLess(profile.index('id="citations"'), profile.index('id="explore-work"'))
        self.assertLess(profile.index('id="explore-work"'), profile.index('id="press"'))
        self.assertIn('Bipartisan House Task Force', profile)
        self.assertNotIn('id="earlier-work"', profile)
        self.assertIn('Engineering AI-Native Products and Mobile Systems', profile)

    def test_topic_pages_resolve_from_the_catalog(self):
        agentic = self.pages["agentic-ai.html"]
        mobile = self.pages["mobile-apps.html"]
        github = self.pages["github.html"]
        startups = self.pages["startups.html"]
        books = self.pages["books.html"]
        self.assertIn("ClineFlow", agentic)
        self.assertIn(generate.IMAGE_MANIFEST["infinite-ai-context-cover"]["url"], agentic)
        self.assertIn('class="video-frame video-frame--square-preview"', agentic)
        self.assertIn('class="video-frame video-frame--square-preview"', mobile)
        self.assertIn(generate.IMAGE_MANIFEST["github-terminal-hero"]["url"], github)
        self.assertIn('class="topic-hero-action" href="https://github.com/hassanvfx"', github)
        self.assertIn('>Open GitHub ', github)
        self.assertIn('topic-hero-art--press-loop', startups)
        for press_logo in generate.PRESS_LOGOS:
            self.assertIn(generate.IMAGE_MANIFEST[press_logo["logo"]]["url"], startups)
        self.assertIn('topic-hero-art--square-image', books)
        self.assertIn(generate.IMAGE_MANIFEST["three-technical-books-hero"]["url"], books)
        self.assertIn("AI-Copyright Weights", agentic)
        for tool in ("SwiftSPM", "DataStore", "WebViewSwiftUI", "SUIPlayer"):
            self.assertIn(tool, mobile)
        self.assertIn("ios-suiplayer", mobile)
        self.assertIn("Meme Arcade", mobile)
        self.assertIn(generate.IMAGE_MANIFEST["meme-arcade-product-panels"]["url"], mobile)
        self.assertNotIn(generate.IMAGE_MANIFEST["meme-arcade-play"]["url"], re.search(r'<article class="startup-case .*?id="meme-arcade-project".*?</article>', mobile, re.S).group(0))
        self.assertIn("Ultrakam", mobile)
        self.assertLess(mobile.index('id="writing-wwdc14"'), mobile.index('id="writing-demystify-swiftui"'))
        self.assertIn('https://www.youtube.com/embed/L8ljk21Oyx0', mobile)
        self.assertIn("KIE CLI &amp; MCP", agentic)
        self.assertLess(agentic.index('id="ai-copyright-weights-feature"'), agentic.index('id="articles"'))
        self.assertIn("Read the TwinChat paper", agentic)
        self.assertIn("https://hassanvfx.github.io/twinchat-paper/", agentic)
        self.assertIn("Read Mind Simulation Technology", agentic)
        self.assertIn("https://www.amazon.com/-/he/Hassan-Uriostegui/dp/1304332993", agentic)
        self.assertNotIn("Read the TwinChat paper", mobile)
        self.assertNotIn("Read Mind Simulation Technology", mobile)
        agentic_btwin = re.search(r'<article class="startup-case .*?id="btwinfriends-project".*?</article>', agentic, re.S).group(0)
        mobile_btwin = re.search(r'<article class="startup-case .*?id="btwinfriends-project".*?</article>', mobile, re.S).group(0)
        self.assertIn("Model orchestration", agentic_btwin)
        self.assertIn("Native product delivery", mobile_btwin)
        self.assertNotIn("SwiftUI", agentic_btwin)
        agentic_twinchat = re.search(r'<article class="startup-case .*?id="twinchat-project".*?</article>', agentic, re.S).group(0)
        mobile_twinchat = re.search(r'<article class="startup-case .*?id="twinchat-project".*?</article>', mobile, re.S).group(0)
        self.assertIn("Behavioral constraints", agentic_twinchat)
        self.assertIn("Character catalog", mobile_twinchat)
        clineflow_case = re.search(r'<article class="startup-case .*?id="clineflow-project".*?</article>', agentic, re.S).group(0)
        open_knowledge = re.search(r'<li class="startup-highlight">.*?<h4>Open knowledge format</h4>.*?</li>', clineflow_case, re.S).group(0)
        self.assertIn('href="https://hassanvfx.github.io/infinite-ai-context/downloads/infinite-ai-context-web.pdf"', open_knowledge)
        self.assertIn('>Free ClineFlow ebook ', open_knowledge)
        versioned_context = re.search(r'<li class="startup-highlight">.*?<h4>Code and context together</h4>.*?</li>', clineflow_case, re.S).group(0)
        self.assertIn('href="https://github.com/hassanvfx/clineflow"', versioned_context)
        self.assertIn('>ClineFlow repository ', versioned_context)
        portable_context = re.search(r'<li class="startup-highlight">.*?<h4>An open file contract</h4>.*?</li>', clineflow_case, re.S).group(0)
        self.assertIn('https://www.lulu.com/shop/hassan-uriostegui/infinite-ai-context-clineflow-and-googles-open-knowledge-format/paperback/product-rmkn8jg.html?page=1&amp;pageSize=4', portable_context)
        self.assertIn('>ClineFlow printed edition ', portable_context)
        self.assertIn('>Lulu book<', portable_context)
        self.assertIn('assets/securevault-article.31b5ce774972.webp', mobile)
        self.assertIn('assets/swiftwallet-article.ddec4a2b6a9e.webp', mobile)

    def test_mobile_hero_indexes_the_career_app_catalog(self):
        mobile = self.pages["mobile-apps.html"]
        self.assertIn('class="mobile-app-wall"', mobile)
        for item in MOBILE_APP_ICON_WALL:
            self.assertIn(item.get("label") or generate.entity_name(PROJECTS[item["project_id"]]), mobile)
            if item.get("image"):
                self.assertIn(generate.IMAGE_MANIFEST[item["image"]]["url"], mobile)
        for image_key in ("meme-arcade-wall-icon", "spreeai-wall-icon", "btwin-wall-icon", "twinchat-wall-icon", "community-wall-icon", "ultrakam-wall-icon", "flyrtv-wall-icon", "viddy-wall-icon"):
            self.assertIn(generate.IMAGE_MANIFEST[image_key]["url"], mobile)

    def test_app_icons_follow_matching_products_across_topic_pages(self):
        expected = {
            "agentic-ai.html": ("btwinfriends", "twinchat"),
            "startups.html": ("ultrakam", "flyr", "viddy", "spreeai", "community"),
        }
        for page_name, project_ids in expected.items():
            page = self.pages[page_name]
            for project_id in project_ids:
                asset = generate.mobile_app_icon_asset(project_id)
                self.assertIsNotNone(asset)
                case = re.search(rf'<article class="startup-case .*?id="{project_id}-(?:project|company|exit)".*?</article>', page, re.S).group(0)
                self.assertIn(generate.IMAGE_MANIFEST[asset]["url"], case)

    def test_topic_cards_keep_their_visual_media(self):
        for page_name in ("books.html", "github.html"):
            page = self.pages[page_name]
            rows = re.findall(r'<article class="home-tooling-project portfolio-row.*?</article>', page, re.S)
            self.assertTrue(rows, page_name)
            for row in rows:
                self.assertIn('class="home-tooling-copy"', row)
                self.assertIn('class="home-tooling-visual"', row)
                self.assertRegex(row, r'<(?:img|iframe) ')
            self.assertNotIn('class="showcase-deck"', page)
            for group in re.findall(r'<div class="portfolio-rows">(.*?)</section>', page, re.S):
                classes = re.findall(r'<article class="([^"]+)"', group)
                for index, names in enumerate(classes):
                    self.assertEqual('home-tooling-project--reverse' in names, index % 2 == 0)
        self.assertIn('id="repo-kie-api-python-featured"', self.pages["github.html"])
        self.assertIn('KIE CLI &amp; MCP', self.pages["github.html"])

    def test_topic_projects_use_technical_case_studies(self):
        for page_name, composition_id in (("agentic-ai.html", "agentic-ai"), ("mobile-apps.html", "mobile-apps")):
            page = self.pages[page_name]
            cases = re.findall(r'<article class="startup-case .*?</article>', page, re.S)
            self.assertEqual(len(cases), len(PAGE_COMPOSITIONS[composition_id]["projects"]))
            for case in cases:
                self.assertIn("Technical contribution", case)
                self.assertIn('class="startup-case-media"', case)
                self.assertIn('class="startup-highlights"', case)
                self.assertIn('class="startup-source"', case)
                self.assertEqual(len(re.findall(r'<li class="startup-highlight">.*?</li>', case, re.S)), 4)

    def test_startup_cases_attribute_contributions_and_company_outcomes(self):
        page = self.pages["startups.html"]
        cases = re.findall(r'<article class="startup-case .*?</article>', page, re.S)
        self.assertEqual(len(cases), 6)
        for case in cases:
            self.assertIn('My contribution', case)
            self.assertRegex(case, r'<(?:img|iframe) ')
            highlights = re.findall(r'<li class="startup-highlight">.*?</li>', case, re.S)
            self.assertEqual(len(highlights), 4)
            for highlight in highlights:
                self.assertIn('class="startup-source"', highlight)
                self.assertIn('startup-source-kind', highlight)
        self.assertIn('Later company milestone', page)
        self.assertIn('Announced in May 2025, after my Dec 2020–Apr 2023 role.', page)
        self.assertIn('Company release', page)
        self.assertIn('Founder interview', page)
        self.assertIn('Career record', page)
        self.assertNotIn('Jabali', page)
        self.assertLess(page.index('id="press-releases"'), page.index('id="press"'))
        self.assertLess(page.index('id="press"'), page.index('id="interviews"'))

    def test_startup_counters_keep_company_milestones(self):
        hero = re.search(r'<section class="startup-hero-stats".*?</section>', self.pages["startups.html"], re.S).group(0)
        self.assertIn('class="stats-row"', hero)
        self.assertEqual(re.findall(r'<div class="value">(.*?)</div>', hero), ["$1.5B", "10M+", "$6M", "40M+"])
        self.assertEqual(len(re.findall('class="startup-counter-source"', hero)), 4)

    def test_case_sources_stay_beneath_facts(self):
        for page_name in ("startups.html", "agentic-ai.html", "mobile-apps.html"):
            page = self.pages[page_name]
            self.assertNotIn('class="case-sources"', page)
            self.assertNotIn('class="case-reference"', page)
            for highlight in re.findall(r'<li class="startup-highlight">.*?</li>', page, re.S):
                self.assertIn('class="startup-source"', highlight)
                self.assertNotRegex(highlight, r'href="#.*?-source-')
        # Established products have separate supporting records for all four facts.
        for project_id, case in generate.STARTUP_CASES.items():
            urls = {generate.STARTUP_SOURCES[item["source"]]["url"] for item in case["highlights"]}
            self.assertEqual(len(urls), 4, project_id)

    def test_github_is_the_previous_portfolio_collection(self):
        github = self.pages["github.html"]
        self.assertEqual(len(GITHUB_REPOSITORIES), 7)
        for repo in GITHUB_REPOSITORY_SNAPSHOT:
            name = repo["name"]
            self.assertIn(f"https://github.com/hassanvfx/{name}", github)
            self.assertIn(repo["language"], github)
            self.assertIn(repo["description"], github)
            if repo["license"]:
                self.assertIn(f'{repo["license"]} license', github)
        self.assertNotIn("Nuke-Cloudlight-Plugin", github)
        self.assertNotIn("ios-suiplayer", github)

    def test_seo_registry_and_legacy_page(self):
        sitemap = (ROOT / "sitemap.xml").read_text()
        indexable_pages = [meta for meta in SITE_PAGES.values() if meta.get("indexable", True)]
        self.assertEqual(sitemap.count("<url>"), len(indexable_pages))
        for meta in indexable_pages:
            self.assertIn(f'<loc>{generate.SITE_URL}/{meta["path"]}</loc>', sitemap)
            self.assertIn(f'<priority>{meta["priority"]}</priority>', sitemap)
            self.assertIn(f'<changefreq>{meta["changefreq"]}</changefreq>', sitemap)
        robots = (ROOT / "robots.txt").read_text()
        self.assertIn(f"Sitemap: {generate.SITE_URL}/sitemap.xml", robots)

        for page_name, page in self.pages.items():
            page_id = self.routes[page_name]
            metadata = generate.get_page_metadata(page_id)
            canonical = f'{generate.SITE_URL}/{metadata["path"]}'
            image = generate.metadata_image(metadata)
            self.assertIn(f'<link rel="canonical" href="{canonical}">', page)
            self.assertIn(f'<meta property="og:image" content="{generate.SITE_URL}/{image["url"]}">', page)
            self.assertIn(f'<meta name="twitter:image" content="{generate.SITE_URL}/{image["url"]}">', page)
            payload = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', page).group(1))
            graph = payload["@graph"]
            page_node = next(node for node in graph if node.get("@id") == canonical)
            self.assertEqual(page_node["@type"], metadata["schema_type"])
            self.assertEqual(page_node["primaryImageOfPage"]["url"], f'{generate.SITE_URL}/{image["url"]}')
            self.assertTrue(any(node.get("@type") == "BreadcrumbList" for node in graph))
            if metadata["schema_type"] == "CollectionPage" and page_id != "selected-work":
                self.assertTrue(any(node.get("@type") == "ItemList" for node in graph))

        legacy = self.pages["selected-work.html"]
        self.assertIn('content="noindex, follow"', legacy)
        self.assertIn("Explore My Work", legacy)
        self.assertIn("legacyHashRoutes", generate.INTERACTION_SCRIPT)
        self.assertIn("'sparks': 'index.html#explore-work'", generate.INTERACTION_SCRIPT)

    def test_manifest_images_remain_intrinsic(self):
        urls = {entry["url"] for entry in generate.IMAGE_MANIFEST.values()}
        for page in self.pages.values():
            for image in Document(page).images:
                self.assertIn(image["src"], urls)
                self.assertIn("width", image)
                self.assertIn("height", image)
                self.assertEqual(image.get("decoding"), "async")


if __name__ == "__main__":
    unittest.main()
