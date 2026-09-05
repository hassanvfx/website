"""CSS Styles for Portfolio - Enhanced Gallery Design"""

CSS_STYLES = '''
:root {
  --black: #000000;
  --white: #FFFFFF;
  --cyan: #00D4FF;
  --purple: #8B5CF6;
  --blue: #00D4FF;
  --neon-gradient: linear-gradient(135deg, #00D4FF, #8B5CF6);
  --neon-glow: 0 0 20px rgba(0, 212, 255, 0.3);
  --neon-glow-strong: 0 0 30px rgba(0, 212, 255, 0.5), 0 0 60px rgba(139, 92, 246, 0.3);
  --gray-dark: #111111;
  --gray-light: #F5F5F5;
  --text-on-black: #FFFFFF;
  --text-muted-black: rgba(255,255,255,0.6);
  --text-on-white: #000000;
  --text-muted-white: #555555;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  border: 0;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: var(--black);
  color: var(--white);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

a,
a:hover,
a:focus,
a:focus-visible {
  text-decoration: none;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 60px;
}

@media (max-width: 768px) {
  .container {
    padding: 0 16px;
  }
}

/* Full-width containers on mobile for ALL sections */
@media (max-width: 968px) {
  /* Make all containers no padding on tablet/mobile */
  .container {
    padding: 0;
    max-width: 100%;
  }

  /* Add padding only to text content, not video wrappers */
  .section-header,
  .project-content,
  .press-grid,
  .books-grid,
  .recognition-grid,
  .quote,
  .hero-content,
  .footer .container > * {
    padding-left: 16px;
    padding-right: 16px;
  }

  /* Project cards full bleed videos */
  .project-card .container {
    padding: 0;
  }

  .project-card .project-content {
    padding: 20px 16px;
  }

  /* All video wrappers full width edge to edge */
  .project-card .video-wrapper,
  .more-video-item .video-wrapper,
  .video-wrapper,
  .project-video {
    border-radius: 0;
    margin: 0;
    width: 100%;
  }

  .more-videos-inner {
    padding-left: 0;
    padding-right: 0;
    gap: 24px;
  }

  .more-video-item {
    padding: 0;
  }

  .more-video-item .video-title {
    padding: 8px 16px;
  }

  /* Hero adjustments */
  .hero {
    padding: 100px 16px;
  }

  /* Section padding on mobile */
  .section-black,
  .section-white,
  .section-dark {
    padding: 60px 0;
  }

  /* Stats row padding */
  .stats-row {
    padding: 0 16px;
  }
}

/* Even smaller screens - truly full width */
@media (max-width: 600px) {
  .section-header,
  .project-content,
  .press-grid,
  .books-grid,
  .recognition-grid,
  .quote,
  .hero-content,
  .stats-row {
    padding-left: 12px;
    padding-right: 12px;
  }

  .project-card .project-content {
    padding: 16px 12px;
  }

  .hero {
    padding: 80px 12px;
  }

  .more-video-item .video-title {
    padding: 8px 12px;
  }
}

/* ===========================================
   SCROLL-SYNCED NAVIGATION
   =========================================== */
.scroll-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: rgba(0,0,0,0.95);
  backdrop-filter: blur(20px);

  transition: transform 0.3s ease;
}

.nav-inner {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 70px;
  gap: 0;
}

nav a {
  position: relative;
  padding: 24px 32px;
  font-size: 13px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: rgba(255,255,255,0.4);
  text-decoration: none;
  transition: all 0.3s ease;
  cursor: pointer;
}

.scroll-nav-item:hover {
  color: rgba(255,255,255,0.8);
}

.scroll-nav-item.active {
  color: var(--white);
}

.scroll-nav-item::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background: var(--blue);
  transform: translateX(-50%);
  transition: width 0.3s ease;
}

.scroll-nav-item.active::after {
  width: 30px;
}

@media (max-width: 968px) {
  .scroll-nav-item {
    padding: 20px 16px;
    font-size: 11px;
    letter-spacing: 0.1em;
  }
}

@media (max-width: 600px) {
  .scroll-nav-inner {
    overflow-x: auto;
    justify-content: flex-start;
  }
  .scroll-nav-item {
    padding: 20px 12px;
    white-space: nowrap;
  }
}

/* ===========================================
   SECTIONS
   =========================================== */
.section-black {
  background: var(--black);
  padding: 140px 0;
}

.section-white {
  background: var(--white);
  padding: 140px 0;
  color: var(--text-on-white);
}

.section-dark {
  background: var(--gray-dark);
  padding: 140px 0;
}

.section-compact {
  padding: 100px 0;
}

/* ===========================================
   TYPOGRAPHY
   =========================================== */
h1 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 80px;
  font-weight: 900;
  letter-spacing: -0.03em;
  line-height: 1.0;
}

h2 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 56px;
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.1;
}

h3 {
  font-family: 'Inter', sans-serif;
  font-size: 36px;
  font-weight: 700;
  letter-spacing: -0.01em;
}

h4 {
  font-family: 'Inter', sans-serif;
  font-size: 24px;
  font-weight: 600;
}

.eyebrow {
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.2em;
  color: var(--blue);
  margin-bottom: 16px;
}

.lead {
  font-size: 24px;
  line-height: 1.5;
  font-weight: 400;
}

.quote {
  font-size: 28px;
  font-style: italic;
  line-height: 1.5;
  color: var(--text-muted-black);
  max-width: 900px;
  margin: 0 auto;
  text-align: center;
  padding: 60px 0;

}

.quote cite {
  display: block;
  margin-top: 24px;
  font-size: 14px;
  font-style: normal;
  font-weight: 600;
  color: var(--blue);
}

.footnote {
  font-size: 13px;
  color: var(--text-muted-black);
  margin-top: 16px;
  font-style: italic;
}

/* ===========================================
   HERO
   =========================================== */
.hero {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 120px 60px;
  position: relative;
}

.section {
  padding: 100px 60px;
}

.section-header.white {
  color: var(--white);
}

.quote-section {
  padding: 80px 60px;
  text-align: center;
  background: #000;
}

.quote-section blockquote {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 24px;
  font-style: italic;
  color: rgba(255,255,255,0.7);
  max-width: 900px;
  margin: 0 auto;
}

.quote-section cite {
  display: block;
  margin-top: 20px;
  color: var(--blue);
  font-style: normal;
}

footer {
  padding: 100px 60px;
  text-align: center;
  background: #000;

}

footer h2 {
  font-family: 'Playfair Display', Georgia, serif;
  margin-bottom: 10px;
}

footer p {
  color: rgba(255,255,255,0.6);
  margin-bottom: 20px;
}

footer .email {
  display: block;
  color: var(--blue);
  font-size: 1.2rem;
  margin-bottom: 30px;
  text-decoration: none;
}

footer .social-links {
  display: flex;
  gap: 15px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 40px;
}

footer .copyright {
  color: rgba(255,255,255,0.4);
  font-size: 0.85rem;
}

.hero-content {
  max-width: 1000px;
}

.hero h1 {
  margin-bottom: 24px;
}

.hero .subtitle {
  font-size: 28px;
  color: var(--blue);
  margin-bottom: 12px;
  font-weight: 600;
}

.hero .tagline {
  font-size: 20px;
  color: var(--text-muted-black);
  margin-bottom: 60px;
}

/* Stats Row */
.stats-row {
  display: flex;
  justify-content: center;
  gap: 80px;
  margin: 60px 0;
}

@media (max-width: 768px) {
  .stats-row {
    flex-wrap: wrap;
    gap: 40px;
  }
}

.stat-item {
  text-align: center;
}

.stat-item .value {
  font-size: 64px;
  font-weight: 900;
  color: var(--white);
  line-height: 1;
}

.stat-item .label {
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  color: var(--text-muted-black);
  margin-top: 8px;
}

/* ===========================================
   PROJECT CARDS - HERO VIDEO + VIEW MORE
   =========================================== */
.project-card {
  margin-bottom: 0;
}

.project-card-inner {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: center;
}

.project-card-inner.reverse {
  direction: rtl;
}

.project-card-inner.reverse > * {
  direction: ltr;
}

@media (max-width: 968px) {
  .project-card-inner {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  .project-card-inner.reverse {
    direction: ltr;
  }
}

.project-video {
  position: relative;
}

.video-wrapper {
  position: relative;
  padding-top: 56.25%;
  background: #111;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}

.video-wrapper iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;

}

.project-content {
  padding: 20px 0;
}

.project-content .eyebrow {
  margin-bottom: 20px;
}

.project-content h2 {
  margin-bottom: 24px;
}

.project-content .description {
  font-size: 18px;
  line-height: 1.8;
  color: var(--text-muted-black);
  margin-bottom: 32px;
}

.project-content .highlight {
  display: inline-block;
  background: rgba(0,113,227,0.15);
  color: var(--blue);
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 24px;
}

.project-actions {
  display: flex;
  gap: 16px;
  flex-wrap: wrap;
}

/* Expandable Videos */
.more-videos {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.5s ease;
  margin-top: 0;
}

.more-videos.expanded {
  max-height: 2000px;
  margin-top: 60px;
}

.more-videos-inner {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 30px;
  padding: 40px 0;

}

@media (max-width: 968px) {
  .more-videos-inner {
    grid-template-columns: 1fr;
    gap: 40px;
  }
}

.more-video-item {
  position: relative;
}

.more-video-item .video-wrapper {
  margin-bottom: 12px;
}

.more-video-item .video-title {
  font-size: 14px;
  color: var(--text-muted-black);
}

/* ===========================================
   BUTTONS
   =========================================== */
.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 28px;
  font-size: 14px;
  font-weight: 500;
  text-decoration: none;
  border-radius: 50px;
  transition: all 0.3s ease;
  cursor: pointer;

}

.btn-primary {
  background: linear-gradient(135deg, #00D4FF, #8B5CF6);
  color: var(--white);
  box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 0 30px rgba(0, 212, 255, 0.5), 0 0 60px rgba(139, 92, 246, 0.3);
}

.btn-outline {
  background: transparent;
  color: var(--cyan);

}

.btn-outline:hover {

  background: rgba(0, 212, 255, 0.1);
  box-shadow: 0 0 20px rgba(0, 212, 255, 0.2);
}

.btn-text {
  background: transparent;
  color: var(--blue);
  padding: 16px 0;
}

.btn-text:hover {
  opacity: 0.8;
}

.btn-text .arrow {
  transition: transform 0.3s ease;
}

.btn-text:hover .arrow {
  transform: translateX(4px);
}

.btn-expand {
  background: transparent;
  color: var(--text-muted-black);

  font-size: 14px;
  padding: 12px 24px;
}

.btn-expand:hover {
  color: var(--white);

}

.btn-expand .icon {
  transition: transform 0.3s ease;
}

.btn-expand.expanded .icon {
  transform: rotate(180deg);
}

/* ===========================================
   SECTION HEADERS
   =========================================== */
.section-header {
  text-align: center;
  margin-bottom: 80px;
}

.section-header .eyebrow {
  margin-bottom: 20px;
}

.section-header h2 {
  margin-bottom: 24px;
}

.section-header .lead {
  max-width: 700px;
  margin: 0 auto;
  color: var(--text-muted-black);
}

.section-white .section-header .lead {
  color: var(--text-muted-white);
}

/* ===========================================
   PRESS CARDS
   =========================================== */
.press-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

@media (max-width: 968px) {
  .press-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
  }
}

@media (max-width: 600px) {
  .press-grid {
    grid-template-columns: 1fr;
    padding: 0 16px;
  }
}

.press-card {
  background: var(--white);
  border-radius: 16px;
  padding: 2rem;
  transition: all 0.3s ease;
  text-decoration: none;
  display: block;
  color: var(--text-on-white);
}

.press-card:hover {
  background: #fafafa;
  transform: translateY(-4px);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
}

.press-card .press-logo {
  width: 100%;
  aspect-ratio: 3/2;
  object-fit: contain;
  border-radius: 12px;
  margin-bottom: 1.5rem;
  background: #000;
  padding: 1rem;
}

.press-card .publication {
  color: #666;
  font-size: 0.85rem;
  margin-bottom: 0.5rem;
  display: block;
}

.press-card h4 {
  color: var(--text-on-white);
  font-size: 1.15rem;
  margin: 0.5rem 0;
  line-height: 1.3;
  font-weight: 600;
}

.press-card .excerpt {
  color: #666;
  font-size: 0.9rem;
  line-height: 1.5;
  margin-top: 0.75rem;
}

/* ===========================================
   RECOGNITION
   =========================================== */
.recognition-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
}

@media (max-width: 968px) {
  .recognition-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .recognition-grid {
    grid-template-columns: 1fr;
  }
}

.recognition-item {
  text-align: center;
  padding: 40px 30px;
  background: rgba(255,255,255,0.03);
  border-radius: 16px;

}

.recognition-item .year {
  font-size: 13px;
  color: var(--blue);
  font-weight: 600;
  margin-bottom: 16px;
  letter-spacing: 0.1em;
}

.recognition-item h4 {
  color: var(--white);
  margin-bottom: 12px;
  font-size: 18px;
}

.recognition-item p {
  color: var(--text-muted-black);
  font-size: 14px;
  line-height: 1.6;
}

/* ===========================================
   BOOKS
   =========================================== */
.books-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 40px;
}

@media (max-width: 768px) {
  .books-grid {
    grid-template-columns: 1fr;
  }
}

.book-card {
  background: var(--white);
  border-radius: 16px;
  padding: 48px;
  text-align: center;
  color: var(--text-on-white);
}

.book-card .year {
  font-size: 13px;
  color: var(--blue);
  font-weight: 600;
  margin-bottom: 20px;
  letter-spacing: 0.1em;
}

.book-card h4 {
  color: var(--text-on-white);
  margin-bottom: 12px;
  font-size: 24px;
}

.book-card .subtitle {
  color: var(--text-muted-white);
  font-size: 16px;
  margin-bottom: 20px;
}

.book-card .press {
  font-size: 13px;
  font-style: italic;
  color: var(--text-muted-white);
  margin-bottom: 24px;
}

/* ===========================================
   FOOTER
   =========================================== */
.footer {
  background: var(--black);
  padding: 100px 0;
  text-align: center;

}

.footer h3 {
  color: var(--white);
  margin-bottom: 16px;
  font-size: 32px;
}

.footer .email {
  font-size: 18px;
  color: var(--text-muted-black);
  margin-bottom: 40px;
}

.footer .social-links {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 60px;
}

.footer .copyright {
  font-size: 13px;
  color: rgba(255,255,255,0.4);
  max-width: 600px;
  margin: 0 auto;
}

/* ===========================================
   RESPONSIVE TYPOGRAPHY
   =========================================== */
@media (max-width: 768px) {
  h1 {
    font-size: 48px;
  }

  h2 {
    font-size: 36px;
  }

  h3 {
    font-size: 28px;
  }

  .lead {
    font-size: 18px;
  }

  .quote {
    font-size: 20px;
    padding: 40px 0;
  }

  .section-black,
  .section-white,
  .section-dark {
    padding: 100px 0;
  }

  .stat-item .value {
    font-size: 48px;
  }
}

/* ===========================================
   ANIMATIONS
   =========================================== */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

[data-aos="fade-up"] {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.8s ease, transform 0.8s ease;
}

[data-aos="fade-up"].aos-animate {
  opacity: 1;
  transform: translateY(0);
}

/* ===========================================
   PRESS LOGOS SHOWCASE - "IN THE NEWS" MARQUEE
   =========================================== */
.press-showcase {
  background: linear-gradient(180deg, #000 0%, #0a0a0a 50%, #000 100%);
  padding: 12rem 0;
  width: 100%;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  transition: all 0.3s ease;
}

.press-showcase::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 1200px;
  height: 400px;
  background: radial-gradient(ellipse at center, rgba(0,212,255,0.08) 0%, transparent 70%);
  pointer-events: none;
}

.press-marquee-container {
  width: 100%;
  overflow: hidden;
  position: relative;
}

.press-logos-scroll {
  display: flex;
  align-items: center;
  gap: 8rem;
  animation: scroll-logos 50s linear infinite;
  will-change: transform;
}

.press-logo-item {
  flex-shrink: 0;
}

.press-logo-item img {
  height: 240px;
  width: auto;
  object-fit: contain;
  opacity: 0.7;
  filter: brightness(1.2);
  transition: all 0.3s ease;
}

.press-showcase:hover::before {
  background: radial-gradient(ellipse at center, rgba(0,212,255,0.12) 0%, transparent 70%);
}

.press-showcase:hover .press-logo-item img {
  opacity: 1;
  filter: brightness(1.4) drop-shadow(0 0 20px rgba(0,212,255,0.3));
}

@keyframes scroll-logos {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}

@media (max-width: 968px) {
  .press-showcase {
    padding: 4rem 0;
  }

  .press-logos-scroll {
    gap: 5rem;
    animation-duration: 40s;
  }

  .press-logo-item img {
    height: 180px;
  }
}

@media (max-width: 600px) {
  .press-showcase {
    padding: 6rem 0;
  }

  .press-logos-scroll {
    gap: 4rem;
    animation-duration: 30s;
  }

  .press-logo-item img {
    height: 120px;
  }
}
'''


