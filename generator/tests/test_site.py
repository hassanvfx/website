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
        self.pages={name:generate.render_portfolio(page) for name,page in [('index.html','home'),('selected-work.html','selected-work')]}
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
        for name,doc in self.docs.items():
            baseline=Document(subprocess.check_output(['git','show',f'7e34a70:{name}'],cwd=ROOT,text=True))
            self.assertTrue(set(baseline.ids).issubset(set(doc.ids)),name)
            baseline_destinations={h for h in baseline.links if not h.startswith('#')}
            self.assertTrue(baseline_destinations.issubset(set(doc.links)),baseline_destinations-set(doc.links))
    def test_resume_priority_and_media_contract(self):
        home=self.pages['index.html']
        self.assertLess(home.index('id="professional-profile"'),home.index('id="clineflow"'))
        self.assertNotIn('id="resumeCanvas"',self.pages['selected-work.html'])
        for doc in self.docs.values():
            for iframe in doc.iframes:
                self.assertTrue(iframe.get('title'))
                self.assertEqual(iframe.get('loading'),'lazy')
    def test_desktop_navigation_and_home_portfolio_placement(self):
        home=self.pages['index.html']
        header=home[home.index('<header'):home.index('</header>')]
        expected=[
            ('Profile','#professional-profile'), ('AI coding','#clineflow'),
            ('Apps','#memearcade'), ('Citations','#citations'), ('Books','#books'),
            ('Press','#press'), ('Sparks',f'{generate.SELECTED_WORK_PAGE}#selected-work'),
        ]
        positions=[header.index(f'href="{href}">{label}') for label,href in expected]
        self.assertEqual(positions,sorted(positions))
        self.assertIn(f'href="{generate.CLINEFLOW["website"]}" target="_blank" rel="noopener noreferrer" class="desktop-clineflow"',header)
        self.assertIn('ClineFlow <span aria-hidden="true">↗</span>',header)
        self.assertIn(f'href="{generate.SELECTED_WORK_PAGE}#selected-work">Sparks</a>',header)
        self.assertIn(f'href="{generate.SELECTED_WORK_PAGE}#selected-work">SPARKS</a>',home)
        self.assertLess(home.index('<section class="quote-section">'),home.index('class="selected-work-gateway"'))
        self.assertLess(home.index('class="selected-work-gateway"'),home.index('id="eb1a"'))
    def test_ultrakam_exit_card_and_coverage(self):
        work=self.pages['selected-work.html']
        self.assertLess(work.index('id="viddy"'),work.index('id="ultrakam"'))
        self.assertLess(work.index('id="ultrakam"'),work.index('id="flyr"'))
        self.assertIn('https://www.youtube.com/embed/jqs6dXF9wDU',work)
        self.assertIn('style="--video-ratio: 200 / 150"',work)
        self.assertIn('Apple’s WWDC14 feature on Medium',work)
        self.assertEqual({company['name'] for company in generate.HISTORIC_COMPANIES if company.get('exit')},{'Viddy','Ultrakam','FlyrTV'})
    def test_spreeai_valuation_and_coverage(self):
        work=self.pages['selected-work.html']
        self.assertIn('$1.5B Valuation | 2026',work)
        self.assertIn('PR Newswire: $1.5B valuation',work)
        self.assertNotIn('Naomi Campbell Board Member | AI Fashion',work)
    def test_press_precedes_interviews_on_home(self):
        home=self.pages['index.html']
        self.assertLess(home.index('id="press"'),home.index('id="interviews"'))
    def test_image_budgets_and_responsive_assets(self):
        for name,budget in [('index.html',1450000),('selected-work.html',360000)]:
            total=sum((ROOT/url).stat().st_size for url in {im['src'] for im in self.docs[name].images})
            self.assertLessEqual(total,budget)
        portrait=next(im for im in self.docs['index.html'].images if im.get('fetchpriority')=='high')
        self.assertIn('srcset',portrait)
        self.assertLessEqual((ROOT/portrait['src']).stat().st_size,150000)
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
