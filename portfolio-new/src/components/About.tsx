import { Box, Container, Typography } from '@mui/material';
import { motion } from 'framer-motion';
import { portfolioData } from '../data/portfolio';
import { glassStyles } from '../theme/theme';

const About = () => {
  const { about } = portfolioData;

  return (
    <Box sx={{ py: 10 }}>
      <Container maxWidth="lg">
        <motion.div
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
        >
          <Box
            sx={{
              ...glassStyles.glass,
              p: { xs: 4, md: 6 },
              textAlign: 'center',
              position: 'relative',
            }}
          >
            <Box
              sx={{
                maxWidth: '800px',
                margin: '0 auto',
              }}
            >
              <Typography
                variant="h3"
                sx={{
                  mb: 4,
                  fontStyle: 'italic',
                  color: 'rgba(255, 255, 255, 0.9)',
                  lineHeight: 1.6,
                }}
              >
                "{about.quote}"
              </Typography>
              <Typography
                variant="h6"
                sx={{
                  color: 'rgba(255, 255, 255, 0.7)',
                  fontWeight: 600,
                }}
              >
                — {about.author}
              </Typography>
            </Box>

            {/* Decorative elements */}
            <Box
              sx={{
                position: 'absolute',
                width: '100px',
                height: '100px',
                borderRadius: '50%',
                background: 'radial-gradient(circle, rgba(139,92,246,0.2) 0%, transparent 70%)',
                top: '-50px',
                left: '-50px',
                pointerEvents: 'none',
              }}
            />
            <Box
              sx={{
                position: 'absolute',
                width: '150px',
                height: '150px',
                borderRadius: '50%',
                background: 'radial-gradient(circle, rgba(6,182,212,0.15) 0%, transparent 70%)',
                bottom: '-75px',
                right: '-75px',
                pointerEvents: 'none',
              }}
            />
          </Box>
        </motion.div>
      </Container>
    </Box>
  );
};

export default About;