COMPONENT_STYLES = '''
/* Hero Portrait */
.hero-portrait {
  margin-bottom: 2.5rem;
}
.hero-portrait img {
  width: 280px;
  height: 350px;
  border-radius: 16px;
  object-fit: cover;
  object-position: top center;

  box-shadow: 0 0 50px rgba(0, 212, 255, 0.25), 0 0 100px rgba(139, 92, 246, 0.15);
  transition: all 0.3s ease;
}
.hero-portrait img:hover {

  box-shadow: 0 0 70px rgba(0, 212, 255, 0.4), 0 0 120px rgba(139, 92, 246, 0.25);
  transform: scale(1.02);
}

/* Timeline Markers */
.timeline-marker {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  padding: 3rem 0;
  background: #000;
}
.marker-line {
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, #333, transparent);
  max-width: 200px;
}
.marker-circle {
  background: #1a1a1a;

  border-radius: 50px;
  padding: 0.75rem 1.5rem;
  color: #fff;
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 0.9rem;
}
.marker-label {
  color: #666;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

/* Featured Nav Link - Neon Cyan */
nav a.featured {
  background: linear-gradient(135deg, #00D4FF, #8B5CF6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 600;
  text-shadow: 0 0 30px rgba(0, 212, 255, 0.5);
}
nav a.featured:hover {
  text-shadow: 0 0 40px rgba(0, 212, 255, 0.8), 0 0 60px rgba(139, 92, 246, 0.5);
}
nav a:hover {
  color: #00D4FF !important;
}

/* Mobile identity lockup */
.mobile-title {
  display: none;
}
.mobile-title-first {
  color: #FFFFFF;
}
.mobile-title-last {
  color: #FFFFFF;
}

/* Hamburger Menu Button */
.hamburger {
  display: none;
  flex-direction: column;
  justify-content: center;
  gap: 5px;
  width: 30px;
  height: 30px;
  padding: 0;

  background: transparent;
  cursor: pointer;
  z-index: 1002;
  position: relative;
}
.hamburger span {
  display: block;
  width: 100%;
  height: 2px;
  background: #fff;
  transition: all 0.3s ease;
}
.hamburger.active span:nth-child(1) {
  transform: rotate(45deg) translate(5px, 5px);
}
.hamburger.active span:nth-child(2) {
  opacity: 0;
}
.hamburger.active span:nth-child(3) {
  transform: rotate(-45deg) translate(5px, -5px);
}

/* Mobile Menu Modal */
.mobile-menu {
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
}
.mobile-menu.active {
  opacity: 1;
  visibility: visible;
}
.mobile-menu a {
  font-size: 24px;
  font-weight: 500;
  color: rgba(255,255,255,0.8);
  text-decoration: none;
  padding: 16px 32px;
  text-transform: uppercase;
  letter-spacing: 0.15em;
  transition: all 0.3s ease;
}
.mobile-menu a:hover {
  color: #00D4FF;
}
.mobile-menu a.featured {
  background: linear-gradient(135deg, #00D4FF, #8B5CF6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 600;
}

/* Submenu - Separate Row */
.submenu-nav {
  background: rgba(10, 10, 10, 0.95);

  padding: 10px 0;
  position: sticky;
  top: 60px;
  z-index: 999;
  backdrop-filter: blur(10px);
}
.submenu-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2.5rem;
}
.submenu-link {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.85rem;
  font-weight: 400;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  text-decoration: none;
  transition: all 0.3s ease;
  padding: 8px 12px;
}
.submenu-link:hover {
  color: #00D4FF;
}

/* Mobile Nav Responsive */
@media (max-width: 768px) {
  .scroll-nav {
    z-index: 1002;
  }
  .mobile-title {
    display: inline-flex;
    align-items: baseline;
    gap: 0.34em;
    padding: 0;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    font-size: clamp(1rem, 4.8vw, 1.25rem);
    font-weight: 600;
    line-height: 1;
    letter-spacing: -0.02em;
    text-transform: none;
    text-shadow: none;
  }
  .hamburger {
    display: flex;
    flex: 0 0 30px;
    margin-left: auto;
  }
  .nav-inner a:not(.mobile-title) {
    display: none;
  }
  .mobile-menu {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    align-content: start;
    align-items: stretch;
    justify-content: stretch;
    gap: 0.65rem;
    padding: max(5.75rem, calc(env(safe-area-inset-top) + 4.25rem)) 1rem max(1.25rem, env(safe-area-inset-bottom));
    overflow-y: auto;
  }
  .mobile-menu a {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 44px;
    padding: 0.6rem 0.5rem;

    border-radius: 999px;
    background: rgba(255, 255, 255, 0.035);
    font-size: 0.72rem;
    line-height: 1.15;
    letter-spacing: 0.1em;
    text-align: center;
  }
  .mobile-menu a.featured {

    background: linear-gradient(135deg, #00D4FF, #8B5CF6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .mobile-menu a:last-child {
    grid-column: 1 / -1;
  }
  .mobile-menu-close {
    display: none;
  }
  .mobile-menu-close:hover {

    color: #00D4FF;
  }
  .scroll-nav .nav-inner {
    justify-content: space-between;
    padding: 0 20px;
  }

  /* Hide submenu bar on mobile */
  .submenu-nav {
    display: none;
  }
}

/* Impact Cards */
.impact-card {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  background: #0a0a0a;
  padding: 2rem;
  margin-bottom: 1px;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}
.impact-card:nth-child(even) {
  direction: rtl;
}
.impact-card:nth-child(even) > * {
  direction: ltr;
}
.impact-card .card-video iframe {
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: 8px;
  box-shadow: 0 20px 60px rgba(0,212,255,0.15);

}
.impact-card .highlight {
  display: inline-block;
  background: linear-gradient(135deg, rgba(0,212,255,0.15), rgba(139,92,246,0.15));
  color: #00D4FF;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-size: 0.85rem;
  font-weight: 500;
  margin-bottom: 1rem;

}
.impact-card h3 {
  font-family: 'Playfair Display', serif;
  font-size: 2rem;
  margin: 0.5rem 0;
  color: #fff;
}
.impact-card .role {
  color: #888;
  margin-bottom: 1rem;
}

/* Company Press Quotes */
.company-press-quote {
  margin-top: 1.5rem;
  padding: 1rem;
  background: rgba(0,212,255,0.05);

  border-radius: 0 8px 8px 0;
}
.company-press-quote .quote-text {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  color: rgba(255,255,255,0.8);
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 0.5rem;
}
.company-press-quote .quote-source {
  color: rgba(255,255,255,0.5);
  font-size: 0.8rem;
}
.company-press-quote .quote-source strong {
  color: #00D4FF;
}

/* Project Cards */
.project-card {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  background: #0a0a0a;
  padding: 2rem;
  margin-bottom: 1px;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}
.project-card:nth-child(odd) {
  direction: rtl;
}
.project-card:nth-child(odd) > * {
  direction: ltr;
}
.project-card .card-video iframe {
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: 8px;
  box-shadow: 0 20px 60px rgba(0,212,255,0.15);

}
.project-card .highlight {
  display: inline-block;
  background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(139,92,246,0.1));
  color: #00D4FF;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-size: 0.85rem;
  margin-bottom: 1rem;

}
.project-card h3 {
  font-family: 'Playfair Display', serif;
  font-size: 1.75rem;
  margin: 0.5rem 0;
  color: #fff;
}
.project-card .quote {
  font-style: italic;
  color: #888;

  padding-left: 1rem;
  margin: 1rem 0;
}

/* Innovation Cards */
.innovation-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1rem;
  padding: 2rem;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}
.innovation-card {
  background: #0a0a0a;
  border-radius: 12px;
  overflow: hidden;
}
.innovation-card.featured {
  grid-column: 1 / -1;
  background: linear-gradient(135deg, rgba(0,212,255,0.05), rgba(139,92,246,0.08));

  padding: 2rem;
}
.innovation-card .badge {
  display: inline-block;
  background: linear-gradient(135deg, rgba(0,212,255,0.15), rgba(139,92,246,0.15));
  color: #00D4FF;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-size: 0.85rem;
  margin-bottom: 1rem;

}
.innovation-card .year-badge {
  display: inline-block;
  background: rgba(0,212,255,0.1);
  color: #00D4FF;
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-size: 0.75rem;

}
.innovation-card h3 {
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  margin: 0.5rem 0;
  color: #fff;
}
.innovation-card .tagline {
  background: linear-gradient(135deg, #00D4FF, #8B5CF6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 500;
  margin-bottom: 0.5rem;
}
.innovation-card .card-content {
  padding: 1.5rem;
}
.innovation-card .card-video iframe {
  width: 100%;
  aspect-ratio: 16/9;
  box-shadow: 0 20px 60px rgba(0,212,255,0.15);

  border-radius: 8px;
}

/* Filmography */
.filmography .film-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 2rem;
  padding: 2rem;
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}
.film-video iframe {
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: 8px;
  box-shadow: 0 20px 60px rgba(0,212,255,0.15);

}
.film-video .video-title {
  color: #888;
  text-align: center;
  margin-top: 0.5rem;
}
.film-links {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 2rem;
  padding: 2rem;
}
.ves-badge {
  background: linear-gradient(135deg, #b8860b, #daa520);
  color: #000;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-weight: 600;
  font-size: 0.85rem;
}

/* Books */
.books-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2.5rem;
  padding: 3rem 2rem;
  max-width: 1200px;
  margin: 0 auto;
}
.book-card:last-child:nth-child(odd) {
  grid-column: 1 / -1;
  width: min(100%, calc((100% - 2.5rem) / 2));
  justify-self: center;
}
.book-card {
  background: #0a0a0a;
  border-radius: 16px;
  padding: 2.5rem;
  transition: all 0.3s ease;
}
.book-actions {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.75rem;
}
.book-card:hover {
  background: #111;
  transform: translateY(-4px);
}
.book-cover {
  width: 100%;
  aspect-ratio: 1;
  object-fit: cover;
  border-radius: 12px;
  margin-bottom: 1.5rem;

  box-shadow: 0 0 30px rgba(0, 212, 255, 0.15), 0 10px 40px rgba(0, 0, 0, 0.3);
  transition: all 0.3s ease;
}
.book-cover--portrait {
  height: auto;
  aspect-ratio: 2 / 3;
  object-fit: contain;
  background: #050505;
}
.book-card:hover .book-cover {

  box-shadow: 0 0 50px rgba(0, 212, 255, 0.3), 0 15px 60px rgba(0, 0, 0, 0.4);
  transform: scale(1.02);
}
.book-card .year {
  color: #666;
  font-size: 0.85rem;
  margin-bottom: 0.5rem;
}
.book-card h3 {
  font-family: 'Playfair Display', serif;
  font-size: 1.25rem;
  margin: 0.5rem 0;
  color: #fff;
  line-height: 1.3;
}
.book-card .subtitle {
  color: #888;
  font-size: 0.85rem;
  margin-bottom: 1rem;
  line-height: 1.4;
}
.book-card .press {
  color: #00D4FF;
  font-size: 0.85rem;
  margin-bottom: 1rem;
}

/* Press */
.press-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
  padding: 2rem;
}
.press-card {
  background: #0a0a0a;
  border-radius: 8px;
  padding: 1.5rem;
  text-decoration: none;
  transition: all 0.3s ease;

}
.press-card:hover {
  background: #111;
  transform: translateY(-2px);

  box-shadow: 0 0 20px rgba(0, 212, 255, 0.1);
}
.press-card .publication {
  color: #00D4FF;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
}

.press-card h4 {
  color: #fff;
  font-size: 1rem;
  margin: 0.5rem 0;
}
.press-card p {
  color: #888;
  font-size: 0.85rem;
}

/* Bio/Artist Intro Section */
.bio-section {
  padding: 6rem 4rem;
  background: linear-gradient(180deg, #000 0%, #0a0a0a 100%);
}
.bio-content {
  max-width: 900px;
  margin: 0 auto;
}
.bio-headline {
  font-family: 'Playfair Display', serif;
  font-size: 2.5rem;
  color: #fff;
  margin-bottom: 1.5rem;
  text-align: center;
}
.bio-profile-image {
  margin: 0 auto 3rem;
  overflow: hidden;
  border-radius: 12px;
  box-shadow: 0 18px 48px rgba(0, 0, 0, 0.42);
}
.bio-profile-image img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}
.bio-featured-article {
  max-width: 600px;
  margin: 0 auto 3rem;
  padding: 1.5rem;
  background: linear-gradient(135deg, rgba(0,212,255,0.08), rgba(139,92,246,0.08));

  border-radius: 12px;
  text-align: center;
}
.bio-featured-article a {
  text-decoration: none;
}
.bio-featured-article .article-label {
  color: #00D4FF;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 0.5rem;
}
.bio-featured-article .article-title {
  display: block;
  color: #fff;
  font-size: 1.1rem;
  font-weight: 500;
  margin-bottom: 1.25rem;
}
.bio-featured-article .article-title:hover,
.bio-featured-article .article-title:focus-visible {
  color: #00D4FF;
  outline: none;
}
.bio-read-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 116px;
  margin-bottom: 1.1rem;
  padding: 0.7rem 1.15rem;
  color: #00131a;
  background: #00D4FF;
  border-radius: 999px;
  font-size: 0.9rem;
  font-weight: 800;
  transition: background 0.2s ease, transform 0.2s ease;
}
.bio-read-button:hover,
.bio-read-button:focus-visible {
  background: #63e6ff;
  outline: none;
  transform: translateY(-2px);
}
.bio-featured-article .article-source {
  color: rgba(255,255,255,0.5);
  font-size: 0.85rem;
}
.bio-intro {
  font-size: 1.2rem;
  line-height: 1.8;
  color: rgba(255,255,255,0.8);
  margin-bottom: 3rem;
  text-align: center;
}
.eb1a-card {
  background: linear-gradient(135deg, rgba(0,212,255,0.08), rgba(139,92,246,0.08));

  border-radius: 16px;
  padding: 2.5rem;
  margin-bottom: 2rem;
}
.eb1a-card h3 {
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  color: #fff;
  margin-bottom: 1rem;
}
.eb1a-card .eb1a-description {
  color: rgba(255,255,255,0.7);
  margin-bottom: 1.5rem;
  line-height: 1.7;
}
.eb1a-criteria {
  list-style: none;
  padding: 0;
}
.eb1a-criteria li {
  color: rgba(255,255,255,0.8);
  padding: 0.5rem 0;
  padding-left: 2rem;
  position: relative;
  font-size: 0.95rem;
}
.eb1a-criteria li::before {
  content: "✓";
  position: absolute;
  left: 0;
  color: #00D4FF;
  font-weight: bold;
}
.eb1a-wikipedia-link {
  display: flex;
  width: fit-content;
  margin: 1.5rem auto 0;
  padding: 0.72rem 1.1rem;
  color: #00131a;
  background: #00D4FF;
  border-radius: 999px;
  font-size: 0.9rem;
  font-weight: 800;
  text-decoration: none;
  transition: background 0.2s ease, transform 0.2s ease;
}
.eb1a-wikipedia-link:hover,
.eb1a-wikipedia-link:focus-visible {
  background: #63e6ff;
  outline: none;
  transform: translateY(-2px);
}
.bio-summary {
  font-size: 1.1rem;
  line-height: 1.8;
  color: rgba(255,255,255,0.7);
  text-align: center;
  font-style: italic;
}

/* Press Quote Dividers */
.press-quote-divider {
  padding: 4rem 2rem;
  background: linear-gradient(180deg, #050505 0%, #0a0a0a 50%, #050505 100%);
  text-align: center;
}
.press-quote-divider blockquote {
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  font-style: italic;
  color: rgba(255,255,255,0.8);
  max-width: 800px;
  margin: 0 auto 1rem;
  line-height: 1.6;
}
.press-quote-divider .source {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}
.press-quote-divider .source-name {
  color: #00D4FF;
  font-weight: 600;
  font-size: 0.9rem;
}
.press-quote-divider .source-context {
  color: rgba(255,255,255,0.5);
  font-size: 0.85rem;
}
.press-quote-divider a {
  color: #00D4FF;
  text-decoration: none;
}
.press-quote-divider a:hover {
  text-decoration: none;
}

/* Professional Profile / PDF.js Resume Viewer */
.professional-profile {
  position: relative;
  overflow: hidden;
  padding: 6rem 4rem;
  background: linear-gradient(135deg, #071522 0%, #0c0d18 54%, #161022 100%);


}
.professional-profile::before {
  content: "";
  position: absolute;
  inset: -30% auto auto -12%;
  width: 620px;
  height: 620px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(0, 212, 255, 0.13), transparent 68%);
  pointer-events: none;
}
.professional-profile::after {
  content: "";
  position: absolute;
  right: -12%;
  bottom: -45%;
  width: 620px;
  height: 620px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(139, 92, 246, 0.16), transparent 68%);
  pointer-events: none;
}
.professional-profile-inner {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: minmax(260px, 0.75fr) minmax(0, 1.25fr);
  gap: 3rem;
  max-width: 1220px;
  margin: 0 auto;
  align-items: center;
}
.professional-profile-eyebrow {
  display: block;
  color: #00D4FF;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
}
.professional-profile-copy h2 {
  margin: 0.7rem 0 1.2rem;
  color: #fff;
  font-family: 'Playfair Display', serif;
  font-size: clamp(2.3rem, 4vw, 3.9rem);
  line-height: 1.08;
}
.professional-profile-copy p {
  max-width: 500px;
  color: rgba(255, 255, 255, 0.75);
  font-size: 1.08rem;
  line-height: 1.75;
}
.professional-profile-actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1rem;
  margin-top: 2rem;
}
.professional-profile-download {
  display: inline-flex;
  padding: 0.9rem 1.15rem;
  border-radius: 6px;
  background: #00D4FF;
  color: #00141b;
  font-size: 0.92rem;
  font-weight: 800;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.professional-profile-download:hover,
.professional-profile-download:focus-visible {
  box-shadow: 0 0 28px rgba(0, 212, 255, 0.38);
  transform: translateY(-2px);
}
.professional-profile-open {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.9rem;
  font-weight: 600;
}
.professional-profile-open:hover,
.professional-profile-open:focus-visible {
  color: #00D4FF;
}
.professional-profile-viewer {
  overflow: hidden;
  background: rgba(0, 0, 0, 0.38);

  border-radius: 12px;
  box-shadow: 0 28px 80px rgba(0, 0, 0, 0.42), 0 0 45px rgba(0, 212, 255, 0.1);
}
.professional-profile-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  min-height: 52px;
  padding: 0.65rem 0.8rem 0.65rem 1rem;

  background: rgba(7, 18, 29, 0.85);
}
.professional-profile-status {
  color: rgba(255, 255, 255, 0.68);
  font-size: 0.8rem;
}
.professional-profile-controls {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}
.professional-profile-controls button {
  display: inline-grid;
  width: 30px;
  height: 30px;
  place-items: center;

  border-radius: 4px;
  background: rgba(0, 212, 255, 0.08);
  color: #00D4FF;
  cursor: pointer;
  font-size: 1rem;
}
.professional-profile-controls button:disabled {
  cursor: not-allowed;
  opacity: 0.38;
}
.professional-profile-controls button:not(:disabled):hover,
.professional-profile-controls button:not(:disabled):focus-visible {
  background: rgba(0, 212, 255, 0.2);
}
#resumePageIndicator {
  min-width: 42px;
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.78rem;
  text-align: center;
}
.professional-profile-canvas-wrap {
  min-height: 380px;
  max-height: 760px;
  overflow: auto;
  padding: 1rem;
  background: linear-gradient(135deg, rgba(0, 212, 255, 0.035), rgba(139, 92, 246, 0.04));
}
.professional-profile-page-frame {
  display: grid;
  width: 100%;
  place-items: start center;
}
#resumeCanvas {
  display: block;
  max-width: none;
  height: auto;
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.45);
}
.professional-profile-preview {
  display: block;
  width: min(100%, 612px);
  height: auto;
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.45);
}
.professional-profile-page-frame > [hidden] {
  display: none;
}
.professional-profile-fallback {
  padding: 0.75rem 1rem;
  color: rgba(255, 255, 255, 0.52);
  font-size: 0.75rem;
  text-align: center;
}
.professional-profile-fallback a {
  color: #00D4FF;
}
@media (max-width: 768px) {
  .professional-profile {
    padding: 4rem 16px;
  }
  .professional-profile-inner {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  .professional-profile-canvas-wrap {
    min-height: 0;
    max-height: none;
    overflow-x: hidden;
    overflow-y: visible;
    padding: 0.5rem;
  }
  .professional-profile-page-frame {
    place-items: start center;
  }
  #resumeCanvas,
  .professional-profile-preview {
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
  }
  .professional-profile-toolbar {
    align-items: flex-start;
    flex-direction: column;
  }
  .professional-profile-controls {
    width: 100%;
    justify-content: flex-end;
  }
}

/* ClineFlow Featured Callout */
.clineflow-callout {
  padding: 0 0 6rem;
  background: linear-gradient(180deg, #000 0%, #050510 50%, #000 100%);
  position: relative;
  overflow: hidden;
}
.clineflow-callout::before {
  content: "";
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(0,212,255,0.1) 0%, transparent 70%);
  pointer-events: none;
}
.clineflow-inner {
  max-width: 900px;
  margin: 0 auto;
  padding: 5rem 4rem 0;
  text-align: center;
  position: relative;
  z-index: 1;
}
.clineflow-hero {
  display: block;
  position: relative;
  z-index: 1;
  width: 100%;
  margin: 0;
  background: #000;
}
.clineflow-hero img {
  display: block;
  width: 100%;
  height: auto;
}
.clineflow-logo {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  margin-bottom: 1.5rem;
  filter: invert(1);
  transition: all 0.3s ease;
}
.clineflow-logo:hover {
  transform: scale(1.1);
  filter: invert(1) drop-shadow(0 0 20px rgba(0,212,255,0.5));
}
.clineflow-badge {
  display: inline-block;
  background: linear-gradient(135deg, rgba(0,212,255,0.2), rgba(139,92,246,0.2));
  color: #00D4FF;
  padding: 0.5rem 1.5rem;
  border-radius: 50px;
  font-size: 0.85rem;
  font-weight: 600;
  margin-bottom: 2rem;

  letter-spacing: 0.1em;
}
.clineflow-title {
  font-family: 'Playfair Display', serif;
  font-size: 3.5rem;
  margin-bottom: 0.5rem;
  background: linear-gradient(135deg, #00D4FF, #8B5CF6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.clineflow-tagline {
  font-size: 1.4rem;
  color: rgba(255,255,255,0.9);
  margin-bottom: 0.5rem;
}
.clineflow-subtitle {
  color: rgba(255,255,255,0.5);
  font-size: 1rem;
  margin-bottom: 2rem;
}
.clineflow-description {
  font-size: 1.15rem;
  line-height: 1.8;
  color: rgba(255,255,255,0.75);
  margin-bottom: 2.5rem;
}
.clineflow-features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 2.5rem;
  text-align: left;
}
.clineflow-feature {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 0.75rem;
  background: rgba(0,212,255,0.05);
  border-radius: 8px;

}
.clineflow-feature::before {
  content: "→";
  color: #00D4FF;
  font-weight: bold;
}
.clineflow-feature span {
  color: rgba(255,255,255,0.8);
  font-size: 0.9rem;
}
.clineflow-quote {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-size: 1.15rem;
  color: rgba(255,255,255,0.6);
  margin-bottom: 2rem;
  padding: 0 2rem;
}
.clineflow-positioning {
  font-size: 1rem;
  color: #00D4FF;
  font-weight: 500;
  margin-bottom: 0;
}
.clineflow-actions {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.25rem;
  margin: 3.5rem 0 2.75rem;
}
.clineflow-cta {
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
}
.clineflow-cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 0 50px rgba(0, 212, 255, 0.5), 0 0 80px rgba(139, 92, 246, 0.3);
}
.clineflow-stars {
  display: block;
  margin-top: 1.5rem;
  color: rgba(255,255,255,0.5);
  font-size: 0.9rem;
}

/* Focused ClineFlow installer */
.clineflow-callout.clineflow-installer {
  margin: clamp(2.5rem, 5vw, 5rem) 0;
  padding: clamp(3rem, 6vw, 6rem) clamp(1rem, 2.5vw, 3.25rem);
  background: #03090d;
}
.clineflow-installer::before {
  display: none;
}
.clineflow-installer-shell {
  width: min(100%, 1480px);
  margin: 0 auto;
}
.clineflow-installer-inner {
  width: 100%;
  position: relative;
  z-index: 1;
}
.clineflow-installer-hero {
  width: 100%;
  margin: 0 0 clamp(3rem, 6vw, 6rem);

}
.clineflow-installer-hero img {
  aspect-ratio: 16 / 9;
  object-fit: cover;
}
.clineflow-wordmark {
  display: inline-block;
  color: #eaf6ff;
  font-family: Inter, sans-serif;
  font-size: clamp(3.75rem, 8vw, 8rem);
  font-weight: 900;
  letter-spacing: -0.09em;
  line-height: 0.85;
  text-decoration: none;
}
.clineflow-wordmark:hover,
.clineflow-wordmark:focus-visible {
  color: #fff;
  outline: none;
}
.clineflow-installer h2 {
  max-width: 1120px;
  margin: clamp(4rem, 8vw, 8rem) 0 clamp(3rem, 6vw, 5.5rem);
  color: #eaf6ff;
  font-family: Inter, sans-serif;
  font-size: clamp(2rem, 3.2vw, 3.25rem);
  font-weight: 500;
  letter-spacing: -0.045em;
  line-height: 1.32;
}
.clineflow-installer h2 span {
  color: #00bfff;
}
.clineflow-installer-panel {
  padding: clamp(1.75rem, 3.25vw, 4rem);
  background: linear-gradient(115deg, #0b2d45 0%, #0b2538 100%);


}
.clineflow-installer-panel > p {
  margin: 0 0 1.7rem;
  color: #42a9ff;
  font-family: Inter, sans-serif;
  font-size: clamp(0.85rem, 1.2vw, 1.1rem);
  font-weight: 800;
  letter-spacing: 0.18em;
  text-transform: uppercase;
}
.clineflow-prompt-wrap {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1.35rem 1.5rem;
  background: #030e1b;

  border-radius: 7px;
}
.clineflow-prompt-wrap code {
  flex: 1;
  color: #d5eaff;
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: clamp(0.9rem, 1.3vw, 1.15rem);
  line-height: 1.55;
  overflow-wrap: anywhere;
}
.clineflow-copy-button {
  flex: 0 0 auto;
  padding: 0.65rem 1rem;
  color: #d9efff;
  background: #123d5b;

  border-radius: 6px;
  cursor: pointer;
  font: 700 0.9rem Inter, sans-serif;
}
.clineflow-copy-button:hover,
.clineflow-copy-button:focus-visible {
  background: #18567e;
  outline: 2px solid #00bfff;
  outline-offset: 2px;
}
.clineflow-agent-compatibility {
  margin: clamp(2.5rem, 5vw, 5rem) 0 0;
  text-align: center;
}
.clineflow-agent-compatibility img {
  display: block;
  width: 100%;
  height: auto;
}
.clineflow-agent-compatibility figcaption {
  margin-top: 1.25rem;
  color: rgba(234, 246, 255, 0.82);
  font: 600 clamp(1rem, 1.5vw, 1.2rem)/1.45 Inter, sans-serif;
}
.clineflow-masterclass {
  max-width: 560px;
  margin: clamp(2rem, 4vw, 3.5rem) auto 0;
  text-align: center;
}
.clineflow-masterclass p {
  margin: 0 0 1rem;
  color: rgba(234, 246, 255, 0.78);
  font: 600 clamp(1rem, 1.5vw, 1.2rem)/1.45 Inter, sans-serif;
}
.clineflow-masterclass-divider {
  width: 100%;
  height: 1px;
  margin-bottom: 1.1rem;
  background: linear-gradient(90deg, #00bfff 0%, rgba(0, 191, 255, 0.12) 100%);
}
.clineflow-masterclass-cta {
  display: inline-flex;
  align-items: center;
  gap: 0.65rem;
  padding: 0.9rem 1.1rem;
  color: #00121d;
  background: #00bfff;

  border-radius: 4px;
  box-shadow: 0 0 28px rgba(0, 191, 255, 0.23);
  font: 800 clamp(1rem, 1.4vw, 1.15rem)/1.35 Inter, sans-serif;
  text-decoration: none;
  transition: background 180ms ease, box-shadow 180ms ease, transform 180ms ease;
}
.clineflow-masterclass-cta span {
  font-size: 1.2em;
  line-height: 1;
}
.clineflow-masterclass-cta:hover,
.clineflow-masterclass-cta:focus-visible {
  background: #63dcff;
  box-shadow: 0 0 36px rgba(0, 191, 255, 0.42);
  outline: none;
  transform: translateY(-2px);
}
@media (max-width: 700px) {
  .clineflow-wordmark { letter-spacing: -0.07em; }
  .clineflow-installer h2 { margin-top: 4rem; }
  .clineflow-prompt-wrap { flex-direction: column; }
  .clineflow-copy-button { width: 100%; }
  .clineflow-masterclass { max-width: none; }
  .clineflow-masterclass-cta { width: 100%; justify-content: center; }
}

/* MemeArcade Featured App Callout */
.meme-arcade-callout {
  padding: 6rem 4rem;
  position: relative;
  overflow: hidden;
  background:
    radial-gradient(circle at 16% 18%, rgba(234, 56, 255, 0.22), transparent 32%),
    radial-gradient(circle at 84% 28%, rgba(0, 212, 255, 0.16), transparent 30%),
    linear-gradient(180deg, #07010d 0%, #0e0520 50%, #04060f 100%);


}
.meme-arcade-inner {
  max-width: 1100px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
  text-align: center;
}
.meme-arcade-icon {
  display: block;
  width: min(100%, 210px);
  height: auto;
  margin: -1rem auto 0.25rem;
  filter: drop-shadow(0 0 30px rgba(234, 56, 255, 0.55));
}
.meme-arcade-badge {
  display: inline-block;
  margin-bottom: 1.5rem;
  padding: 0.5rem 1.5rem;

  border-radius: 999px;
  background: linear-gradient(135deg, rgba(234, 56, 255, 0.2), rgba(0, 212, 255, 0.16));
  color: #f3a8ff;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.12em;
}
.meme-arcade-callout h2 {
  max-width: 840px;
  margin: 0 auto 1.25rem;
  font-family: 'Playfair Display', serif;
  font-size: clamp(2.5rem, 5vw, 4.25rem);
  line-height: 1.04;
  background: linear-gradient(135deg, #fff 12%, #f16bff 55%, #00d4ff 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.meme-arcade-description {
  max-width: 760px;
  margin: 0 auto 2rem;
  color: rgba(255,255,255,0.8);
  font-size: 1.14rem;
  line-height: 1.75;
}
.meme-arcade-cta {
  display: inline-flex;
  align-items: center;
  gap: 0.65rem;
  padding: 16px 36px;
  border-radius: 999px;
  background: linear-gradient(135deg, #f04dff, #00d4ff);
  box-shadow: 0 0 32px rgba(234, 56, 255, 0.35), 0 0 44px rgba(0, 212, 255, 0.16);
  color: #08000f;
  font-size: 1.05rem;
  font-weight: 800;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.meme-arcade-cta:hover,
.meme-arcade-cta:focus-visible {
  transform: translateY(-3px);
  box-shadow: 0 0 46px rgba(234, 56, 255, 0.56), 0 0 68px rgba(0, 212, 255, 0.3);
}
.meme-arcade-gallery {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.5rem;
  margin-top: 4rem;
}
.meme-arcade-screen-card {
  margin: 0;
}
.meme-arcade-screen-card img {
  display: block;
  width: min(100%, 255px);
  height: auto;
  margin: 0 auto;

  border-radius: 22px;
  box-shadow: 0 20px 45px rgba(0,0,0,0.48), 0 0 28px rgba(0, 212, 255, 0.14);
}
.meme-arcade-screen-card figcaption {
  margin-top: 0.9rem;
  color: rgba(255,255,255,0.78);
  font-size: 0.95rem;
  font-weight: 600;
}

/* Waken AI Featured Callout */
.waken-callout {
  padding: 6rem 4rem;
  background: linear-gradient(180deg, #000 0%, #051015 50%, #000 100%);
  position: relative;
  overflow: hidden;


}
.waken-callout::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 800px;
  height: 800px;
  background: radial-gradient(ellipse at center, rgba(0,212,255,0.08) 0%, transparent 60%);
  pointer-events: none;
}
.waken-inner {
  max-width: 1000px;
  margin: 0 auto;
  position: relative;
  z-index: 1;
}
.waken-header {
  text-align: center;
  margin-bottom: 3rem;
}
.waken-logo {
  max-width: 280px;
  height: auto;
  filter: invert(1) brightness(1.2);
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
}
.waken-logo:hover {
  filter: invert(1) brightness(1.4);
  transform: scale(1.02);
}
.waken-tagline {
  font-family: 'Playfair Display', serif;
  font-size: 1.8rem;
  color: rgba(255,255,255,0.9);
  margin-bottom: 0.5rem;
}
.waken-subtitle {
  color: rgba(255,255,255,0.5);
  font-size: 1rem;
  margin-bottom: 1.5rem;
}
.waken-description {
  font-size: 1.1rem;
  line-height: 1.8;
  color: rgba(255,255,255,0.7);
  max-width: 700px;
  margin: 0 auto 2rem;
  text-align: center;
}
.waken-video-container {
  position: relative;
  padding-top: 56.25%;
  background: linear-gradient(135deg, #0a0a0a 0%, #0a1520 100%);
  border-radius: 16px;
  overflow: hidden;
  max-width: 900px;
  margin: 0 auto 2rem;
  box-shadow: 0 20px 60px rgba(0,212,255,0.15);

}
.waken-video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;

}
.waken-quote {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-size: 1.2rem;
  color: rgba(255,255,255,0.6);
  text-align: center;
  margin-bottom: 1.5rem;
  padding: 0 2rem;
}
.waken-positioning {
  font-size: 0.95rem;
  color: #00D4FF;
  font-weight: 500;
  text-align: center;
  margin-bottom: 2rem;
}
.waken-cta {
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

  transition: all 0.3s ease;
}
.waken-cta:hover {
  background: linear-gradient(135deg, rgba(0,212,255,0.25), rgba(139,92,246,0.25));
  box-shadow: 0 0 30px rgba(0, 212, 255, 0.3);
  transform: translateY(-2px);
}
.waken-footer {
  text-align: center;
  margin-top: 2rem;
}

/* Waken Callout Mobile */
@media (max-width: 768px) {
  .waken-callout {
    padding: 3rem 16px;
  }
  .waken-logo {
    max-width: 200px;
  }
  .waken-tagline {
    font-size: 1.4rem;
  }
  .waken-video-container {
    border-radius: 0;
    margin: 0 -16px 2rem;
    max-width: calc(100% + 32px);
  }
}

/* Apple WWDC14 Ultrakam Recognition */
.wwdc14-feature {
  padding: 6rem 4rem;
  background: linear-gradient(135deg, #07111c 0%, #0a0a0a 55%, #10131b 100%);


}
.wwdc14-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(380px, 1.2fr);
  gap: 2.5rem 4rem;
  align-items: center;
}
.wwdc14-eyebrow {
  color: #00D4FF;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}
.wwdc14-copy h2 {
  margin: 0.7rem 0;
  color: #fff;
  font-family: 'Playfair Display', serif;
  font-size: clamp(2.15rem, 4vw, 3.5rem);
  line-height: 1.08;
}
.wwdc14-subtitle {
  color: #00D4FF;
  font-size: 1.1rem;
  font-weight: 600;
  line-height: 1.5;
}
.wwdc14-description {
  margin-top: 1.25rem;
  color: rgba(255, 255, 255, 0.73);
  font-size: 1.05rem;
  line-height: 1.75;
}
.wwdc14-copy blockquote {
  margin: 1.5rem 0;
  padding-left: 1.1rem;

  color: #fff;
  font-family: 'Playfair Display', serif;
  font-size: 1.25rem;
  font-style: italic;
  line-height: 1.45;
}
.wwdc14-journey {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  margin: 1.5rem 0;
}
.wwdc14-journey span {
  display: inline-flex;
  align-items: center;
  padding: 0.45rem 0.7rem;

  border-radius: 999px;
  color: rgba(255, 255, 255, 0.72);
  font-size: 0.78rem;
}
.wwdc14-journey span:not(:last-child)::after {
  content: '→';
  margin-left: 0.65rem;
  color: #00D4FF;
}
.wwdc14-actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.8rem;
}
.wwdc14-btn {
  display: inline-flex;
  padding: 0.8rem 1rem;

  border-radius: 6px;
  color: #00D4FF;
  font-size: 0.84rem;
  font-weight: 700;
  transition: background 0.25s ease, transform 0.25s ease;
}
.wwdc14-btn-primary {
  background: #00D4FF;

  color: #00131a;
}
.wwdc14-text-link {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.85rem;
}
.wwdc14-btn:hover,
.wwdc14-btn:focus-visible {
  background: rgba(0, 212, 255, 0.16);
  transform: translateY(-2px);
}
.wwdc14-btn-primary:hover,
.wwdc14-btn-primary:focus-visible {
  background: #5be6ff;
}
.wwdc14-text-link:hover,
.wwdc14-text-link:focus-visible {
  color: #00D4FF;
}
.wwdc14-visuals {
  position: relative;
}
.wwdc14-slide-link {
  display: block;
  color: rgba(255, 255, 255, 0.58);
  font-size: 0.78rem;
  text-align: center;
}
.wwdc14-slide {
  display: block;
  width: 100%;
  height: auto;

  border-radius: 8px;
  box-shadow: 0 22px 55px rgba(0, 0, 0, 0.42);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.wwdc14-slide-link:hover .wwdc14-slide,
.wwdc14-slide-link:focus-visible .wwdc14-slide {
  box-shadow: 0 24px 60px rgba(0, 0, 0, 0.5), 0 0 35px rgba(0, 212, 255, 0.18);
  transform: translateY(-4px);
}
.wwdc14-icon-proof {
  position: absolute;
  right: -1rem;
  bottom: -1.7rem;
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.7rem;
  background: #07111c;

  border-radius: 8px;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.45);
}
.wwdc14-icon-proof img {
  width: 76px;
  height: 76px;
  border-radius: 10px;
}
.wwdc14-icon-proof p {
  color: rgba(255, 255, 255, 0.72);
  font-size: 0.74rem;
  line-height: 1.45;
}
.wwdc14-icon-proof strong {
  color: #00D4FF;
}
.wwdc14-proof {
  grid-column: 1 / -1;
  overflow: hidden;

  border-radius: 8px;
  background: rgba(255, 255, 255, 0.035);
}
.wwdc14-proof summary {
  padding: 1rem 1.25rem;
  color: #fff;
  cursor: pointer;
  font-weight: 600;
}
.wwdc14-proof summary::marker {
  color: #00D4FF;
}
.wwdc14-proof-content {
  padding: 0 1.25rem 1.25rem;
}
.wwdc14-proof-content p {
  margin-bottom: 1rem;
  color: rgba(255, 255, 255, 0.65);
  line-height: 1.65;
}
.wwdc14-proof-content img {
  display: block;
  width: min(100%, 860px);

}
@media (max-width: 768px) {
  .wwdc14-feature {
    padding: 4rem 16px;
  }
  .wwdc14-inner {
    grid-template-columns: 1fr;
    gap: 2rem;
  }
  .wwdc14-icon-proof {
    position: static;
    width: fit-content;
    margin: 1rem auto 0;
  }
  .wwdc14-proof {
    grid-column: auto;
  }
  .wwdc14-journey span:not(:last-child)::after {
    content: '';
    margin: 0;
  }
}

/* AI Copyright Weights Citations */
.featured-book-section {
  padding: 6rem 4rem;
  background: linear-gradient(135deg, #080b12 0%, #0b1930 52%, #10101d 100%);


}
.featured-book-inner {
  max-width: 1080px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(250px, 0.62fr);
  align-items: center;
  gap: 3rem 5rem;
}
.featured-book-section--cover-first .featured-book-copy {
  grid-column: 2;
  grid-row: 1;
}
.featured-book-section--cover-first .featured-book-cover-link {
  grid-column: 1;
  grid-row: 1;
}
.featured-book-eyebrow {
  display: block;
  color: #00D4FF;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}
.featured-book-copy h2 {
  margin: 0.65rem 0 0.9rem;
  color: #fff;
  font-family: 'Playfair Display', serif;
  font-size: clamp(2rem, 4.6vw, 3.55rem);
  line-height: 1.08;
}
.featured-book-subtitle {
  margin-bottom: 1.25rem;
  color: rgba(0,212,255,0.84);
  font-size: 1.05rem;
  line-height: 1.5;
}
.featured-book-description {
  max-width: 650px;
  color: rgba(255,255,255,0.76);
  font-size: 1.05rem;
  line-height: 1.75;
}
.featured-book-cta {
  display: inline-flex;
  gap: 0.5rem;
  margin-top: 1.75rem;
  padding: 13px 26px;

  border-radius: 999px;
  color: #00D4FF;
  font-weight: 700;
  transition: background 0.25s ease, box-shadow 0.25s ease, transform 0.25s ease;
}
.featured-book-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.9rem;
  margin-top: 1.75rem;
}
.featured-book-cta {
  margin-top: 0;
}
.featured-book-ebook {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 13px 26px;

  border-radius: 999px;
  color: rgba(255,255,255,0.9);
  font-weight: 700;
  transition: background 0.25s ease, border-color 0.25s ease, transform 0.25s ease;
}
.featured-book-cover-link {
  display: block;
  justify-self: center;
}
.featured-book-cover {
  display: block;
  width: min(100%, 330px);
  height: auto;

  box-shadow: 0 24px 55px rgba(0,0,0,0.45), 0 0 35px rgba(0,212,255,0.12);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.featured-book-cta:hover,
.featured-book-cta:focus-visible {
  background: rgba(0,212,255,0.12);
  box-shadow: 0 0 28px rgba(0,212,255,0.18);
  transform: translateY(-2px);
}
.featured-book-ebook:hover,
.featured-book-ebook:focus-visible {

  background: rgba(255,255,255,0.08);
  transform: translateY(-2px);
}
.featured-book-cover-link:hover .featured-book-cover,
.featured-book-cover-link:focus-visible .featured-book-cover {
  box-shadow: 0 28px 65px rgba(0,0,0,0.5), 0 0 42px rgba(0,212,255,0.28);
  transform: translateY(-4px);
}
@media (max-width: 768px) {
  .featured-book-section {
    padding: 4rem 16px;
  }
  .featured-book-inner {
    grid-template-columns: 1fr;
    gap: 2rem;
    justify-items: center;
  }
  .featured-book-copy {
    text-align: center;
  }
  .featured-book-actions {
    justify-content: center;
  }
  .featured-book-cover-link {
    width: fit-content;
    justify-self: center;
    margin-inline: auto;
  }
  .featured-book-section--cover-first .featured-book-copy,
  .featured-book-section--cover-first .featured-book-cover-link {
    grid-column: auto;
    grid-row: auto;
  }
  .featured-book-cover-link {
    grid-row: 2;
  }
  .featured-book-section--cover-first .featured-book-copy {
    grid-row: 1;
  }
  .featured-book-section--cover-first .featured-book-cover-link {
    grid-row: 2;
  }
  .featured-book-cover {
    width: min(100%, 290px);
    margin-inline: auto;
  }
}

.citations-section {
  padding: 6rem 4rem;
  background: linear-gradient(135deg, #061522 0%, #080b12 55%, #10101d 100%);


}
.citations-inner {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(260px, 0.72fr);
  gap: 2rem 4rem;
  align-items: center;
}
.citations-intro {
  max-width: 620px;
}
.citations-eyebrow,
.citation-source {
  display: block;
  color: #00D4FF;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}
.citations-intro h2 {
  margin: 0.65rem 0 1.15rem;
  color: #fff;
  font-family: 'Playfair Display', serif;
  font-size: clamp(2.25rem, 5vw, 3.75rem);
  line-height: 1.05;
}
.citations-intro p {
  color: rgba(255,255,255,0.76);
  font-size: 1.08rem;
  line-height: 1.75;
}
.citations-intro .citations-context {
  margin-top: 1rem;
  color: rgba(255,255,255,0.52);
  font-size: 0.95rem;
}
.citations-cta {
  display: inline-flex;
  margin-top: 1.75rem;
  padding: 13px 26px;

  border-radius: 999px;
  color: #00D4FF;
  font-weight: 700;
  transition: background 0.25s ease, box-shadow 0.25s ease, transform 0.25s ease;
}
.citations-cover-link {
  display: block;
  color: rgba(255,255,255,0.65);
  font-size: 0.85rem;
  text-align: center;
}
.citations-cover {
  display: block;
  width: min(100%, 360px);
  height: auto;
  margin: 0 auto 1rem;

  box-shadow: 0 24px 55px rgba(0,0,0,0.45), 0 0 35px rgba(0,212,255,0.12);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.citation-house-card {
  grid-column: 1 / -1;
  display: block;
  padding: 2rem;
  background: rgba(0,212,255,0.06);

  border-radius: 12px;
}
.citation-house-card h3,
.citation-card h3 {
  margin: 0.65rem 0;
  color: #fff;
  font-family: 'Playfair Display', serif;
  line-height: 1.25;
}
.citation-house-card h3 {
  font-size: 1.5rem;
}
.citation-house-card p {
  margin-bottom: 1rem;
  color: rgba(255,255,255,0.66);
}
.citation-grid {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
.citation-card {
  display: flex;
  min-height: 170px;
  padding: 1.5rem;
  flex-direction: column;

  border-radius: 10px;
  background: rgba(255,255,255,0.035);
}
.citation-card h3 {
  font-size: 1.08rem;
}
.citation-link {
  display: block;
  margin-top: auto;
  color: #00D4FF;
  font-size: 0.88rem;
  font-weight: 600;
}
.citations-cta:hover,
.citations-cta:focus-visible {
  background: rgba(0,212,255,0.12);
  box-shadow: 0 0 28px rgba(0,212,255,0.18);
  transform: translateY(-2px);
}
.citations-cover-link:hover .citations-cover,
.citations-cover-link:focus-visible .citations-cover {
  box-shadow: 0 28px 65px rgba(0,0,0,0.5), 0 0 42px rgba(0,212,255,0.28);
  transform: translateY(-4px);
}
.citation-house-card:hover,
.citation-house-card:focus-visible,
.citation-card:hover,
.citation-card:focus-visible {

  background: rgba(0,212,255,0.09);
}
@media (max-width: 768px) {
  .citations-section {
    padding: 4rem 16px;
  }
  .citations-inner {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }
  .citations-cover {
    width: min(100%, 315px);
  }
  .citation-house-card,
  .citation-grid {
    grid-column: auto;
  }
  .citation-grid {
    grid-template-columns: 1fr;
  }
}

/* AI Art Row (before Books) */
.ai-art-row {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  padding: 2rem;
  max-width: 1000px;
  margin: 0 auto;
}
.art-video {
  border-radius: 12px;
  overflow: hidden;
}
.art-video iframe {
  width: 100%;
  aspect-ratio: 16/9;
  border-radius: 8px;
  box-shadow: 0 20px 60px rgba(0,212,255,0.15);

}

/* Interviews Section */
.interviews-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 1.5rem;
  padding: 2rem 2rem 0 2rem;
  max-width: 1200px;
  margin: 0 auto;
}
.interview-card {
  background: #0a0a0a;
  border-radius: 12px;
  overflow: hidden;

  transition: all 0.3s ease;
}
.interview-card:hover {

  box-shadow: 0 0 20px rgba(0, 212, 255, 0.1);
}
.interview-card iframe {
  width: 100%;
  aspect-ratio: 16/9;
  box-shadow: 0 20px 60px rgba(0,212,255,0.15);

}
.interview-info {
  padding: 1rem;
}
.interview-info h4 {
  color: #fff;
  font-family: 'Playfair Display', serif;
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}
.interview-info p {
  color: #888;
  font-size: 0.85rem;
}

/* Responsive - Mobile Full Width for Video Sections */
@media (max-width: 768px) {
  /* Hero portrait - larger on mobile */
  .hero-portrait img {
    width: 220px;
    height: 300px;
    border-radius: 12px;
  }

  /* Full width cards - NO padding, full bleed */
  .impact-card, .project-card {
    grid-template-columns: 1fr;
    direction: ltr !important;
    padding: 0;
    gap: 0;
    margin: 0;
  }
  .impact-card > *, .project-card > * {
    direction: ltr !important;
  }
  .impact-card .card-content,
  .project-card .card-content {
    padding: 16px;
  }

  /* Full width video iframes - truly edge to edge */
  .impact-card .card-video,
  .project-card .card-video,
  .innovation-card .card-video {
    margin: 0;
    width: 100%;
  }
  .impact-card .card-video iframe,
  .project-card .card-video iframe,
  .innovation-card .card-video iframe {
    border-radius: 0;
  }

  /* Innovation grid - full width */
  .innovation-grid {
    grid-template-columns: 1fr;
    padding: 0;
    gap: 0;
  }
  .innovation-card {
    border-radius: 0;
    margin: 0;
    width: 100%;
  }
  .innovation-card .card-content {
    padding: 16px;
  }

  /* Interviews grid full width */
  .interviews-grid {
    grid-template-columns: 1fr;
    padding: 0;
    gap: 0;
    max-width: 100%;
  }
  .interview-card {
    border-radius: 0;
    margin: 0;
    width: 100%;
  }
  .interview-card iframe {
    border-radius: 0;
  }
  .interview-info {
    padding: 12px 16px;
  }

  /* Filmography full width */
  .filmography .film-grid {
    grid-template-columns: 1fr;
    padding: 0;
    gap: 0;
  }
  .film-video {
    margin: 0;
    width: 100%;
  }
  .film-video iframe {
    border-radius: 0;
  }
  .film-video .video-title {
    padding: 8px 16px;
  }

  /* Bio section padding */
  .bio-section {
    padding: 3rem 16px;
  }
  .bio-headline {
    font-size: 1.8rem;
  }

  /* ClineFlow padding */
  .clineflow-callout {
    padding: 0 0 3rem;
  }
  .clineflow-inner {
    padding: 3rem 16px 0;
  }
  .clineflow-title {
    font-size: 2.5rem;
  }
  .clineflow-features {
    grid-template-columns: 1fr;
  }
  .meme-arcade-callout {
    padding: 4rem 16px;
  }
  .meme-arcade-icon {
    width: min(100%, 170px);
  }
  .meme-arcade-gallery {
    grid-template-columns: 1fr;
    gap: 2.5rem;
    margin-top: 3rem;
  }
  .meme-arcade-screen-card img {
    width: min(100%, 280px);
  }

  /* Section headers - minimal padding */
  .section-header {
    padding: 0 16px;
  }

  /* Section padding */
  .section {
    padding: 60px 0;
  }

  /* AI Art Row full width */
  .ai-art-row {
    grid-template-columns: 1fr;
    padding: 0;
    gap: 0;
    max-width: 100%;
  }
  .art-video {
    border-radius: 0;
    margin: 0;
    width: 100%;
  }
  .art-video iframe {
    border-radius: 0;
  }

  /* Books grid - single column on mobile */
  .books-grid {
    grid-template-columns: 1fr;
    padding: 0 16px;
  }
  .book-card:last-child:nth-child(odd) {
    grid-column: auto;
    width: auto;
  }

  /* Press grids - some padding */
  .press-grid {
    padding: 0 16px;
  }

}

/* Selected Work gateway */
.selected-work-gateway {
  padding: 88px 24px;
  background: #050505;

}
.selected-work-gateway-inner {
  max-width: 960px;
  margin: 0 auto;
  text-align: center;
}
.selected-work-gateway h2 {
  margin: 14px 0 36px;
  font-family: 'Playfair Display', serif;
  font-size: clamp(2.2rem, 4vw, 3.75rem);
  color: #fff;
}
.selected-work-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
}
.selected-work-link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 62px;
  padding: 0 20px;
  color: #eaf8ff;

  border-radius: 8px;
  text-decoration: none;
  font-size: 0.95rem;
  transition: border-color 180ms ease, background 180ms ease, color 180ms ease;
}
.selected-work-link span {
  color: #00c2ff;
  font-size: 1.2rem;
}
.selected-work-link:hover,
.selected-work-link:focus-visible {
  color: #fff;
  background: rgba(0, 194, 255, 0.1);

  outline: none;
}
@media (max-width: 700px) {
  .selected-work-gateway { padding: 64px 16px; }
  .selected-work-grid { grid-template-columns: 1fr; }
}

/* Persistent booking CTA */
:root {
  --booking-bar-height: 72px;
}
body {
  padding-bottom: calc(var(--booking-bar-height) + 32px + env(safe-area-inset-bottom));
}
.booking-call-bar {
  position: fixed;
  z-index: 998;
  left: 50%;
  bottom: max(16px, env(safe-area-inset-bottom));
  width: min(calc(100% - 32px), 900px);
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 11px 11px 11px 22px;

  border-radius: 18px;
  background: rgba(8, 8, 12, 0.88);
  box-shadow: 0 18px 60px rgba(0, 0, 0, 0.5), 0 0 32px rgba(0, 212, 255, 0.08);
  -webkit-backdrop-filter: blur(18px) saturate(140%);
  backdrop-filter: blur(18px) saturate(140%);
}
.booking-call-copy {
  min-width: 0;
}
.booking-call-title {
  display: block;
  color: #fff;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: clamp(0.95rem, 1.6vw, 1.08rem);
  font-weight: 600;
  line-height: 1.3;
}
.booking-call-charity {
  display: block;
  margin-top: 0.12rem;
  color: #00d4ff;
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.025em;
  text-decoration: none;
}
.booking-call-charity:hover,
.booking-call-charity:focus-visible {
  color: #fff;
  text-decoration: underline;
}
.booking-call-cta {
  flex: 0 0 auto;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5em;
  min-height: 50px;
  padding: 0 22px;

  border-radius: 12px;
  background: linear-gradient(135deg, #00d4ff, #8b5cf6);
  color: #050505;
  font-size: 0.86rem;
  font-weight: 700;
  letter-spacing: 0.01em;
  white-space: nowrap;
  box-shadow: 0 8px 24px rgba(0, 212, 255, 0.18);
  transition: transform 180ms ease, box-shadow 180ms ease, filter 180ms ease;
}
.booking-call-cta .fa-video {
  font-size: 0.96em;
}
.booking-call-arrow {
  margin-left: 0.05em;
}
.booking-call-cta:hover,
.booking-call-cta:focus-visible {
  color: #050505 !important;
  filter: brightness(1.08);
  transform: translateY(-1px);
  box-shadow: 0 10px 30px rgba(0, 212, 255, 0.28);
  outline: 2px solid #fff;
  outline-offset: 3px;
}
@media (max-width: 640px) {
  :root { --booking-bar-height: 105px; }
  body {
    padding-bottom: calc(var(--booking-bar-height) + 20px + env(safe-area-inset-bottom));
  }
  .booking-call-bar {
    bottom: max(10px, env(safe-area-inset-bottom));
    width: calc(100% - 20px);
    display: grid;
    justify-content: stretch;
    gap: 9px;
    padding: 12px;
    border-radius: 16px;
  }
  .booking-call-copy {
    padding: 0 3px;
  }
  .booking-call-title {
    font-size: 0.95rem;
  }
  .booking-call-cta {
    width: auto;
    min-height: 48px;
    border-radius: 11px;
  }
}
@media (prefers-reduced-motion: reduce) {
  .booking-call-cta { transition: none; }
}
'''

