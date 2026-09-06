"""Regression checks for generated page contracts and approved content access."""
import json
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'generator'))
import generate

class Document(HTMLParser):
    def __init__(self, html):
        super().__init__(); self.ids=[]; self.links=[]; self.images=[]; self.iframes=[]; self.h1=0
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='a' and 'href' in a: self.links.append(a['href'])
        if tag=='img': self.images.append(a)
        if tag=='iframe': self.iframes.append(a)
        if tag=='h1': self.h1+=1

class SiteTests(unittest.TestCase):
    def setUp(self):
        self.pages={name:generate.render_portfolio(page) for name,page in [('index.html','home'),('selected-work.html','selected-work'),('profile.html','profile')]}
        self.docs={name:Document(html) for name,html in self.pages.items()}
    def test_outputs_match_generator(self):
        for name,html in self.pages.items():
            expected='\n'.join(line.rstrip() for line in html.splitlines())+'\n'
            self.assertEqual((ROOT/name).read_text(),expected,name)
    def test_page_landmarks_and_anchors(self):
        for name,doc in self.docs.items():
            self.assertEqual(doc.h1,1,name)
            self.assertEqual(len(doc.ids),len(set(doc.ids)),name)
            for href in doc.links:
                if href.startswith('#'): self.assertIn(href[1:],doc.ids,href)
                elif '.html#' in href and not href.startswith('http'):
                    route,anchor=href.split('#'); self.assertIn(anchor,self.docs[route].ids,href)
    def test_existing_content_destinations_preserved(self):
        approved_removed_ids={'sendkarma','professional-profile'}
        relocated_media_ids={'press','interviews'}
        approved_removed_destinations={'https://www.sendkarma.app/','https://player.vimeo.com/video/1138631992'}
        relocated_profile_ids={'resumeCanvas','resumeCanvasWrap','resumeNext','resumePageIndicator','resumePreview','resumePrevious','resumeStatus','resumeZoomIn','resumeZoomOut'}
        resume_pdf='assets/hassan-uriostegui-resume-2026-12.pdf'
        profile_doc=self.docs['profile.html']
        self.assertTrue(relocated_profile_ids.issubset(set(profile_doc.ids)))
        self.assertIn(resume_pdf,profile_doc.links)
        for name,doc in self.docs.items():
            if name == 'profile.html':
                continue
            baseline=Document(subprocess.check_output(['git','show',f'7e34a70:{name}'],cwd=ROOT,text=True))
            baseline_ids=set(baseline.ids)-approved_removed_ids
            if name == 'index.html':
                baseline_ids-=relocated_profile_ids
                baseline_ids-=relocated_media_ids
            self.assertTrue(baseline_ids.issubset(set(doc.ids)),name)
            baseline_destinations={h for h in baseline.links if not h.startswith('#')}-approved_removed_destinations
            baseline_destinations.discard('index.html#press')
            if name == 'index.html':
                baseline_destinations.discard(resume_pdf)
                baseline_destinations -= {item['url'] for item in generate.PRESS}
                # Innovations was removed from the home highlights by request.
                baseline_destinations.discard('selected-work.html#research')
            baseline_destinations.discard('index.html#professional-profile')
            self.assertTrue(baseline_destinations.issubset(set(doc.links)),baseline_destinations-set(doc.links))
    def test_resume_page_and_media_contract(self):
        home=self.pages['index.html']
        profile=self.pages['profile.html']
        self.assertNotIn('id="professional-profile"',home)
        self.assertLess(home.index('class="selected-work-gateway"'),home.index('id="clineflow"'))
        self.assertIn('id="professional-profile"',profile)
        self.assertIn('id="resumeCanvas"',profile)
        self.assertNotIn('id="clineflow"',profile)
        self.assertIn('id="contact"',profile)
        self.assertIn("location.replace('profile.html');",generate.INTERACTION_SCRIPT)
        self.assertNotIn('id="resumeCanvas"',self.pages['selected-work.html'])
        for doc in self.docs.values():
            for iframe in doc.iframes:
                self.assertTrue(iframe.get('title'))
                self.assertEqual(iframe.get('loading'),'lazy')
    def test_desktop_navigation_and_home_portfolio_placement(self):
        home=self.pages['index.html']
        header=home[home.index('<header'):home.index('</header>')]
        expected=[
            ('Resume',generate.PROFILE_PAGE), ('Agentic AI','#clineflow'),
            ('Mobile Apps','#memearcade'), ('Citations','#citations'), ('Books','#books'),
            ('Press',f'{generate.PROFILE_PAGE}#press'), ('Sparks',f'{generate.SELECTED_WORK_PAGE}#selected-work'),
        ]
        positions=[header.index(f'href="{href}">{label}') for label,href in expected]
        self.assertEqual(positions,sorted(positions))
        self.assertIn(f'href="{generate.CLINEFLOW["website"]}" target="_blank" rel="noopener noreferrer" class="desktop-clineflow"',header)
        self.assertIn('ClineFlow <span aria-hidden="true">↗</span>',header)
        self.assertIn(f'href="{generate.SELECTED_WORK_PAGE}#selected-work">Sparks</a>',header)
        self.assertIn(f'href="{generate.SELECTED_WORK_PAGE}#selected-work">SPARKS</a>',home)
        self.assertIn('Prompt Engineering',home)
        self.assertNotIn('TwinChat Paper',home)
        self.assertIn('<h2 id="selected-work-title">Explore Sparks</h2>',home)
        self.assertLess(home.index('Agentic &amp; Open Source'),home.index('AI Context Engineering'))
        self.assertLess(home.index('AI Context Engineering'),home.index('Prompt Engineering'))
        self.assertNotIn('Agentic Products &amp; Tools', home)
        self.assertIn('AI SYSTEMS',home)
        self.assertRegex(home, 'href="selected-work.html#ios-open-source" class="selected-work-link">.*?<span class="sparks-label">iOS &amp; Open Source</span>')
        self.assertRegex(home, 'href="selected-work.html#casual-books" class="selected-work-link">.*?<span class="sparks-label">Writing About Trends</span>')
        self.assertIn(generate.generate_selected_work_grid("selected-work").strip(), self.pages['selected-work.html'])
        self.assertNotIn('<nav class="work-index"', self.pages['selected-work.html'])
        self.assertRegex(home, 'href="#clineflow" class="selected-work-link selected-work-link--ai">.*?<span class="sparks-label">AI Context Engineering</span>')
        self.assertRegex(self.pages['selected-work.html'], 'href="index.html#clineflow" class="selected-work-link selected-work-link--ai">.*?<span class="sparks-label">AI Context Engineering</span>')
        self.assertNotIn('selected-work-link--external',home)
    def test_ultrakam_exit_card_and_coverage(self):
        work=self.pages['selected-work.html']
        self.assertLess(work.index('id="viddy"'),work.index('id="ultrakam"'))
        self.assertLess(work.index('id="ultrakam"'),work.index('id="flyr"'))
        self.assertIn('https://www.youtube.com/embed/jqs6dXF9wDU',work)
        self.assertIn('style="--video-ratio: 200 / 150"',work)
        self.assertIn('Apple’s WWDC14 feature on Medium',work)
        self.assertEqual({company['name'] for company in generate.HISTORIC_COMPANIES if company.get('exit')},{'Viddy','Ultrakam','FlyrTV'})

    def test_center_interview_uses_the_ultrakam_video(self):
        profile = self.pages['profile.html']
        center_card = profile.split('class="interview-card"')[2]
        third_card = profile.split('class="interview-card"')[3]
        self.assertIn('https://www.youtube.com/embed/jqs6dXF9wDU', center_card)
        self.assertIn('style="--video-ratio: 200 / 150"', center_card)
        self.assertIn('https://player.vimeo.com/video/843499496', third_card)

    def test_ai_native_style_variant_uses_modern_type_and_warm_indigo_tokens(self):
        home = self.pages['index.html']
        self.assertIn('family=DM+Sans', home)
        self.assertIn('family=Space+Grotesk', home)
        self.assertIn('--ink: #0a091b;', home)
        self.assertIn('--sunset: #ffd09c;', home)

    def test_current_projects_follow_the_requested_sequence(self):
        work=self.pages['selected-work.html']
        self.assertLess(work.index('id="brb2me"'),work.index('id="newsmusic"'))
        self.assertLess(work.index('id="newsmusic"'),work.index('id="lyrics-refiner"'))
        self.assertLess(work.index('id="lyrics-refiner"'),work.index('id="kie-api"'))
        self.assertLess(work.index('id="kie-api"'),work.index('id="btwinfriends"'))
        self.assertLess(work.index('id="btwinfriends"'),work.index('id="twinchat"'))
        self.assertIn('href="https://github.com/hassanvfx/newsmusic"',work)
        self.assertIn('href="https://github.com/hassanvfx/lyrics-refiner"',work)
        self.assertIn('href="https://github.com/hassanvfx/kie-api-python"',work)
        for image_key in ('newsmusic-hero','lyrics-refiner-hero','kie-api-hero'):
            self.assertIn(generate.IMAGE_MANIFEST[image_key]['url'],work)
        self.assertIn('View on GitHub',work)
        self.assertIn('An early exploration of cognitive profiling and conversational AI companions.',work)
        self.assertNotIn('The predecessor to modern AI mind simulation.',work)
    def test_spreeai_valuation_and_coverage(self):
        work=self.pages['selected-work.html']
        self.assertIn('$1.5B Valuation · 2026',work)
        self.assertIn('PR Newswire: $1.5B valuation',work)
        self.assertNotIn('Naomi Campbell Board Member | AI Fashion',work)

    def test_positioning_prefers_supported_evidence(self):
        home = self.pages['index.html']
        self.assertIn('EB-1A · EXTRAORDINARY ABILITY', home)
        self.assertIn('40M+', home)
        self.assertIn('Users Reached', home)
        self.assertIn('$6M+', home)
        self.assertIn('Raised as Co-Founder', home)
        self.assertNotIn('0.1% of visa applicants', home)
        self.assertNotIn('granted U.S. Citizenship through the EB1A category', home)

    def test_home_books_are_followed_by_the_technical_writing_bridge(self):
        home = self.pages['index.html']
        self.assertLess(home.index('id="books"'), home.index('class="writing-sparks-callout"'))
        self.assertLess(home.index('class="writing-sparks-callout"'), home.index('id="about"'))
        self.assertIn('href="selected-work.html#technical-writing">More Technical Writing', home)

    def test_home_clineflow_is_followed_by_the_ai_sparks_bridge(self):
        home = self.pages['index.html']
        self.assertLess(home.index('id="clineflow"'), home.index('class="ai-sparks-callout"'))
        self.assertLess(home.index('class="ai-sparks-callout"'), home.index('id="memearcade"'))
        self.assertIn('href="selected-work.html#work">More AI Sparks', home)
        self.assertIn('href="selected-work.html#ios-open-source">More iOS Sparks', home)
        self.assertIn('id="ai-sparks-heading" class="sparks-callout-title"><span class="sparks-callout-icon">', home)
        self.assertIn('id="ios-sparks-heading" class="sparks-callout-title"><span class="sparks-callout-icon">', home)
        self.assertIn('id="writing-sparks-heading" class="sparks-callout-title"><span class="sparks-callout-icon">', home)

    def test_book_covers_link_to_their_product_pages(self):
        home = self.pages['index.html']
        self.assertIn('href="https://www.lulu.com/shop/hassan-uriostegui/ai-from-tensors-to-agents-on-mac-silicon/hardcover/product-e7qy7gy.html?page=1&pageSize=4" target="_blank" rel="noopener noreferrer" class="book-cover-link"', home)
        self.assertIn('href="https://www.lulu.com/shop/hassan-uriostegui/modern-ios-architecture-deconstructing-the-3b-memearcade/hardcover/product-yvewn4y.html?page=1&pageSize=4" target="_blank" rel="noopener noreferrer" class="book-cover-link"', home)

    def test_swift_foundations_are_an_ios_open_source_chapter_on_sparks(self):
        home=self.pages['index.html']
        work=self.pages['selected-work.html']
        self.assertNotIn('<section class="home-tooling-showcase"', home)
        self.assertIn('id="ios-open-source"', work)
        self.assertLess(work.index('id="work"'), work.index('id="ios-open-source"'))
        self.assertLess(work.index('id="twinchat-paper"'), work.index('id="ios-open-source"'))
        self.assertLess(work.index('id="ios-open-source"'), work.index('id="research"'))
        self.assertLess(work.index('id="swift-spm"'), work.index('id="datastore"'))
        self.assertLess(work.index('id="datastore"'), work.index('id="webview-swiftui"'))
        self.assertIn('href="https://github.com/hassanvfx/ios-framework"',work)
        self.assertIn('href="https://github.com/hassanvfx/ios-storage"',work)
        self.assertIn('href="https://github.com/hassanvfx/ios-webViewSwiftUI"',work)
        self.assertIn('"@type":"SoftwareSourceCode"',work)
        self.assertIn('"codeRepository":"https://github.com/hassanvfx/ios-webViewSwiftUI"',work)
        for image_key in ('swift-spm-hero','datastore-hero','webview-swiftui-hero'):
            self.assertIn(generate.IMAGE_MANIFEST[image_key]['url'],work)
    def test_sitemap_contains_every_canonical_page_and_publishing_metadata(self):
        sitemap = (ROOT / 'sitemap.xml').read_text()
        for page in ('', generate.SELECTED_WORK_PAGE, generate.PROFILE_PAGE):
            self.assertIn(f'<loc>{generate.SITE_URL}/{page}</loc>', sitemap)
        self.assertEqual(sitemap.count('<url>'), 3)
        self.assertEqual(sitemap.count(f'<lastmod>{generate.SITE_LAST_MODIFIED}</lastmod>'), 3)
        self.assertIn('<changefreq>weekly</changefreq>', sitemap)

    def test_chapter_returns_target_the_current_page_menu(self):
        for name in ('index.html', 'selected-work.html'):
            doc = self.docs[name]
            self.assertEqual(doc.ids.count('explore-sparks'), 1)
            self.assertGreater(doc.links.count('#explore-sparks'), 0)
            self.assertIn('id="explore-sparks" tabindex="-1"', self.pages[name])
            self.assertNotIn('index.html#explore-sparks', doc.links)
            self.assertNotIn('selected-work.html#explore-sparks', doc.links)
        profile = self.pages['profile.html']
        self.assertEqual(self.docs['profile.html'].ids.count('explore-sparks'), 1)
        self.assertLess(profile.index('id="professional-profile"'), profile.index('id="explore-sparks"'))
        self.assertIn('href="index.html#clineflow" class="selected-work-link selected-work-link--ai"', profile)
        self.assertIn('href="selected-work.html#technical-writing" class="selected-work-link"', profile)

    def test_technical_writing_navigation_and_articles(self):
        from html import escape
        work = self.pages['selected-work.html']
        self.assertIn('selected-work.html#technical-writing', self.docs['index.html'].links)
        self.assertIn('#technical-writing', self.docs['selected-work.html'].links)
        self.assertLess(work.index('id="technical-writing"'), work.index('id="ios-open-source"'))
        self.assertEqual(len(generate.TECHNICAL_WRITING), 5)
        for article in generate.TECHNICAL_WRITING:
            self.assertIn(article['url'], self.docs['selected-work.html'].links)
            self.assertIn(escape(article['title']), work)
            self.assertIn(article['id'], self.docs['selected-work.html'].ids)
            image = next(image for image in self.docs['selected-work.html'].images
                         if image['src'] == generate.IMAGE_MANIFEST[article['id']]['url'])
            self.assertEqual(image.get('loading'), 'lazy')
            self.assertIn('width', image)
            self.assertIn('height', image)

    def test_sendkarma_is_not_rendered(self):
        for page in self.pages.values():
            self.assertNotIn('SendKarma',page)
            self.assertNotIn('sendkarma',page)
    def test_press_and_interviews_follow_explore_sparks_on_resume(self):
        home=self.pages['index.html']
        profile=self.pages['profile.html']
        self.assertNotIn('id="press"',home)
        self.assertNotIn('id="interviews"',home)
        self.assertLess(profile.index('id="explore-sparks"'),profile.index('id="press"'))
        self.assertLess(profile.index('id="press"'),profile.index('id="interviews"'))
        self.assertIn('profile.html#press', home)
    def test_image_budgets_and_responsive_assets(self):
        # Editorial photography has its own allowance: new article covers must
        # not force existing book imagery below its display resolution.
        trend_urls = {generate.IMAGE_MANIFEST[book['image']]['url'] for book in generate.BOOKS[2:]}
        for name,budget in [('index.html',1450000),('selected-work.html',360000)]:
            urls = {im['src'] for im in self.docs[name].images}
            if name == 'selected-work.html':
                urls -= trend_urls
            total=sum((ROOT/url).stat().st_size for url in urls)
            self.assertLessEqual(total,budget)
        self.assertLessEqual(sum((ROOT/url).stat().st_size for url in trend_urls), 600000)
        portrait=next(im for im in self.docs['index.html'].images if im.get('fetchpriority')=='high')
        self.assertIn('srcset',portrait)
        self.assertLessEqual((ROOT/portrait['src']).stat().st_size,150000)
    def test_trend_images_keep_square_high_resolution_sources(self):
        for book in generate.BOOKS[2:]:
            asset = generate.IMAGE_MANIFEST[book['image']]
            self.assertGreaterEqual(asset['width'], 660)
            self.assertEqual(asset['width'], asset['height'])
            image = next(im for im in self.docs['selected-work.html'].images if im['src'] == asset['url'])
            self.assertIn('660w', image['srcset'])
            self.assertIn('440w', image['srcset'])
            self.assertIn('520px', image['sizes'])
            self.assertEqual(image['loading'], 'lazy')

    def test_provider_video_dimensions(self):
        for doc in self.docs.values():
            for iframe in doc.iframes:
                metadata=generate.VIDEO_METADATA[iframe['src']]
                self.assertEqual(int(iframe['width']),metadata['width'])
                self.assertEqual(int(iframe['height']),metadata['height'])
        for video_id in ('839937602','1005370651'):
            video=generate.VIDEO_METADATA[f'https://player.vimeo.com/video/{video_id}']
            self.assertEqual(video['width'],video['height'])
    def test_carousel_progressive_fallback(self):
        html=self.pages['index.html']
        self.assertEqual(html.count('aria-roledescription="slide"'),3)
        self.assertIn('class="carousel-controls" hidden',html)
        self.assertNotIn('particle-field',html)
        self.assertNotIn('booking-call-bar"',html)

if __name__=='__main__': unittest.main()
