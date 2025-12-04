import { Box, Container, Typography, Grid } from '@mui/material';
import { motion } from 'framer-motion';

const Hero = () => {
  return (
    <Box
      sx={{
        minHeight: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        position: 'relative',
        py: { xs: 10, md: 15 },
      }}
    >
      <Container maxWidth="lg">
        <Box sx={{ textAlign: 'center', mb: 8 }}>
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
          >
            <Typography
              variant="h1"
              sx={{
                mb: 3,
                fontSize: { xs: '3rem', md: '5rem', lg: '6rem' },
                fontWeight: 800,
                color: '#ffffff',
              }}
            >
              Hassan Uriostegui
            </Typography>
          </motion.div>

          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.6, delay: 0.2 }}
          >
            <Typography
              variant="h4"
              sx={{
                mb: 2,
                fontSize: { xs: '1.25rem', md: '1.75rem' },
                color: '#4A90E2',
                fontFamily: '"Montserrat", sans-serif',
                fontWeight: 600,
              }}
            >
              EB1A Extraordinary Ability • Principal Engineer
            </Typography>
          </motion.div>

          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.6, delay: 0.4 }}
          >
            <Typography
              variant="h5"
              sx={{
                mb: 6,
                fontSize: { xs: '1.1rem', md: '1.5rem' },
                color: 'rgba(255, 255, 255, 0.8)',
                fontWeight: 400,
                maxWidth: '900px',
                margin: '0 auto 3rem',
                lineHeight: 1.6,
              }}
            >
              Silicon Valley Innovator • AI Pioneer • Author
            </Typography>
          </motion.div>

          {/* Stats Grid */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.6 }}
          >
            <Grid container spacing={4} sx={{ maxWidth: '1000px', margin: '0 auto' }}>
              {[
                { value: '40M+', label: 'Users Impacted' },
                { value: '$6M+', label: 'Funding Raised' },
                { value: '10K+', label: 'Products Launched' },
                { value: '10+', label: 'Years Silicon Valley' },
              ].map((stat, index) => (
                <Grid item xs={6} md={3} key={index}>
                  <Box>
                    <Typography
                      variant="h2"
                      sx={{
                        mb: 1,
                        fontSize: { xs: '2.5rem', md: '3.5rem' },
                        fontWeight: 700,
                        color: '#ffffff',
                        fontFamily: '"Playfair Display", serif',
                      }}
                    >
                      {stat.value}
                    </Typography>
                    <Typography
                      variant="body2"
                      sx={{
                        color: 'rgba(255, 255, 255, 0.6)',
                        fontSize: '0.875rem',
                        textTransform: 'uppercase',
                        letterSpacing: '0.1em',
                      }}
                    >
                      {stat.label}
                    </Typography>
                  </Box>
                </Grid>
              ))}
            </Grid>
          </motion.div>
        </Box>
      </Container>
    </Box>
  );
};

export default Hero;