SIGNAL_STYLES = r'''
/* Signal & Craft: a shared editorial system with dimensional accents. */
:root {
  --ink: #070a0e; --surface: #0e141b; --line: #25313c;
  --paper: #f3f5f7; --muted: #a3b0bd; --cyan: #75e1f4;
  --blue: #75e1f4; --purple: #9e89ff;
  --ease: cubic-bezier(.2,.75,.2,1); --header-height: 82px;
}
html { scroll-padding-top: calc(var(--header-height) + 24px); }
body { background: var(--ink); color: var(--paper); padding: 0; overflow-wrap: break-word; }
[hidden] { display: none !important; }
main { outline: none; }
main > *, footer { scroll-margin-top: calc(var(--header-height) + 24px); }
main section[id], main article[id], footer[id] { scroll-margin-top: 0; }
button, a { -webkit-tap-highlight-color: transparent; }
button { font: inherit; cursor: pointer; }
a { color: var(--cyan); }
a:focus-visible, button:focus-visible, summary:focus-visible { outline: 2px solid var(--cyan); outline-offset: 5px; }
h1, h2, h3 { text-wrap: balance; }
p { text-wrap: pretty; }
img { max-width: 100%; }
.skip-link { position: fixed; top: -100px; left: 16px; z-index: 3000; background: var(--cyan); color: #070a0e; padding: 12px 24px; }
.skip-link:focus { top: 12px; }
.site-header { position: sticky; top: 0; z-index: 1000;  background: rgba(7,10,14,.96); }
.site-nav { width: min(1320px, calc(100% - 96px)); margin: auto; min-height: var(--header-height); display: flex; align-items: center; gap: 30px; }
.site-nav a { text-transform: none; letter-spacing: 0; padding: 12px 0; font-size: .875rem; color: #c8d1d9; }
.site-nav .site-identity { display: flex; gap: 14px; align-items: center; margin-right: auto; font-size: .9rem; color: var(--paper); font-weight: 600; }
.identity-mark { font-family: 'Playfair Display', Georgia, serif; font-size: 2.1rem; letter-spacing: -.08em; color: var(--cyan); line-height: 1; }
.desktop-links { display: flex; gap: 28px; align-items: center; }
.site-nav .header-book {  border-radius: 4px; padding: 11px 17px; color: var(--paper); }
.header-book span { margin-left: 16px; }
.menu-toggle, .menu-close {  background: var(--surface); color: var(--paper); padding: 11px 14px; min-height: 44px; border-radius: 4px; }
.menu-toggle { display: none; }
.signal-menu { position: fixed; inset: 0; width: 100%; max-width: 100%; max-height: 100dvh; height: 100dvh; margin: 0;  padding: 24px; color: var(--paper); background: var(--ink); overflow-y: auto; }
.signal-menu::backdrop { background: #070a0e; }
.menu-heading { display: flex; align-items: center; justify-content: space-between; gap: 20px; margin-bottom: 32px; }
.menu-heading h2 { font-size: 2rem; }
.signal-menu nav { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 24px; }
.signal-menu nav a { font-size: .875rem; letter-spacing: .04em; color: #c8d1d9; padding: 16px 8px;  min-height: 48px; }
.noscript-nav { padding: 16px; display: flex; flex-wrap: wrap; gap: 16px; }
.signal-hero { isolation: isolate; position: relative; overflow: clip; background: radial-gradient(ellipse at 82% 35%, #123044 0%, transparent 49%), var(--ink); }
.signal-hero-inner { max-width: 1320px; margin: auto; padding: 88px 48px 76px; display: grid; grid-template-columns: 1.22fr 1fr; gap: 72px; align-items: center; }
.signal-eyebrow { font-size: .75rem; letter-spacing: .16em; color: var(--cyan); font-weight: 600; margin: 0 0 28px; display: flex; align-items: center; gap: 12px; }
.signal-eyebrow > span { width: 6px; height: 6px; background: var(--cyan); display: inline-block; }
.signal-copy h1 { font-family: 'Playfair Display', Georgia, serif; font-weight: 400; font-size: clamp(3.4rem, 6.5vw, 6rem); line-height: 1.05; letter-spacing: -.055em; margin: 0 0 32px; }
.signal-copy h1 em, .work-intro h1 em, .contact-callout h2 em { font-weight: 400; color: var(--cyan); }
.signal-position { font-size: clamp(1.4rem, 2.25vw, 2rem); line-height: 1.35; letter-spacing: -.03em; margin-bottom: 20px; }
.signal-position span { color: var(--cyan); }
.signal-summary { font-size: 1rem; color: #acbac6; line-height: 1.85; max-width: 480px; }
.signal-actions { display: flex; align-items: center; flex-wrap: wrap; gap: 20px 24px; margin-top: 30px; }
.signal-button { display: inline-flex; align-items: center; justify-content: center; gap: 24px; min-height: 50px; padding: 14px 22px; background: var(--cyan);  border-radius: 4px; color: #071015; font-size: .875rem; line-height: 1.45; font-weight: 600; transition: background 180ms var(--ease), box-shadow 180ms var(--ease); }
.signal-button:hover { background: #b1f2fc; color: #071015; box-shadow: 0 0 26px #75e1f425; }
.signal-text-link { font-size: .875rem; color: var(--paper); padding: 12px 0; min-height: 44px; }
.signal-text-link span { color: var(--cyan); margin-left: 10px; }
.hero-footnote { color: #91a1b0; font-size: .75rem; margin-top: 20px; }
.portrait-stage { position: relative; perspective: 1000px; width: min(100%, 400px); margin: 0 auto; padding: 30px 20px 0; }
.portrait-window { position: relative;  border-radius: 3px; overflow: hidden; background: #172430; box-shadow: 20px 24px 60px #0008; }
.portrait-window img { display: block; width: 100%; height: auto; aspect-ratio: 4/5; object-fit: cover; object-position: 50% 28%; filter: saturate(.65); }
.depth-rig { position: absolute; inset: 0 0 44px; pointer-events: none; transform-style: preserve-3d; transform: rotateX(var(--tilt-x, 0deg)) rotateY(var(--tilt-y, 0deg)); }
.depth-plane { position: absolute; inset: 18px 10px;  border-radius: 3px; }
.plane-back { transform: translateZ(-55px) rotate(-10deg); background: linear-gradient(150deg,#75e1f409,#9e89ff18);  }
.plane-middle { transform: translateZ(-25px) rotate(7deg); background: linear-gradient(120deg,#75e1f418, transparent 60%); }
.plane-front { transform: translateZ(22px) rotate(-3deg);  }
.portrait-stage figcaption { display: flex; flex-direction: column; gap: 7px; margin-top: 22px; padding-left: 12px;  font-size: .75rem; color: var(--muted); }
.portrait-stage figcaption span:first-child { font-size: .75rem; letter-spacing: .15em; color: #e2e8ed; }
.stage-index { position: absolute; right: -14px; top: 28%; writing-mode: vertical-rl; font-size: .75rem; letter-spacing: .2em; color: #97b6c7; }
.hero-baseline { max-width: 1320px; margin: auto;  padding: 22px 48px; display: flex; justify-content: space-between; gap: 24px; font-size: .75rem; letter-spacing: .14em; color: #93a5b3; }
.hero-baseline a { color: var(--cyan); }
.proof-section { max-width: 1224px; margin: auto; padding: 52px 0 0; }
.proof-section .stats-row { display: grid; grid-template-columns: repeat(4,1fr); gap: 0; margin: 0; padding: 0; }
.stat-item { text-align: left; padding: 4px 32px;  }
.stat-item:first-child { padding-left: 0; }
.stat-item:last-child {  }
.stat-item .value { font-size: clamp(2rem,4vw,3.5rem); color: var(--paper); font-weight: 400; letter-spacing: -.04em; line-height: 1.15; }
.stat-item .label { font-size: .75rem; color: var(--muted); letter-spacing: .13em; margin-top: 10px; }
.proof-press { display: flex; gap: 40px; align-items: center; padding: 38px 0; margin-top: 38px;   }
.proof-press > a { flex-shrink: 0; font-size: .75rem; letter-spacing: .1em; }
.proof-logos { display: flex; justify-content: space-between; align-items: center; gap: 24px; flex: 1; flex-wrap: wrap; }
.proof-logos .press-logo-item { flex: 0 1 100px; padding: 0; }
.proof-logos .press-logo-item img { width: 100%; height: 30px; object-fit: contain; filter: grayscale(1) brightness(1.6); opacity: .7; }
.selected-work-gateway { background: var(--ink); padding: 80px 48px; }
.selected-work-gateway-inner { max-width: 1224px; margin: auto; }
.selected-work-gateway h2 { text-align: left; font-size: clamp(2rem,3vw,3rem); font-weight: 400; margin-bottom: 28px; }
.selected-work-gateway .eyebrow { display: block; text-align: left; font-size: .75rem; }
.selected-work-grid { display: grid; grid-template-columns: repeat(3,minmax(0,1fr)); gap: 12px; }
.selected-work-link { background: var(--surface);  border-radius: 4px; padding: 24px; min-height: 88px; font-size: 1rem; color: var(--paper); }
.selected-work-link:hover { transform: none; background: #14232e;  }
/* Product chapters: stable media with dimensional frames and generous typography. */
.clineflow-installer, .meme-arcade-callout, .wwdc14-feature, .citations-section, .professional-profile, .bio-section, .waken-callout { background: var(--ink);  }
.clineflow-installer { padding: 80px 48px; }
.clineflow-installer-shell { max-width: 1224px; margin: auto; display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center; overflow: visible;  background: transparent; box-shadow: none; }
.clineflow-installer-hero { order: 2; position: relative;  border-radius: 4px; box-shadow: 12px 18px 38px #0006; }
.clineflow-installer-hero img { width: 100%; height: auto; display: block; }
.clineflow-installer-inner { padding: 0; text-align: left; min-width: 0; }
.clineflow-installer-inner h2 { font-size: clamp(2rem,3.1vw,3rem); line-height: 1.2; letter-spacing: -.025em; margin: 20px 0 28px; }
.clineflow-installer-inner h2 span { color: var(--cyan); }
.clineflow-wordmark { font-size: .875rem; letter-spacing: .12em; text-transform: uppercase; }
.clineflow-installer-panel { padding: 22px; background: #0e1720;  border-radius: 4px; text-align: left; }
.clineflow-prompt-wrap { display: flex; flex-wrap: wrap; gap: 16px; }
.clineflow-prompt-wrap code { flex-basis: 100%; min-width: 0; overflow-wrap: anywhere; white-space: normal; font-size: .875rem; }
.clineflow-copy-button { position: static; min-height: 44px; transform: none; }
.copy-status { color: var(--cyan); font-size: .875rem; align-self: center; }
.clineflow-agent-compatibility { margin: 24px 0; max-width: 420px; }
.clineflow-agent-compatibility figcaption { font-size: .75rem; }
.clineflow-masterclass { margin-top: 20px; padding: 0; }
.clineflow-masterclass p, .clineflow-masterclass-divider { display: none; }
.clineflow-masterclass-cta { font-size: 1rem; padding: 12px 0; background: transparent; box-shadow: none;  color: var(--cyan); }
.section, .wwdc14-feature, .citations-section, .professional-profile, .bio-section, .waken-callout { padding: 80px 48px; }
.section-header { max-width: 1224px; margin: 0 auto 44px; text-align: left; position: relative; padding: 0; }
.section-header::before { content: ''; display: block; width: 48px; height: 2px; background: var(--cyan); margin-bottom: 26px; transform-origin: left; }
.section-header h2, .wwdc14-copy h2, .citations-intro h2, .professional-profile-copy h2, .bio-headline { font-size: clamp(2rem,3.5vw,3.3rem); font-weight: 400; line-height: 1.2; }
.section-header .lead { font-size: 1.1rem; color: var(--muted); max-width: 620px; }
.eyebrow { color: var(--cyan); font-size: .75rem; }
.impact-card, .project-card {  background: #0c1117; border-radius: 5px; box-shadow: none; margin: 0 auto 40px; max-width: 1224px; overflow: visible; position: relative; }
.impact-card .card-video, .project-card .card-video { position: relative;  border-radius: 3px; overflow: hidden; box-shadow: 8px 14px 28px #0005; }
.impact-card:hover, .project-card:hover { transform: none; box-shadow: none; }
.card-content { min-width: 0; }
.card-content h3 { font-weight: 400; }
.card-content .highlight { white-space: normal; background: #14212c; color: #a9e8f3;  border-radius: 3px; box-shadow: none; }
.company-press-quote { background: transparent;  }
.books-grid, .press-grid, .interviews-grid { max-width: 1224px; margin-left: auto; margin-right: auto; padding: 0; grid-template-columns: repeat(3,minmax(0,1fr)); gap: 24px; }
.books-grid { grid-template-columns: repeat(2,minmax(0,1fr)); }
.book-card, .press-card, .citation-card, .citation-house-card, .interview-card { border-radius: 4px; background: #0e141b;  box-shadow: none; }
.book-card:hover, .press-card:hover, .interview-card:hover { transform: none; box-shadow: none;  }
.featured-book-section { background: transparent;  margin-bottom: 40px; }
.featured-book-cover-link:hover .featured-book-cover, .citations-cover-link:hover .citations-cover { transform: none; }
.featured-book-inner { padding-left: 0; padding-right: 0; }
.bio-headline { max-width: 840px; margin-left: auto; margin-right: auto; }
.quote-section { background: #0b1118; padding: 80px 48px; }
.quote-section blockquote { max-width: 850px; font-size: clamp(1.5rem,2.8vw,2.4rem); }
.professional-profile { border-radius: 0; }
.professional-profile-viewer { min-width: 0; }
.work-intro { position: relative; isolation: isolate; overflow: clip; background: radial-gradient(ellipse at 90% 60%,#123044,transparent 60%); padding: 90px 48px 76px; }
.work-intro-inner { max-width: 1224px; margin: auto; position: relative; z-index: 1; }
.work-intro h1 { font-family: 'Playfair Display',Georgia,serif; font-size: clamp(3.5rem,7vw,6.5rem); line-height: 1.05; font-weight: 400; letter-spacing: -.055em; margin: 0 0 28px; }
.work-intro p:not(.signal-eyebrow) { max-width: 510px; font-size: 1.1rem; color: var(--muted); }
.work-intro-meta { display: flex; gap: 24px; flex-wrap: wrap; margin-top: 36px; color: var(--cyan); font-size: .75rem; letter-spacing: .12em; }
.work-orbit { position: absolute; top: 16%; right: 12%; width: 340px; height: 340px; perspective: 1000px; pointer-events: none; }
.work-orbit span { position: absolute; inset: 0;  background: linear-gradient(130deg,#75e1f409,#9e89ff0d); transform: rotateY(-30deg) rotateX(25deg) rotateZ(-15deg); box-shadow: 0 0 50px #75e1f409; }
.work-orbit span:nth-child(2) { inset: 30px; transform: translateZ(45px) rotateY(-30deg) rotateX(25deg) rotateZ(-15deg);  }
.work-orbit span:nth-child(3) { inset: 60px; transform: translateZ(90px) rotateY(-30deg) rotateX(25deg) rotateZ(-15deg); }
.work-index { max-width: 1224px; padding: 28px 0; margin: auto; display: flex; flex-wrap: wrap; gap: 12px 32px;  }
.work-index a { display: flex; align-items: center; gap: 18px; min-height: 44px; font-size: .875rem; color: #c2cdd5; letter-spacing: 0; padding: 8px 0; text-transform: none; }
.work-index span { color: var(--cyan); }
.signal-footer { background: #0c131b; padding: 80px 48px 28px; text-align: left; }
.contact-callout { max-width: 1224px; margin: auto; display: grid; grid-template-columns: 1.5fr 1fr; gap: 60px; align-items: center; padding-bottom: 64px;  }
.contact-callout h2 { font-size: clamp(2rem,3.4vw,3.4rem); font-weight: 400; line-height: 1.2; margin-bottom: 22px; }
.contact-callout p:not(.signal-eyebrow) { max-width: 540px; color: var(--muted); font-size: 1rem; }
.contact-actions { display: flex; flex-direction: column; align-items: flex-start; gap: 16px; justify-self: end; }
.contact-actions > a:last-child { font-size: .875rem; color: var(--muted); min-height: 44px; display: flex; align-items: center; }
.footer-details { max-width: 1224px; margin: 50px auto; display: grid; grid-template-columns: 2fr 1fr; gap: 80px; }
.footer-details strong { font-size: 1.1rem; }
.footer-details p { text-align: left; font-size: .875rem !important; margin: 16px 0 !important; color: var(--muted) !important; }
.footer-links { display: flex; flex-wrap: wrap; align-content: start; gap: 12px 24px; }
.footer-links a { min-height: 44px; display: inline-flex; align-items: center; color: var(--paper); font-size: .875rem; }
#motion-toggle { display: block; flex-basis: 100%; text-align: left; background: none;   color: var(--cyan); margin-top: 8px; padding: 16px 0; min-height: 44px; font-size: .875rem; }
.signal-footer .copyright { max-width: 1224px; margin: auto; font-size: .75rem; }
/* Decoration responds independently of interactive content. */
.motion-frame { position: relative; isolation: isolate; }
.motion-frame::after { content: ''; position: absolute; inset: 0;  border-radius: inherit; pointer-events: none; z-index: 2; }
.motion-frame.is-arriving::after { animation: frame-light 900ms var(--ease) both; }
.section-header.is-arriving::before { animation: chapter-line 650ms var(--ease) both; }
html[data-motion-state="paused"] .is-arriving::after,
html[data-motion-state="paused"] .is-arriving::before,
.motion-offscreen::before, .motion-offscreen::after { animation-play-state: paused; }
@keyframes frame-light { 0% {  box-shadow: inset 20px 0 35px #75e1f400; } 35% {  box-shadow: inset 20px 0 35px #75e1f40f; } 100% {  box-shadow: inset -20px 0 35px #75e1f400; } }
@keyframes chapter-line { from { transform: scaleX(.1); } to { transform: scaleX(1); } }
html[data-reduced-motion="true"] *, html[data-reduced-motion="true"] *::before, html[data-reduced-motion="true"] *::after { animation: none !important; transition: none !important; scroll-behavior: auto !important; }
html[data-reduced-motion="true"] { scroll-behavior: auto; }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } *, *::before, *::after { animation: none !important; transition: none !important; scroll-behavior: auto !important; } }
@media (max-width: 1100px) {
  .site-nav { width: calc(100% - 48px); gap: 20px; }
  .desktop-links { gap: 18px; }
  .site-identity > span:last-child { display: none; }
  .signal-hero-inner { gap: 40px; padding: 64px 36px; }
  .proof-section, .work-index { margin-left: 36px; margin-right: 36px; }
  .work-orbit { right: 4%; width: 280px; height: 280px; }
}
@media (max-width: 800px) {
  :root { --header-height: 70px; }
  .site-nav { width: calc(100% - 40px); gap: 12px; }
  .site-nav .site-identity { gap: 10px; }
  .site-identity > span:last-child { display: inline; font-size: .75rem; }
  .desktop-links, .site-nav .header-book { display: none; }
  .menu-toggle { display: inline-flex; align-items: center; gap: 12px; font-size: .875rem; }
  .signal-hero-inner { grid-template-columns: 1fr; padding: 48px 24px 40px; gap: 46px; }
  .signal-copy h1 { font-size: clamp(3rem,10.5vw,4.6rem); margin-bottom: 24px; }
  .signal-eyebrow { font-size: .75rem; margin-bottom: 24px; letter-spacing: .13em; }
  .signal-position { font-size: 1.5rem; }
  .signal-summary { font-size: 1rem; max-width: 560px; line-height: 1.75; }
  .signal-actions { gap: 10px 22px; margin-top: 24px; }
  .portrait-stage { width: min(78%,320px); padding-top: 16px; }
  .portrait-window img { aspect-ratio: 4/4.5; }
  .plane-front { display: none; }
  .stage-index { right: -6px; }
  .hero-baseline { padding: 20px 24px; flex-wrap: wrap; font-size: .75rem; gap: 16px; }
  .hero-baseline > span:nth-child(2) { display: none; }
  .proof-section { margin: 0 24px; padding-top: 36px; }
  .proof-section .stats-row { grid-template-columns: repeat(2,1fr); row-gap: 24px; }
  .stat-item, .stat-item:first-child { padding: 4px 16px; }
  .stat-item:nth-child(odd) { padding-left: 0; }
  .stat-item:nth-child(even) {  }
  .stat-item .value { font-size: 2.3rem; }
  .stat-item .label { font-size: .75rem; }
  .proof-press { display: block; padding: 28px 0; margin-top: 30px; }
  .proof-logos { display: grid; grid-template-columns: repeat(3,minmax(0,1fr)); margin-top: 24px; gap: 20px; }
  .proof-logos .press-logo-item { min-width: 0; }
  .proof-logos .press-logo-item img { height: 24px; }
  .selected-work-gateway, .section, .wwdc14-feature, .citations-section, .professional-profile, .bio-section, .waken-callout, .clineflow-installer { padding: 56px 24px; }
  .selected-work-grid { grid-template-columns: 1fr; }
  .selected-work-link { min-height: 68px; padding: 18px 20px; }
  .clineflow-installer-shell { grid-template-columns: 1fr; gap: 32px; }
  .clineflow-installer-inner { order: 0; }
  .clineflow-installer-hero { order: 1; margin: 0 8px 8px 0; }
  .clineflow-installer-panel { padding: 18px; }
  .clineflow-installer-inner h2 { font-size: 2rem; }
  .section-header { margin-bottom: 32px; }
  .impact-card, .project-card { margin-bottom: 32px; overflow: hidden; }
  .impact-card .card-content, .project-card .card-content { padding: 24px; }
  .impact-card .card-video, .project-card .card-video { box-shadow: none;  }
  .books-grid, .press-grid, .interviews-grid { grid-template-columns: 1fr; gap: 24px; }
  .featured-book-inner { padding: 24px 0; }
  .work-intro { padding: 56px 24px; }
  .work-intro h1 { font-size: 4rem; }
  .work-intro p:not(.signal-eyebrow) { font-size: 1rem; }
  .work-intro-meta { gap: 16px; font-size: .75rem; }
  .work-orbit { opacity: .25; top: 20px; right: -120px; width: 240px; height: 240px; }
  .work-orbit span:nth-child(3) { display: none; }
  .work-index { margin: 0 24px; gap: 8px 22px; }
  .work-index a { font-size: .875rem; }
  .quote-section { padding: 56px 24px; }
  .signal-footer { padding: 56px 24px 24px; }
  .contact-callout { grid-template-columns: 1fr; gap: 16px; padding-bottom: 40px; }
  .contact-actions { justify-self: start; }
  .footer-details { grid-template-columns: 1fr; gap: 24px; margin: 36px auto; }
}
@media (hover: none), (pointer: coarse) {
  .depth-rig { transform: none; }
  .book-card:hover, .press-card:hover, .featured-book-cover-link:hover .featured-book-cover, .citations-cover-link:hover .citations-cover { transform: none; }
}
'''

