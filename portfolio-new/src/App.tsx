import { ThemeProvider } from '@mui/material/styles';
import { CssBaseline, Box, Container, Typography, Button, Grid } from '@mui/material';
import { FadingGallery } from './components/FadingGallery';
import Navigation from './components/Navigation';
import { GlassPanel } from './components/GlassPanel';
import { theme } from './theme/theme';
import { BACKGROUND_IMAGES } from './config/images';

const FullWidthVideo = ({ src, title }: { src: string; title?: string }) => (
  <Box sx={{ mb: 6 }}>
    {title && (
      <Typography variant="h6" sx={{ color: '#0071E3', mb: 2, textAlign: 'center', fontWeight: 500 }}>
        {title}
      </Typography>
    )}
    <Box sx={{ 
      position: 'relative', 
      paddingTop: '56.25%', 
      background: '#111', 
      borderRadius: '12px', 
      overflow: 'hidden', 
      maxWidth: '1000px', 
      margin: '0 auto' 
    }}>
      <Box 
        component="iframe" 
        src={src} 
        sx={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 'none' }} 
        allow="autoplay; fullscreen; picture-in-picture" 
        allowFullScreen 
      />
    </Box>
  </Box>
);

const Section = ({ children, dark = false, id }: { children: React.ReactNode; dark?: boolean; id?: string }) => (
  <Box id={id} sx={{ py: { xs: 10, md: 15 }, background: dark ? 'rgba(0,0,0,0.4)' : 'transparent' }}>
    <Container maxWidth="lg">{children}</Container>
  </Box>
);

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <FadingGallery images={BACKGROUND_IMAGES} />
      <Navigation />
      
      {/* Hero */}
      <Box id="home" sx={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative' }}>
        <Container maxWidth="lg" sx={{ textAlign: 'center', py: 10 }}>
          <Typography variant="h1" sx={{ mb: 3, color: '#fff', textShadow: '0 4px 20px rgba(0,0,0,0.5)' }}>
            Hassan Uriostegui
          </Typography>
          <Typography variant="h3" sx={{ mb: 4, color: '#0071E3' }}>
            EB1A Extraordinary Ability • Principal Engineer
          </Typography>
          <Typography variant="h4" sx={{ mb: 6, color: 'rgba(255,255,255,0.85)', fontWeight: 400 }}>
            Silicon Valley Innovator • AI Pioneer • Author
          </Typography>
          
          {/* Stats */}
          <Grid container spacing={3} sx={{ mb: 8, maxWidth: '900px', mx: 'auto' }}>
            {[
              { value: '40M+', label: 'Users Impacted' },
              { value: '$6M+', label: 'Funding Raised' },
              { value: '10K+', label: 'Products Launched' },
              { value: '4', label: 'Books Published' },
            ].map((stat, i) => (
              <Grid item xs={6} md={3} key={i}>
                <Typography variant="h2" sx={{ color: '#fff', mb: 1 }}>{stat.value}</Typography>
                <Typography variant="body2" sx={{ color: 'rgba(255,255,255,0.6)', textTransform: 'uppercase', fontSize: '0.85rem' }}>
                  {stat.label}
                </Typography>
              </Grid>
            ))}
          </Grid>

          <Typography variant="body1" sx={{ maxWidth: 700, mx: 'auto', color: 'rgba(255,255,255,0.7)', fontStyle: 'italic', fontSize: '1.2rem' }}>
            "Intelligence might be appreciated as the most primitive form of life. As such, the Universe won't be just a pathway full of intelligent life, but an absolute reflection of human awareness."
          </Typography>
        </Container>
      </Box>

      {/* Philosophy / Journey */}
      <Section dark id="journey">
        <Typography variant="h2" sx={{ mb: 4, color: '#fff', textAlign: 'center' }}>The Journey</Typography>
        <GlassPanel sx={{ maxWidth: '900px', mx: 'auto' }}>
          <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', mb: 3, fontSize: '1.2rem', lineHeight: 1.8 }}>
            Self-taught from age 10, learning object-oriented programming and binary code as a "native language." 
            Reading Asimov, Einstein, Nietzsche, and Freud at 11 years old.
          </Typography>
          <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', mb: 3, fontSize: '1.2rem', lineHeight: 1.8 }}>
            In 2012, Hassan won a legal case against Mexico's Education Ministry (SEP), setting a national precedent 
            for recognizing precocious talent and allowing young people to obtain degrees through accreditation exams 
            without age restrictions.
          </Typography>
          <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', fontSize: '1.2rem', lineHeight: 1.8 }}>
            Left Mexico for Silicon Valley due to insecurity and lack of support for technology innovation. 
            Mission: "Elevating Humanity through ergonomic and ethical AI."
          </Typography>
        </GlassPanel>
      </Section>

      {/* EB1A */}
      <Section id="eb1a">
        <Typography variant="h2" sx={{ mb: 4, color: '#fff', textAlign: 'center' }}>EB1A Extraordinary Ability</Typography>
        <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', textAlign: 'center', maxWidth: 900, mx: 'auto', mb: 4, fontSize: '1.3rem' }}>
          U.S. Permanent Residency granted in 2020 via the prestigious EB-1A visa, reserved for individuals who demonstrate extraordinary ability 
          in sciences, arts, education, business, or athletics through sustained national or international acclaim.
        </Typography>
        <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', textAlign: 'center', maxWidth: 900, mx: 'auto' }}>
          Hassan qualified through extraordinary achievements: 40M+ users impacted, $6M+ funding raised, patents, 
          Apple WWDC recognition, pioneering Mind Simulation Therapy framework, and founding multiple successful technology ventures.
        </Typography>
      </Section>

      {/* TwinChat 2023 */}
      <Section dark id="twinchat">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>TwinChat</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          Mind Simulation Therapy | 2023 | 20K Conversations | 200K Messages
        </Typography>
        <FullWidthVideo src="https://player.vimeo.com/video/833069637" title="Main Demo" />
        <FullWidthVideo src="https://player.vimeo.com/video/839937602" title="Tutorial" />
        <FullWidthVideo src="https://player.vimeo.com/video/831097799" title="Overview" />
        <Typography variant="h4" sx={{ mt: 10, mb: 4, color: '#fff', textAlign: 'center' }}>Press Interviews</Typography>
        <FullWidthVideo src="https://player.vimeo.com/video/843499496" title="David Paramo & Paul Lara - Cyberpunks Book" />
        <FullWidthVideo src="https://player.vimeo.com/video/843495231" title="Fernanda & Paul Lara - Familiar AI" />
      </Section>

      {/* BTwin Friends 2024 */}
      <Section id="btwin">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>BTwin Friends</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          Entertainment + Wellness Platform | 2024
        </Typography>
        <FullWidthVideo src="https://player.vimeo.com/video/1101438413" title="Main Video" />
        <FullWidthVideo src="https://player.vimeo.com/video/1005370967" title="It's Not Therapy" />
        <FullWidthVideo src="https://player.vimeo.com/video/1003088113" title="Q&A" />
        <Box sx={{ textAlign: 'center', mt: 6 }}>
          <Button variant="contained" size="large" href="https://btwinai.com/" target="_blank">
            Visit BTwin
          </Button>
        </Box>
      </Section>

      {/* Bruja Roja 2024 */}
      <Section dark id="brujaroja">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>Bruja Roja</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          WhatsApp Storytelling AI | 2024
        </Typography>
        <FullWidthVideo src="https://player.vimeo.com/video/1022298842" />
        <FullWidthVideo src="https://player.vimeo.com/video/1023079085" />
        <Box sx={{ textAlign: 'center', mt: 6 }}>
          <Button variant="contained" size="large" href="https://www.brujaroja.mx/" target="_blank">
            Visit Bruja Roja
          </Button>
        </Box>
      </Section>

      {/* SendKarma 2025 */}
      <Section id="sendkarma">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>SendKarma</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          Sadhguru-Inspired Spiritual Wellness AI | 2025
        </Typography>
        <FullWidthVideo src="https://player.vimeo.com/video/1138631992" />
        <Box sx={{ textAlign: 'center', mt: 6 }}>
          <Button variant="contained" size="large" href="https://www.sendkarma.app/" target="_blank">
            Visit SendKarma
          </Button>
        </Box>
      </Section>

      {/* YouChews 2025 */}
      <Section dark id="youchews">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>YouChews</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          2025 Innovation
        </Typography>
        <FullWidthVideo src="https://player.vimeo.com/video/1136377813" />
        <FullWidthVideo src="https://player.vimeo.com/video/1137579881" />
        <FullWidthVideo src="https://player.vimeo.com/video/1137973511" />
      </Section>

      {/* AI Product Shots 2025 */}
      <Section id="aiproductshots">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>AI Product Shots</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          State-of-the-Art November 2025 Generative Motion Graphics AI
        </Typography>
        <FullWidthVideo src="https://player.vimeo.com/video/1144077038" />
        <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', textAlign: 'center', mt: 6, maxWidth: 800, mx: 'auto' }}>
          Revolutionary AI-powered motion graphics system for automated product visualization and video generation. 
          Pushing the boundaries of what's possible with generative AI in late 2025.
        </Typography>
      </Section>

      {/* Viddy */}
      <Section id="viddy">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>Viddy</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          40M Users | $370-480M Valuation | 2012-2013
        </Typography>
        <FullWidthVideo src="https://www.youtube.com/embed/avccq32KfOE" />
        <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', textAlign: 'center', mt: 6, maxWidth: 800, mx: 'auto' }}>
          Director of Video Engineering. Built state-of-the-art mobile VFX engine when Instagram was photo-only. 
          Backed by Will Smith and Shakira. Acquired by Fullscreen in 2014.
        </Typography>
      </Section>

      {/* FlyrTV */}
      <Section dark id="flyrtv">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>FlyrTV</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          CTO & Co-founder | $6M Raised | Acquired by POND5 | 2014-2018
        </Typography>
        <FullWidthVideo src="https://www.youtube.com/embed/7GQm8h70PRg" />
        <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', textAlign: 'center', mt: 6, maxWidth: 800, mx: 'auto' }}>
          10,000+ HD video templates. FIRST third-party with Snapchat API access. Acquired by POND5 (Accel/Google backed).
        </Typography>
      </Section>

      {/* Ultrakam */}
      <Section id="ultrakam">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>Ultrakam</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          Featured at Apple WWDC 2014 | Forbes Coverage | 2013-2014
        </Typography>
        <FullWidthVideo src="https://www.youtube.com/embed/fhgSC6TvnoM" />
        <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', textAlign: 'center', mt: 6, maxWidth: 800, mx: 'auto' }}>
          FIRST mobile app enabling 2K film-resolution recording. Surpassed Apple's own implementation. Featured at WWDC as example of outstanding design.
        </Typography>
      </Section>

      {/* Books */}
      <Section dark id="books">
        <Typography variant="h2" sx={{ mb: 8, color: '#fff', textAlign: 'center' }}>Published Works</Typography>
        {[
          { 
            title: "I, AI: Nemo's Mirror", 
            subtitle: 'Exploring the Singular Nature of Self-Awareness in ChatGPT', 
            year: '2023', 
            url: 'https://www.amazon.com/-/he/Hassan-Uriostegui/dp/1304332993',
            press: 'Featured in Korea Biz Wire'
          },
          { 
            title: 'I, AI: Exploring ChatGPT', 
            subtitle: 'The Singular Nature of Self-Awareness', 
            year: '2023', 
            url: 'https://www.amazon.com.mx/AI-Exploring-Singular-Self-Awareness-ChatGPT/dp/1365528669' 
          },
          { 
            title: 'Yo, IA: Cyberpunks', 
            subtitle: 'La Inteligencia Artificial y el Espejo de Nemo (Spanish Edition)', 
            year: '2023', 
            url: 'https://www.amazon.com/Yo-IA-Cyberpunks-Inteligencia-Artificial/dp/1312446501',
            media: 'Featured on Imagen Radio Mexico'
          },
          { 
            title: 'The Fly of the Humanized Robot', 
            subtitle: 'An Algorithm to Heal the Soul', 
            year: '2020', 
            url: 'http://gethumanized.com' 
          }
        ].map((book, i) => (
          <GlassPanel key={i} sx={{ mb: 4, maxWidth: '800px', mx: 'auto' }}>
            <Box sx={{ textAlign: 'center' }}>
              <Typography variant="h6" sx={{ color: '#0071E3', mb: 1 }}>{book.year}</Typography>
              <Typography variant="h3" sx={{ color: '#fff', mb: 1 }}>{book.title}</Typography>
              <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.7)', mb: 2 }}>{book.subtitle}</Typography>
              {(book.press || book.media) && (
                <Typography variant="body2" sx={{ color: 'rgba(255,255,255,0.5)', mb: 3, fontStyle: 'italic' }}>
                  {book.press || book.media}
                </Typography>
              )}
              <Button variant="contained" href={book.url} target="_blank">View Book</Button>
            </Box>
          </GlassPanel>
        ))}
      </Section>

      {/* Press */}
      <Section id="press">
        <Typography variant="h2" sx={{ mb: 8, color: '#fff', textAlign: 'center' }}>Press & Media Coverage</Typography>
        {[
          { 
            pub: 'TechCrunch', 
            date: 'March 13, 2017',
            headline: 'Flyr launches app for rapid creation of Snapchat Discover-style stories', 
            excerpt: 'FlyrTV launches today making it easier for anyone to create Snapchat Discover-style video stories. First third-party with Snapchat content API access.',
            url: 'https://techcrunch.com/2017/03/13/flyr-launch/' 
          },
          { 
            pub: 'Authority Magazine', 
            date: 'August 2024',
            headline: 'Hassan Uriostegui On the Future of Artificial Intelligence', 
            excerpt: 'In-depth interview discussing AI consciousness, Mind Simulation Therapy, and the future of human-AI interaction.',
            url: 'https://medium.com/authority-magazine/hassan-uriostegui-on-the-future-of-artificial-intelligence-a013ebee514e' 
          },
          { 
            pub: 'Noroeste (Mexico)', 
            date: 'November 15, 2015',
            headline: 'Revolutionizes the World of Apps', 
            excerpt: 'At 28, Hassan created an iPhone application that surpasses Photoshop according to users worldwide. Won legal case against Education Ministry, setting national precedent.',
            url: 'https://www.noroeste.com.mx/buen-vivir/revoluciona-el-mundo-de-las-apps-EPNO861674' 
          },
          { 
            pub: 'Korea Biz Wire', 
            date: '2023',
            headline: 'Is ChatGPT Sentient? The Question is Answered in I, AI', 
            excerpt: 'Waken AI founder Hassan Uriostegui explores consciousness and AI sentience in groundbreaking new book.',
            url: 'http://koreabizwire.com/is-chatgpt-sentient-the-question-is-answered-in-i-ai-by-waken-ai-founder-hassan-uriostegui' 
          },
          { 
            pub: 'Forbes', 
            date: '2014',
            headline: 'Ultrakam 4K video app arrives for iPhone 6', 
            excerpt: 'Revolutionary app brings professional-grade 2K recording to mobile devices, surpassing Apple\'s own implementation.',
            url: '#' 
          },
          { 
            pub: 'Newswire', 
            date: 'September 2020',
            headline: 'The Mexican Developer Behind Ashton Kutcher\'s Latest Celebrities App', 
            excerpt: 'Hassan Uriostegui, pioneer developer who overpassed Instagram, Apple, and Adobe with visionary research, builds Community app for Ashton Kutcher and Madonna.',
            url: 'https://www.newswire.com/news/the-mexican-developer-behind-ashton-kutchers-latest-celebrities-app-21215115' 
          }
        ].map((article, i) => (
          <GlassPanel 
            key={i} 
            sx={{ 
              mb: 4,
              cursor: 'pointer',
              transition: 'transform 0.3s, box-shadow 0.3s',
              '&:hover': { 
                transform: 'translateY(-4px)',
                boxShadow: '0 12px 40px 0 rgba(0, 113, 227, 0.3)'
              } 
            }}
          >
            <Box 
              component="a" 
              href={article.url} 
              target="_blank"
              sx={{ textDecoration: 'none', display: 'block' }}
            >
              <Typography 
                variant="overline" 
                sx={{ 
                  color: 'rgba(255,255,255,0.5)', 
                  letterSpacing: '0.1em',
                  fontSize: '0.75rem',
                  display: 'block',
                  mb: 1
                }}
              >
                {article.pub} • {article.date}
              </Typography>
              <Typography variant="h4" sx={{ color: '#fff', mb: 3, fontWeight: 700 }}>
                {article.headline}
              </Typography>
              <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.7)', fontSize: '1.1rem', lineHeight: 1.8 }}>
                {article.excerpt}
              </Typography>
              <Button 
                variant="text" 
                sx={{ mt: 3, color: '#0071E3', '&:hover': { background: 'rgba(0,113,227,0.1)' } }}
              >
                Read Full Article →
              </Button>
            </Box>
          </GlassPanel>
        ))}
      </Section>

      {/* Recognition */}
      <Section dark id="recognition">
        <Typography variant="h2" sx={{ mb: 8, color: '#fff', textAlign: 'center' }}>Recognition & Awards</Typography>
        <Grid container spacing={4} sx={{ maxWidth: '1000px', mx: 'auto' }}>
          {[
            { title: 'EB1A Extraordinary Ability', year: '2020', desc: 'U.S. Immigration recognition for extraordinary ability in computer sciences' },
            { title: 'Apple WWDC Featured', year: '2014', desc: 'Ultrakam featured at WWDC as example of outstanding design' },
            { title: 'Patent Holder', year: '2018', desc: 'Intelligent Graphical Feature Generation for User Content' },
            { title: 'First Snapchat API Access', year: '2017', desc: 'FlyrTV - First third-party company granted Snapchat API integration' },
            { title: 'Ariel Awards Winner', year: '2008', desc: 'Km 31 - First Mexican film to win for VFX/Special Effects' },
            { title: 'Visual Effects Society', year: '2010+', desc: 'Active member of Hollywood VES' }
          ].map((item, i) => (
            <Grid item xs={12} md={6} key={i}>
              <Box sx={{ textAlign: 'center', p: 3 }}>
                <Typography variant="h6" sx={{ color: '#0071E3', mb: 1 }}>{item.year}</Typography>
                <Typography variant="h4" sx={{ color: '#fff', mb: 1, fontSize: '1.5rem' }}>{item.title}</Typography>
                <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.7)' }}>{item.desc}</Typography>
              </Box>
            </Grid>
          ))}
        </Grid>
      </Section>

      {/* Filmography */}
      <Section id="filmography">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>Filmography & Visual Effects</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          10+ Feature Films | VFX Supervisor | 2006-2010
        </Typography>
        <FullWidthVideo src="https://www.youtube.com/embed/cS9tKYNIOxg" title="VFX Reel" />
        <FullWidthVideo src="https://www.youtube.com/embed/H1D5HITPAhc" title="Creative Engineering" />
        <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', textAlign: 'center', mt: 6, maxWidth: 800, mx: 'auto', mb: 4 }}>
          Worked on 10+ feature films as Digital Compositor, Technical Director, and VFX Supervisor. 
          Won Ariel Awards (Mexican Academy Award equivalent) for Km 31 - the first Mexican film to win for visual effects.
        </Typography>
        <Box sx={{ textAlign: 'center', mt: 6 }}>
          <Button variant="contained" href="https://www.imdb.com/name/nm2843359/" target="_blank" size="large">
            View IMDB Profile
          </Button>
        </Box>
      </Section>

      {/* Footer / Contact */}
      <Box id="contact" sx={{ py: 12, background: 'rgba(0,0,0,0.95)' }}>
        <Container maxWidth="lg">
          <Typography variant="h3" sx={{ color: '#fff', textAlign: 'center', mb: 4 }}>
            Get in Touch
          </Typography>
          <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.8)', textAlign: 'center', mb: 4, fontSize: '1.3rem' }}>
            hassan.uriostegui@gmail.com
          </Typography>
          <Box sx={{ textAlign: 'center', mb: 6 }}>
            {[
              { label: 'LinkedIn', url: 'https://www.linkedin.com/in/bensabbah' },
              { label: 'GitHub', url: 'https://github.com/hassanvfx' },
              { label: 'Medium', url: 'https://uriostegui.medium.com' },
              { label: 'Waken.ai', url: 'https://www.wakenai.com' },
              { label: 'Chat with My AI', url: 'https://chatgpt.com/g/g-encZOxBLw-uriosteguigpt' }
            ].map((link, i) => (
              <Button key={i} variant="outlined" href={link.url} target="_blank" sx={{ mx: 1, my: 1 }}>
                {link.label}
              </Button>
            ))}
          </Box>
          <Typography variant="body2" sx={{ color: 'rgba(255,255,255,0.4)', textAlign: 'center' }}>
            © 2025 Hassan Uriostegui. EB1A Extraordinary Ability. 40M+ Users | $6M+ Raised | 4 Books | 1 Patent
          </Typography>
        </Container>
      </Box>

    </ThemeProvider>
  );
}

export default App;
