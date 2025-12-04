import { ThemeProvider, createTheme } from '@mui/material/styles';
import { CssBaseline, Box, Container, Typography, Button } from '@mui/material';
import { FadingGallery } from './components/FadingGallery';
import { Navigation } from './components/Navigation';
import { GlassPanel } from './components/GlassPanel';

const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: { main: '#0071E3' },
    background: { default: '#000000', paper: '#000000' },
  },
  typography: {
    fontFamily: '"SF Pro Display", "Inter", -apple-system, sans-serif',
    h1: { fontSize: '5rem', fontWeight: 800, letterSpacing: '-0.03em' },
    h2: { fontSize: '3.5rem', fontWeight: 700, letterSpacing: '-0.02em' },
    h3: { fontSize: '2.5rem', fontWeight: 600 },
    h4: { fontSize: '1.8rem', fontWeight: 500 },
    body1: { fontSize: '1.25rem', lineHeight: 1.7 },
  },
});

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
      <FadingGallery />
      <Navigation />
      
      {/* Hero */}
      <Box id="home" sx={{ minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'relative' }}>
        <Container maxWidth="lg" sx={{ textAlign: 'center', py: 10 }}>
          <Typography variant="h1" sx={{ mb: 3, color: '#fff', textShadow: '0 4px 20px rgba(0,0,0,0.5)' }}>
            Hassan Uriostegui
          </Typography>
          <Typography variant="h3" sx={{ mb: 4, color: '#0071E3' }}>
            EB1A Extraordinary Ability
          </Typography>
          <Typography variant="h4" sx={{ mb: 6, color: 'rgba(255,255,255,0.85)', fontWeight: 400 }}>
            40M+ Users | $6M+ Raised | 4 Books | 1 Patent
          </Typography>
          <Typography variant="body1" sx={{ maxWidth: 700, mx: 'auto', color: 'rgba(255,255,255,0.7)', fontStyle: 'italic' }}>
            "Intelligence might be appreciated as the most primitive form of life. As such, the Universe won't be just a pathway full of intelligent life, but an absolute reflection of human awareness."
          </Typography>
        </Container>
      </Box>

      {/* TwinChat 2023 */}
      <Section dark id="twinchat">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>TwinChat</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          Mind Simulation Therapy | 2023 | 20K Conversations | 200K Messages
        </Typography>
        <FullWidthVideo src="https://player.vimeo.com/video/833069637" title="Main Demo" />
        <FullWidthVideo src="https://player.vimeo.com/video/839937602" title="Tutorial" />
        <FullWidthVideo src="https://player.vimeo.com/video/831097799" title="Overview" />
        <FullWidthVideo src="https://player.vimeo.com/video/831097785" title="App Store" />
        <Typography variant="h4" sx={{ mt: 10, mb: 4, color: '#fff', textAlign: 'center' }}>Press Interviews</Typography>
        <FullWidthVideo src="https://player.vimeo.com/video/843499496" title="David Paramo & Paul Lara" />
        <FullWidthVideo src="https://player.vimeo.com/video/843495231" title="Fernanda & Paul Lara" />
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
        <FullWidthVideo src="https://player.vimeo.com/video/1004812787" title="Famous Characters" />
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
        <FullWidthVideo src="https://player.vimeo.com/video/1023078988" />
        <FullWidthVideo src="https://player.vimeo.com/video/1023079032" />
        <Box sx={{ textAlign: 'center', mt: 6 }}>
          <Button variant="contained" size="large" href="https://www.brujaroja.mx/" target="_blank">
            Visit Website
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
        <FullWidthVideo src="https://player.vimeo.com/video/1115280799" />
        <FullWidthVideo src="https://player.vimeo.com/video/1137973511" />
        <FullWidthVideo src="https://player.vimeo.com/video/1137579986" />
      </Section>

      {/* CoachTotal 2025 */}
      <Section id="coachtotal">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>CoachTotal</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          AI Emotional Coaching via WhatsApp | 2025
        </Typography>
        <Box sx={{ textAlign: 'center' }}>
          <Button variant="contained" size="large" href="https://coachtotal.app/" target="_blank">
            Visit CoachTotal
          </Button>
        </Box>
      </Section>

      {/* JabaliAI 2025 */}
      <Section dark id="jabali">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>JabaliAI</Typography>
        <Typography variant="h4" sx={{ mb: 4, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          Principal Engineer | Text-to-Game AI Systems | 2025
        </Typography>
        <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.8)', textAlign: 'center', maxWidth: 800, mx: 'auto' }}>
          Building revolutionary AI systems for game development. SimZApp.com product designer.
        </Typography>
      </Section>

      {/* HISTORIC COMPANIES */}

      {/* Viddy */}
      <Section id="viddy">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>Viddy</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          40M Users | $370-480M Valuation | 2012-2013
        </Typography>
        <FullWidthVideo src="https://www.youtube.com/embed/avccq32KfOE" />
        <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', textAlign: 'center', mt: 6, maxWidth: 800, mx: 'auto' }}>
          Director of Video Engineering. Built state-of-the-art mobile VFX engine when Instagram was photo-only. 
          Backed by Will Smith and Shakira. Acquired by Fullscreen.
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

      {/* Community */}
      <Section id="community">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>Community</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          Principal iOS Architect | Backed by Madonna & Ashton Kutcher | 2019-2020
        </Typography>
        <FullWidthVideo src="https://www.youtube.com/embed/ZOWuy-HhQxE" />
        <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', textAlign: 'center', mt: 6, maxWidth: 800, mx: 'auto' }}>
          Millions of users. Implemented Princeton CS Ph.D. paper in Swift for high-performance messaging.
        </Typography>
      </Section>

      {/* Ultrakam */}
      <Section dark id="ultrakam">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>Ultrakam</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          Featured at Apple WWDC 2014 | Forbes Coverage | 2013-2014
        </Typography>
        <FullWidthVideo src="https://www.youtube.com/embed/fhgSC6TvnoM" />
        <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', textAlign: 'center', mt: 6, maxWidth: 800, mx: 'auto' }}>
          FIRST mobile app enabling 2K film-resolution recording. Surpassed Apple's own implementation.
        </Typography>
      </Section>

      {/* EB1A Section */}
      <Section id="eb1a">
        <Typography variant="h2" sx={{ mb: 4, color: '#fff', textAlign: 'center' }}>EB1A Extraordinary Ability</Typography>
        <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', textAlign: 'center', maxWidth: 900, mx: 'auto', mb: 4, fontSize: '1.3rem' }}>
          The EB-1A visa is reserved for individuals who demonstrate extraordinary ability in sciences, arts, education, business, or athletics through sustained national or international acclaim.
        </Typography>
        <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.85)', textAlign: 'center', maxWidth: 900, mx: 'auto' }}>
          Hassan qualified through extraordinary achievements: 40M+ users impacted, $6M+ funding raised, patents, Apple WWDC recognition, pioneering Mind Simulation Therapy framework, and founding multiple successful technology ventures.
        </Typography>
        <Box sx={{ textAlign: 'center', mt: 4 }}>
          <Button variant="outlined" href="https://en.wikipedia.org/wiki/EB-1_visa" target="_blank">
            Learn about EB1A
          </Button>
        </Box>
      </Section>

      {/* Books */}
      <Section dark id="books">
        <Typography variant="h2" sx={{ mb: 8, color: '#fff', textAlign: 'center' }}>Published Works</Typography>
        {[
          { title: "I, AI: Nemo's Mirror", subtitle: 'Exploring AI Consciousness', year: '2023', url: 'https://www.amazon.com/-/he/Hassan-Uriostegui/dp/1304332993' },
          { title: 'I, AI: Exploring ChatGPT', subtitle: 'Self-Awareness Study', year: '2023', url: 'https://www.amazon.com.mx/AI-Exploring-Singular-Self-Awareness-ChatGPT/dp/1365528669' },
          { title: 'Yo, IA: Cyberpunks', subtitle: 'Spanish Edition', year: '2023', url: 'https://www.amazon.com/Yo-IA-Cyberpunks-Inteligencia-Artificial/dp/1312446501' },
          { title: 'The Humanized Robot', subtitle: 'Algorithm to Heal the Soul', year: '2020', url: 'http://gethumanized.com' }
        ].map((book, i) => (
          <GlassPanel key={i} sx={{ mb: 4 }}>
            <Box sx={{ textAlign: 'center' }}>
              <Typography variant="h6" sx={{ color: '#0071E3', mb: 1 }}>{book.year}</Typography>
              <Typography variant="h3" sx={{ color: '#fff', mb: 1 }}>{book.title}</Typography>
              <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.7)', mb: 3 }}>{book.subtitle}</Typography>
              <Button variant="contained" href={book.url} target="_blank">View Book</Button>
            </Box>
          </GlassPanel>
        ))}
      </Section>

      {/* Press */}
      <Section id="press">
        <Typography variant="h2" sx={{ mb: 8, color: '#fff', textAlign: 'center' }}>Press & Media</Typography>
        {[
          { 
            pub: 'TechCrunch', 
            date: 'March 13, 2017',
            headline: 'Flyr launches app for rapid creation of Snapchat Discover-style stories', 
            excerpt: 'A new app called Flyr is launching today that aims to make it easier for anyone to create Snapchat Discover-style video stories...',
            url: 'https://techcrunch.com/2017/03/13/flyr-launch/' 
          },
          { 
            pub: 'Authority Magazine', 
            date: '2023',
            headline: 'Hassan Uriostegui On the Future of Artificial Intelligence', 
            excerpt: 'Intelligence might be appreciated as the most primitive form of life. The Universe will be an absolute reflection of human awareness.',
            url: 'https://medium.com/authority-magazine/hassan-uriostegui-on-the-future-of-artificial-intelligence-a013ebee514e' 
          },
          { 
            pub: 'Noroeste', 
            date: 'November 15, 2015',
            headline: 'Revolutionizes the World of Apps', 
            excerpt: 'At 28 years old, Hassan Urióstegui has managed to revolutionize the world of Apps. Created an iPhone application that surpasses Photoshop according to users worldwide.',
            url: 'https://www.noroeste.com.mx/buen-vivir/revoluciona-el-mundo-de-las-apps-EPNO861674' 
          },
          { 
            pub: 'Korea Biz Wire', 
            date: '2023',
            headline: 'Is ChatGPT Sentient? The Question is Answered in I, AI', 
            excerpt: 'Waken AI founder Hassan Uriostegui explores consciousness and AI sentience in groundbreaking new book...',
            url: 'http://koreabizwire.com/is-chatgpt-sentient-the-question-is-answered-in-i-ai-by-waken-ai-founder-hassan-uriostegui' 
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
                boxShadow: '0 12px 40px 0 rgba(0, 113, 227, 0.2)'
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
        <Typography variant="h2" sx={{ mb: 8, color: '#fff', textAlign: 'center' }}>Recognition</Typography>
        {[
          { title: 'EB1A Extraordinary Ability Visa', year: '2020', desc: 'US Immigration recognition for extraordinary ability in technology' },
          { title: 'Apple WWDC Featured', year: '2014', desc: 'Ultrakam featured by Apple at WWDC keynote' },
          { title: 'Patent: Intelligent Graphical Feature Generation', year: '2018', desc: 'Renderfarm X patent pending technology' },
          { title: 'First Snapchat API Access', year: '2017', desc: 'FlyrTV was the first third-party with Snapchat API integration' },
          { title: 'Ariel Awards - VFX Winner', year: '2008', desc: 'First Mexican film VFX winner (Mexican Academy Award equivalent)' },
          { title: 'Visual Effects Society Member', year: '2010+', desc: 'Recognized member of the Visual Effects Society' }
        ].map((item, i) => (
          <Box key={i} sx={{ mb: 6, textAlign: 'center' }}>
            <Typography variant="h6" sx={{ color: '#0071E3', mb: 1 }}>{item.year}</Typography>
            <Typography variant="h4" sx={{ color: '#fff', mb: 1 }}>{item.title}</Typography>
            <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.7)' }}>{item.desc}</Typography>
          </Box>
        ))}
      </Section>

      {/* Filmography */}
      <Section id="filmography">
        <Typography variant="h2" sx={{ mb: 2, color: '#fff', textAlign: 'center' }}>Filmography</Typography>
        <Typography variant="h4" sx={{ mb: 8, color: 'rgba(255,255,255,0.7)', textAlign: 'center', fontWeight: 400 }}>
          10+ Feature Films | 2006-2010
        </Typography>
        <FullWidthVideo src="https://www.youtube.com/embed/cS9tKYNIOxg" title="VFX Reel" />
        <FullWidthVideo src="https://www.youtube.com/embed/H1D5HITPAhc" title="Creative Engineering" />
        <Box sx={{ textAlign: 'center', mt: 6 }}>
          <Button variant="contained" href="https://www.imdb.com/name/nm2843359/" target="_blank">
            View IMDB Profile
          </Button>
        </Box>
      </Section>

      {/* Footer */}
      <Box id="contact" sx={{ py: 12, background: 'rgba(0,0,0,0.95)' }}>
        <Container maxWidth="lg">
          <Typography variant="h3" sx={{ color: '#fff', textAlign: 'center', mb: 4 }}>
            Contact
          </Typography>
          <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.8)', textAlign: 'center', mb: 4, fontSize: '1.3rem' }}>
            hassan.uriostegui@gmail.com
          </Typography>
          <Box sx={{ textAlign: 'center', mb: 6 }}>
            {[
              { label: 'LinkedIn', url: 'https://www.linkedin.com/in/bensabbah' },
              { label: 'GitHub', url: 'https://github.com/hassanvfx' },
              { label: 'Medium', url: 'https://uriostegui.medium.com' },
              { label: 'Waken.ai', url: 'https://www.wakenai.com' }
            ].map((link, i) => (
              <Button key={i} variant="outlined" href={link.url} target="_blank" sx={{ mx: 1, my: 1 }}>
                {link.label}
              </Button>
            ))}
          </Box>
          <Typography variant="body2" sx={{ color: 'rgba(255,255,255,0.4)', textAlign: 'center' }}>
            2025 Hassan Uriostegui. EB1A Extraordinary Ability.
          </Typography>
        </Container>
      </Box>

    </ThemeProvider>
  );
}

export default App;