SIGNAL_STYLES += r'''
/* Familiar press marquee, with an explicit pause control and static fallback. */
.proof-press { display: block; padding: 24px 0 28px; }
.press-strip-heading { display: flex; align-items: center; justify-content: space-between; gap: 16px; margin-bottom: 14px; }
.press-strip-heading > a { font-size: .75rem; letter-spacing: .12em; }
.press-pause { background: transparent;  color: #a3b0bd; font-size: .75rem; min-height: 44px; padding: 8px 0 8px 16px; }
.proof-marquee { overflow: hidden; padding: 12px 0; mask-image: linear-gradient(90deg,transparent,#000 7%,#000 93%,transparent); }
.proof-track { display: flex; width: max-content; }
.proof-logo-group { display: flex; gap: 52px; align-items: center; padding-right: 52px; }
.proof-logo-group .press-logo-item { width: 132px; flex: 0 0 132px; padding: 0; }
.proof-logo-group .press-logo-item img { width: 132px; height: 45px; object-fit: contain; opacity: .8; filter: grayscale(1) brightness(1.6); }
.proof-marquee.is-live .proof-track { animation: press-drift 44s linear infinite; }
.proof-marquee.is-paused .proof-track { animation-play-state: paused; }
.proof-marquee:not(.is-live) .logo-repeat { display: none; }
.proof-marquee:not(.is-live) { overflow-x: auto; mask-image: none; }
@keyframes press-drift { to { transform: translateX(-50%); } }
html[data-reduced-motion="true"] .proof-marquee { overflow-x: auto; mask-image: none; }
html[data-reduced-motion="true"] .logo-repeat { display: none; }
/* A single stable app viewer; all slides remain available without JavaScript. */
.meme-carousel { width: min(100%,350px); margin: 40px auto 0; }
.meme-carousel .meme-arcade-gallery { display: grid; grid-template-columns: 1fr; gap: 28px; margin: 0; }
.meme-carousel.is-carousel-live .meme-arcade-gallery { display: grid; grid-template-columns: 1fr; align-items: start; }
.meme-carousel .meme-arcade-screen-card { min-width: 0; }
.meme-carousel .meme-arcade-screen-card img { width: min(100%,300px); height: auto; aspect-ratio: 416/900; object-fit: contain; background: #090615; }
.meme-carousel figcaption { min-height: 2.7em; font-size: .95rem; }
.carousel-controls { display: flex; gap: 10px; align-items: center; justify-content: center; padding: 0 0 22px; }
.carousel-controls button { min-height: 44px; min-width: 44px;  background: #171322; color: #ece4ff; border-radius: 4px; padding: 10px 12px; }
.carousel-position { font-size: .875rem; color: #c4bcd4; min-width: 42px; }
.carousel-status { min-height: 1.5em; color: #c4bcd4; font-size: .75rem; }
@media (max-width:800px) {
  .proof-logo-group { gap: 32px; padding-right: 32px; }
  .proof-logo-group .press-logo-item { width: 110px; flex-basis: 110px; }
  .proof-logo-group .press-logo-item img { width: 110px; height: 36px; }
  .meme-carousel { width: min(100%,290px); }
}
'''

