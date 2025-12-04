import { Box, Container, Typography, Grid, CardMedia } from '@mui/material';
import { motion } from 'framer-motion';
import { portfolioData } from '../data/portfolio';
import { glassStyles } from '../theme/theme';

const AIVideos2025 = () => {
  const { aiVideos2025 } = portfolioData;

  return (
    <Box sx={{ py: 10, position: 'relative' }} id="ai-2025">
      {/* Animated background element */}
      <Box
        sx={{
          position: 'absolute',
          width: '500px',
          height: '500px',
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(6,182,212,0.15) 0%, transparent 70%)',
          top: '20%',
          right: '-250px',
          pointerEvents: 'none',
          animation: 'float 10s ease-in-out infinite',
          '@keyframes float': {
            '0%, 100%': { transform: 'translateY(0px)' },
            '50%': { transform: 'translateY(-30px)' },
          },
        }}
      />

      <Container maxWidth="lg">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
        >
          <Typography
            variant="h2"
            sx={{
              mb: 2,
              textAlign: 'center',
              ...glassStyles.gradientText,
            }}
          >
            AI Innovations 2025
          </Typography>
          <Typography
            variant="h6"
            sx={{
              mb: 6,
              textAlign: 'center',
              color: 'rgba(255, 255, 255, 0.7)',
            }}
          >
            Latest breakthroughs in artificial intelligence and human-AI interaction
          </Typography>
        </motion.div>

        <Grid container spacing={3}>
          {aiVideos2025.map((video, index) => (
            <Grid item xs={12} sm={6} md={4} key={video.id}>
              <motion.div
                initial={{ opacity: 0, scale: 0.9 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
              >
                <Box
                  sx={{
                    ...glassStyles.glass,
                    ...glassStyles.glassHover,
                    p: 2,
                    borderRadius: '16px',
                    transition: 'all 0.3s ease',
                  }}
                >
                  {/* 16:9 Video Container */}
                  <Box
                    sx={{
                      position: 'relative',
                      paddingTop: '56.25%',
                      width: '100%',
                      overflow: 'hidden',
                      borderRadius: '12px',
                      mb: 2,
                    }}
                  >
                    <CardMedia
                      component="iframe"
                      src={video.videoUrl}
                      title={video.title}
                      sx={{
                        position: 'absolute',
                        top: 0,
                        left: 0,
                        width: '100%',
                        height: '100%',
                        border: 'none',
                      }}
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                      allowFullScreen
                    />
                  </Box>
                  <Typography
                    variant="body1"
                    sx={{
                      color: 'rgba(255, 255, 255, 0.9)',
                      fontWeight: 500,
                      textAlign: 'center',
                    }}
                  >
                    {video.title}
                  </Typography>
                </Box>
              </motion.div>
            </Grid>
          ))}
        </Grid>
      </Container>
    </Box>
  );
};

export default AIVideos2025;
