"""HTML Template Parts - Enhanced with Scroll Nav and View More Pattern"""

HTML_HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} - {status}</title>
  <meta name="description" content="{name} - {status}. Silicon Valley Innovator, AI Pioneer, Author. 40M+ users impacted, $6M+ raised.">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&family=Playfair+Display:wght@700;900&display=swap" rel="stylesheet">
  
  <style>
{css}
  </style>
</head>
<body>
'''

HTML_SCROLL_NAV = '''
<!-- Scroll-Synced Navigation -->
<nav class="scroll-nav">
  <div class="scroll-nav-inner">
    <a href="#home" class="scroll-nav-item active" data-section="home">Home</a>
    <a href="#work" class="scroll-nav-item" data-section="work">Work</a>
    <a href="#impact" class="scroll-nav-item" data-section="impact">Impact</a>
    <a href="#books" class="scroll-nav-item" data-section="books">Books</a>
    <a href="#press" class="scroll-nav-item" data-section="press">Press</a>
    <a href="#contact" class="scroll-nav-item" data-section="contact">Contact</a>
  </div>
</nav>
'''

HTML_HERO = '''
<!-- Hero Section -->
<section id="home" class="hero section-black" data-nav="home">
  <div class="container">
    <div class="hero-content">
      <p class="eyebrow" data-aos="fade-up">{status}</p>
      <h1 data-aos="fade-up" data-aos-delay="100">{name}</h1>
      <p class="tagline" data-aos="fade-up" data-aos-delay="200">Silicon Valley Innovator | AI Pioneer | Author</p>
      
      <div class="stats-row" data-aos="fade-up" data-aos-delay="300">
{stats_html}
      </div>
    </div>
  </div>
</section>

<!-- Opening Quote -->
<section class="section-dark section-compact">
  <div class="container">
    <blockquote class="quote" data-aos="fade-up">
      "{quote}"
      <cite>{name}</cite>
    </blockquote>
  </div>
</section>
'''

HTML_PROJECT_CARD = '''
<!-- {name} -->
<section id="{id}" class="section-black project-card" data-nav="work">
  <div class="container">
    <div class="project-card-inner{reverse_class}">
      <div class="project-video" data-aos="fade-up">
        <div class="video-wrapper">
          <iframe src="{hero_video}" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen loading="lazy"></iframe>
        </div>
      </div>
      
      <div class="project-content" data-aos="fade-up" data-aos-delay="100">
        <p class="eyebrow">{year}</p>
        <h2>{name}</h2>
        {highlight_html}
        <p class="description">{description}</p>
        {quote_html}
        <div class="project-actions">
          {website_btn}
          {expand_btn}
        </div>
      </div>
    </div>
    
{more_videos_html}
  </div>
</section>
'''

HTML_MORE_VIDEOS = '''
    <div class="more-videos" id="{id}-videos">
      <div class="more-videos-inner">
{video_items}
      </div>
    </div>
'''

HTML_MORE_VIDEO_ITEM = '''
        <div class="more-video-item">
          <div class="video-wrapper">
            <iframe src="{url}" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen loading="lazy"></iframe>
          </div>
          <p class="video-title">{title}</p>
        </div>
'''

HTML_SECTION_HEADER = '''
<!-- {title} Section Header -->
<section id="{id}" class="section-white" data-nav="{nav_id}">
  <div class="container">
    <div class="section-header" data-aos="fade-up">
      <p class="eyebrow">{eyebrow}</p>
      <h2>{title}</h2>
      <p class="lead">{description}</p>
    </div>
  </div>
</section>
'''

HTML_EB1A_SECTION = '''
<!-- EB1A Section -->
<section id="eb1a" class="section-white" data-nav="impact">
  <div class="container">
    <div class="section-header" data-aos="fade-up">
      <p class="eyebrow">Official Recognition</p>
      <h2>EB1A Extraordinary Ability</h2>
      <p class="lead">
        U.S. Permanent Residency granted in 2020 via the prestigious <strong>EB-1A visa</strong>, 
        reserved for individuals who demonstrate extraordinary ability through sustained national 
        or international acclaim.
      </p>
    </div>
    
    <div style="max-width: 800px; margin: 0 auto; text-align: center;" data-aos="fade-up">
      <p class="description" style="color: var(--text-muted-white); font-size: 18px; line-height: 1.8;">
        Only 0.5% of U.S. green card applicants qualify for this category. Hassan qualified through 
        documented evidence of: original contributions of major significance (Mind Simulation Therapy), 
        authorship of scholarly articles (4 published books), critical role in distinguished organizations 
        (CTO/Co-founder positions), commercial success (40M+ users, $6M+ raised), and widespread 
        media coverage (TechCrunch, Forbes, Authority Magazine).
      </p>
      <p class="footnote" style="color: var(--text-muted-white);">
        Source: USCIS EB-1A Criteria for Extraordinary Ability Classification
      </p>
    </div>
  </div>
</section>
'''

HTML_BOOKS_SECTION = '''
<!-- Books Section -->
<section id="books" class="section-dark" data-nav="books">
  <div class="container">
    <div class="section-header" data-aos="fade-up">
      <p class="eyebrow">Published Works</p>
      <h2>Books on AI Consciousness</h2>
      <p class="lead">Exploring the boundaries of artificial intelligence, consciousness, and what it means to be human in an age of thinking machines.</p>
    </div>
    
    <div class="books-grid">
{books_html}
    </div>
  </div>