SIGNAL_STYLES += r'''
/* App showcase: an editorial left column and one compact device on the right. */
.meme-arcade-callout { padding: 80px 48px; background: radial-gradient(ellipse at 78% 55%,#261a3b,transparent 55%),var(--ink); }
.meme-arcade-inner { max-width: 1224px; display: grid; grid-template-columns: 1.2fr 1fr; gap: 80px; align-items: center; text-align: left; }
.meme-arcade-icon { width: 96px; margin: 0 0 22px; filter: drop-shadow(0 0 24px #a975fa35); }
.meme-arcade-badge { display: block; padding: 0;  background: none; border-radius: 0; font-size: .75rem; letter-spacing: .15em; margin-bottom: 20px; }
.meme-arcade-callout h2 { font-size: clamp(2.3rem,4vw,3.5rem); line-height: 1.12; margin: 0 0 24px; }
.meme-arcade-description { font-size: 1rem; margin: 0 0 28px; max-width: 510px; }
.meme-arcade-cta { padding: 14px 22px; border-radius: 4px; font-size: .875rem; box-shadow: none; background: #d3b0ff; font-weight: 600; }
.meme-arcade-cta:hover, .meme-arcade-cta:focus-visible { transform: none; box-shadow: 0 0 24px #c59cfa22; }
.meme-carousel { width: min(100%,320px); margin: 0 auto; display: flex; flex-direction: column; text-align: center; }
.meme-carousel .meme-arcade-gallery { order: 0; }
.meme-carousel .meme-arcade-screen-card img { width: min(100%,280px); box-shadow: 15px 18px 50px #0008;  }
.meme-carousel figcaption { margin-top: 20px; min-height: 1.6em; font-size: .875rem; font-weight: 400; color: #b9accc; }
.carousel-controls { order: 1; padding: 8px 0 0; gap: 0; justify-content: center; }
.carousel-controls button {  padding: 10px; background: transparent; color: #b9accc; }
.carousel-controls button:hover { color: #e5d2ff; background: #cda5ff0a; }
.carousel-controls .carousel-pause { order: 4; font-size: .75rem; margin-left: 8px; min-width: 52px; }
.carousel-dots { display: flex; align-items: center; }
.carousel-dot { display: grid; place-items: center; }
.carousel-dot span { display: block; width: 5px; height: 5px; border-radius: 50%; background: #655d73; }
.carousel-dot[aria-current="true"] span { width: 16px; border-radius: 5px; background: #cfabff; }
.carousel-position { order: 2; font-size: .75rem; color: #8e849f; margin-top: 4px; }
.carousel-status { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); }
.proof-logo-group { gap: 52px; padding-right: 52px; }
.proof-logo-group .press-logo-item { width: 220px; flex-basis: 220px; }
.proof-logo-group .press-logo-item img { width: 220px; height: auto; opacity: .85; filter: brightness(1.3); }
.professional-profile-controls button { width: 44px; height: 44px; }
.professional-profile-toolbar { flex-wrap: wrap; }
@media (max-width:800px) {
  .meme-arcade-callout { padding: 56px 24px; }
  .meme-arcade-inner { grid-template-columns: 1fr; gap: 40px; }
  .meme-arcade-icon { width: 80px; }
  .meme-arcade-callout h2 { font-size: 2.4rem; }
  .meme-carousel { width: min(100%,290px); }
  .meme-carousel .meme-arcade-screen-card img { width: min(100% - 16px,260px); }
  .carousel-controls button { padding: 8px; }
  .carousel-controls .carousel-pause { margin-left: 0; }
  .proof-logo-group .press-logo-item { width: 160px; flex-basis: 160px; }
  .proof-logo-group .press-logo-item img { width: 160px; height: auto; }
}
'''

