import { Box, Container, Typography, Grid, Button } from '@mui/material';
import { motion } from 'framer-motion';
import { glassStyles } from '../theme/theme';

const EB1ASection = () => {
  return (
    <Box sx={{ py: 15, position: 'relative' }} id="eb1a">
      <Container maxWidth="lg">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
        >
          {/* Section Header */}
          <Box sx={{ mb: 10, textAlign: 'center' }}>
            <Typography
              variant="h6"
              sx={{
                mb: 2,
                color: 'rgba(255, 255, 255, 0.6)',
              }}
            >
              Immigration Status
            </Typography>
            <Typography
              variant="h2"
              sx={{
                mb: 4,
                ...glassStyles.gradientText,
              }}
            >
              EB1A Extraordinary Ability
            </Typography>
          </Box>

          {/* Main Content */}
          <Grid container spacing={6}>
            <Grid item xs={12} md={6}>
              <Box
                sx={{
                  ...glassStyles.glass,
                  p: 5,
                  height: '100%',
                }}
              >
                <Typography
                  variant="h4"
                  sx={{
                    mb: 3,
                    fontFamily: '"Montserrat", sans-serif',
                  }}
                >
                  What is EB1A?
                </Typography>
                <Typography
                  variant="body1"
                  sx={{
                    mb: 3,
                    color: 'rgba(255, 255, 255, 0.85)',
                  }}
                >
                  The EB-1A visa classification is reserved for individuals who can demonstrate 
                  <strong style={{ color: '#4A90E2' }}> sustained national or international acclaim</strong> and 
                  recognition in their field through extensive documentation.
                </Typography>
                <Typography
                  variant="body1"
                  sx={{
                    mb: 3,
                    color: 'rgba(255, 255, 255, 0.85)',
                  }}
                >
                  This classification is one of the highest employment-based immigration categories in the United States, 
                  granted to those who have risen to the very top of their field in sciences, arts, education, business, or athletics.
                </Typography>
                <Button
                  variant="outlined"
                  href="https://en.wikipedia.org/wiki/EB-1_visa"
                  target="_blank"
                  sx={{
                    borderColor: 'rgba(255, 255, 255, 0.3)',
                    color: '#4A90E2',
                    '&:hover': {
                      borderColor: '#4A90E2',
                    },
                  }}
                >
                  Learn More on Wikipedia
                </Button>
              </Box>
            </Grid>

            <Grid item xs={12} md={6}>
              <Box
                sx={{
                  ...glassStyles.glass,
                  p: 5,
                  height: '100%',
                  background: 'rgba(74, 144, 226, 0.08)',
                  border: '1px solid rgba(74, 144, 226, 0.3)',
                }}
              >
                <Typography
                  variant="h4"
                  sx={{
                    mb: 3,
                    fontFamily: '"Montserrat", sans-serif',
                    color: '#4A90E2',
                  }}
                >
                  Hassan's Qualification
                </Typography>
                <Typography
                  variant="body1"
                  sx={{
                    mb: 2,
                    color: 'rgba(255, 255, 255, 0.9)',
                  }}
                >
                  Hassan Uriostegui earned the EB1A classification in recognition of his 
                  <strong> extraordinary career in computer sciences</strong>, demonstrating:
                </Typography>
                <Box component="ul" sx={{ pl: 3, color: 'rgba(255, 255, 255, 0.85)' }}>
                  <li>
                    <Typography variant="body1" sx={{ mb: 1.5 }}>
                      <strong>Original contributions of major significance:</strong> Mind Simulation Therapy framework, 
                      first 2K mobile recording, patent-pending rendering platform
                    </Typography>
                  </li>
                  <li>
                    <Typography variant="body1" sx={{ mb: 1.5 }}>
                      <strong>Sustained acclaim:</strong> Featured at Apple WWDC, covered by TechCrunch, Forbes, 
                      and international media
                    </Typography>
                  </li>
                  <li>
                    <Typography variant="body1" sx={{ mb: 1.5 }}>
                      <strong>Impact at scale:</strong> Built products serving 40+ million users, raised $6M+ in funding, 
                      multiple successful exits
                    </Typography>
                  </li>
                  <li>
                    <Typography variant="body1">
                      <strong>Leadership recognition:</strong> Principal Engineer positions, CTO roles, published author 
                      and researcher
                    </Typography>
                  </li>
                </Box>
              </Box>
            </Grid>
          </Grid>

          {/* Stats Bar */}
          <Box sx={{ mt: 8 }}>
            <Grid container spacing={3}>
              {[
                { label: 'Users Impacted', value: '40M+' },
                { label: 'Funding Raised', value: '$6M+' },
                { label: 'Products Launched', value: '10,000+' },
                { label: 'Years in Silicon Valley', value: '10+' },
                { label: 'Books Published', value: '4' },
                { label: 'Patents', value: '1' },
              ].map((stat, index) => (
                <Grid item xs={6} sm={4} md={2} key={index}>
                  <Box
                    sx={{
                      ...glassStyles.glass,
                      p: 3,
                      textAlign: 'center',
                    }}
                  >
                    <Typography
                      variant="h3"
                      sx={{
                        mb: 1,
                        ...glassStyles.gradientText,
                        fontFamily: '"Playfair Display", serif',
                      }}
                    >
                      {stat.value}
                    </Typography>
                    <Typography
                      variant="body2"
                      sx={{
                        color: 'rgba(255, 255, 255, 0.7)',
                        fontSize: '0.875rem',
                      }}
                    >
                      {stat.label}
                    </Typography>
                  </Box>
                </Grid>
              ))}
            </Grid>
          </Box>
        </motion.div>
      </Container>
    </Box>
  );
};

export default EB1ASection;