</section>
'''

HTML_BOOK_ITEM = '''
      <div class="book-card" data-aos="fade-up" data-aos-delay="{delay}">
        <p class="year">{year} | {language}</p>
        <h4>{title}</h4>
        <p class="subtitle">{subtitle}</p>
        {press_html}
        <a href="{url}" target="_blank" class="btn btn-primary">View on Amazon</a>
      </div>
'''

HTML_PRESS_SECTION = '''
<!-- Press Section -->
<section id="press" class="section-black" data-nav="press">
  <div class="container">
    <div class="section-header" data-aos="fade-up">
      <p class="eyebrow">Media Coverage</p>
      <h2>Press & Recognition</h2>
      <p class="lead">Featured in leading technology publications worldwide.</p>
    </div>
    
    <div class="press-grid">
{press_html}
    </div>
  </div>
</section>
'''

HTML_PRESS_ITEM = '''
      <a href="{url}" target="_blank" class="press-card" data-aos="fade-up" data-aos-delay="{delay}">
        <p class="publication">{publication}</p>
        <h4>{headline}</h4>
        <p class="excerpt">{excerpt}</p>
      </a>
'''

HTML_RECOGNITION_SECTION = '''
<!-- Recognition Section -->
<section class="section-dark">
  <div class="container">
    <div class="section-header" data-aos="fade-up">
      <p class="eyebrow">Achievements</p>
      <h2>Recognition & Awards</h2>
    </div>
    
    <div class="recognition-grid">
{recognition_html}
    </div>
  </div>
</section>
'''

HTML_RECOGNITION_ITEM = '''
      <div class="recognition-item" data-aos="fade-up" data-aos-delay="{delay}">
        <p class="year">{year}</p>
        <h4>{title}</h4>
        <p>{description}</p>
      </div>
'''

HTML_FILMOGRAPHY_SECTION = '''
<!-- Filmography Section -->
<section id="filmography" class="section-black">
  <div class="container">
    <div class="project-card-inner">
      <div class="project-video" data-aos="fade-up">
        <div class="video-wrapper">
          <iframe src="{hero_video}" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen loading="lazy"></iframe>
        </div>
      </div>
      
      <div class="project-content" data-aos="fade-up" data-aos-delay="100">
        <p class="eyebrow">{years}</p>
        <h2>Visual Effects & Filmography</h2>
        <span class="highlight">{total_films} Feature Films</span>
        <p class="description">{description}</p>
        <div class="project-actions">
          <a href="{imdb}" target="_blank" class="btn btn-primary">View IMDB Profile</a>
        </div>
      </div>
    </div>
  </div>
</section>
'''

HTML_FOOTER = '''
<!-- Footer -->
<footer id="contact" class="footer" data-nav="contact">
  <div class="container">
    <p class="eyebrow" data-aos="fade-up">Get in Touch</p>
    <h3 data-aos="fade-up">Let's Build Something Extraordinary</h3>
    <p class="email" data-aos="fade-up">{email}</p>
    
    <div class="social-links" data-aos="fade-up">
{social_links_html}
    </div>
    
    <p class="copyright">
      {name} | {status}<br>
      40M+ Users Impacted | $6M+ Raised | 4 Books Published | 1 Patent
    </p>
  </div>
</footer>
'''

HTML_FOOTER_SCRIPTS = '''
<!-- Intersection Observer for Scroll Navigation -->
<script>
  // Scroll-synced navigation
  const navItems = document.querySelectorAll('.scroll-nav-item');
  const sections = document.querySelectorAll('[data-nav]');
  
  const observerOptions = {
    root: null,
    rootMargin: '-50% 0px -50% 0px',
    threshold: 0
  };
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const navId = entry.target.getAttribute('data-nav');
        navItems.forEach(item => {
          item.classList.remove('active');
          if (item.getAttribute('data-section') === navId) {
            item.classList.add('active');
          }
        });
      }
    });
  }, observerOptions);
  
  sections.forEach(section => observer.observe(section));
  
  // Smooth scroll for navigation
  navItems.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = item.getAttribute('href');
      const target = document.querySelector(targetId);
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
  
  // Expand/collapse videos
  document.querySelectorAll('.btn-expand').forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-target');
      const target = document.getElementById(targetId);
      if (target) {
        target.classList.toggle('expanded');
        btn.classList.toggle('expanded');
        btn.querySelector('.text').textContent = 
          target.classList.contains('expanded') ? 'Show Less' : 'View More';
      }
    });
  });
  
  // Simple AOS-like animation on scroll
  const animateOnScroll = () => {
    document.querySelectorAll('[data-aos]').forEach(el => {
      const rect = el.getBoundingClientRect();
      const isVisible = rect.top < window.innerHeight - 100;
      if (isVisible) {
        el.classList.add('aos-animate');
      }
    });
  };
  
  window.addEventListener('scroll', animateOnScroll);
  window.addEventListener('load', animateOnScroll);
</script>
</body>
</html>
'''