SIGNAL_STYLES += r'''
/* Meme Arcade keeps its own product typography and iOS-style icon treatment. */
#memearcade, #memearcade h2, #memearcade button { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }
#memearcade h2 { font-weight: 600; letter-spacing: -.045em; line-height: 1.12; }
.meme-app-icon { width: 104px; aspect-ratio: 1; padding: 12px; border-radius: 24px; background: linear-gradient(145deg,#36115b,#18092e 65%,#102537);  box-shadow: 0 12px 30px #0006; margin-bottom: 28px; overflow: hidden; }
.meme-app-icon .meme-arcade-icon { width: 100%; height: auto; margin: 0; filter: none; }
@media (max-width:800px) { .meme-app-icon { width: 88px; border-radius: 21px; padding: 10px; margin-bottom: 24px; } }
'''

SIGNAL_STYLES += r'''
/* Provider dimensions reserve square, 4:3, and widescreen players without crops. */
.video-frame { position: relative; width: 100%; aspect-ratio: var(--video-ratio); background: #070b10; overflow: hidden; border-radius: 3px; }
main .video-frame iframe { position: absolute; inset: 0; display: block; width: 100%; height: 100%; aspect-ratio: auto;  border-radius: 0; box-shadow: none; }
.impact-card .card-video, .project-card .card-video, .innovation-card .card-video { align-self: center; height: auto; }
.waken-video-container { padding-top: 0; }
.filmography .film-grid { grid-template-columns: repeat(2,minmax(0,1fr)); }
@media (max-width:800px) { .filmography .film-grid { grid-template-columns: 1fr; padding: 0; } }
'''

