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
  border-bottom: 1px solid rgba(255,255,255,0.1);
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
  border-left: none;
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
  border-top: 1px solid rgba(255,255,255,0.1);
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
  border: none;
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
  border-top: 1px solid rgba(255,255,255,0.1);
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
  border: none;
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
  border: 1px solid rgba(0, 212, 255, 0.4);
}

.btn-outline:hover {
  border-color: var(--cyan);
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
  border: 1px solid rgba(255,255,255,0.2);
  font-size: 14px;
  padding: 12px 24px;
}

.btn-expand:hover {
  color: var(--white);
  border-color: rgba(255,255,255,0.4);
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
  border: 1px solid rgba(255,255,255,0.08);
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
  border-top: 1px solid rgba(255,255,255,0.1);
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