SIGNAL_STYLES += r'''
/* Intrinsic sizing stays robust when visitors enlarge text. */
html { scroll-padding-top: calc(var(--header-clearance, var(--header-height)) + 24px); }
main *, .signal-footer * { min-width: 0; }
.site-identity { min-width: 0; }
.site-nav { min-width: 0; }
.site-nav .site-identity { flex-shrink: 1; }
.identity-mark { flex-shrink: 0; }
.menu-toggle { flex-shrink: 0; }
.signal-copy, .citations-inner > *, .featured-book-inner > *, .meme-arcade-inner > * { min-width: 0; }
.signal-actions > a, .meme-arcade-cta, .citations-cta, .featured-book-cta, .professional-profile-download { max-width: 100%; white-space: normal; overflow-wrap: anywhere; }
.carousel-controls { flex-wrap: wrap; }
@media (max-width:800px) {
  .signal-hero-inner, .meme-arcade-inner, .citations-inner, .featured-book-inner, .professional-profile-inner { grid-template-columns: minmax(0,1fr); }
  .site-nav .site-identity > span:last-child { overflow-wrap: anywhere; }
}
'''

SIGNAL_STYLES += r'''
/* Each chapter and card has scroll-linked depth, independently of its content. */
.has-scroll-depth { position: relative; isolation: isolate; }
.scroll-depth-layer { position: absolute; inset: 24px 2%; z-index: -1; pointer-events: none; border-radius: 24px; background: radial-gradient(ellipse at 92% var(--scroll-depth-light,38%),rgba(117,225,244,.09),transparent 65%),radial-gradient(ellipse at 12% 75%,rgba(158,137,255,.035),transparent 65%); transform: translate3d(0,var(--scroll-depth-y,0px),0); }
/* Edge-positioned light must fade out before its decorative box ends. */
.scroll-depth-layer { -webkit-mask-image: radial-gradient(ellipse closest-side, #000 35%, transparent 100%); mask-image: radial-gradient(ellipse closest-side, #000 35%, transparent 100%); }
html[data-motion-quality="calm"] .scroll-depth-layer { background: none; }
.section-header { translate: 0 calc(var(--scroll-depth-y,0px) * .35); }
.depth-rig, .work-orbit { translate: 0 var(--scroll-depth-y,0px); }
#memearcade .scroll-depth-layer { background: radial-gradient(ellipse at 85% var(--scroll-depth-light,38%),rgba(197,145,255,.12),transparent 55%); }
html[data-reduced-motion="true"] .scroll-depth-layer { transform: none; }
html[data-reduced-motion="true"] :is(.section-header,.depth-rig,.work-orbit) { translate: none; }
@media (max-width:800px), (hover:none), (pointer:coarse), (prefers-reduced-motion:reduce) {
  .scroll-depth-layer { transform: none; opacity: .5; }
  .section-header, .depth-rig, .work-orbit { translate: none; }
}
'''

SIGNAL_STYLES += r'''
/* Separation comes from space and tonal surfaces, without outlined boxes. */
*::before, *::after { border: 0; }
.site-nav .header-book, .btn-outline { background: #14212b; }
.site-nav .header-book:hover, .btn-outline:hover { background: #1d303d; }
.section-header::before { display: none; }
.portrait-stage figcaption { padding-left: 0; }
.plane-front { background: linear-gradient(145deg,#75e1f407,transparent 65%); }
.work-orbit span { background: linear-gradient(130deg,#75e1f41c,#9e89ff0a); }
'''
