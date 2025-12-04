import { Box, Container, Typography, CardMedia } from '@mui/material';
import { motion } from 'framer-motion';
import { portfolioData } from '../data/portfolio';
import { glassStyles } from '../theme/theme';

const AIVideos2024 = () => {
  const { aiVideos2024 } = portfolioData;

  return (
    <Box sx={{ py: 10, position: 'relative' }} id="ai-2024">
      {/* Animated background element */}
      <Box
        sx={{
          position: 'absolute',
          width: '600px',
          height: '600px',
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(139,92,246,0.12) 0%, transparent 70%)',
          top: '10%',
          left: '-300px',
          pointerEvents: 'none',
          animation: 'pulse 8s ease-in-out infinite',
          '@keyframes pulse': {
            '0%, 100%': { transform: 'scale(1)' },
            '50%': { transform: 'scale(1.1)' },
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
            {aiVideos2024.title}
          </Typography>
          <Typography
            variant="h6"
            sx={{
              mb: 6,
              textAlign: 'center',
              color: 'rgba(255, 255, 255, 0.7)',
            }}
          >
            {aiVideos2024.description}
          </Typography>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
          transition={{ duration: 0.7 }}
        >
          <Box
            sx={{
              ...glassStyles.glass,
              p: { xs: 2, md: 4 },
              borderRadius: '24px',
              maxWidth: '1000px',
              margin: '0 auto',
            }}
          >
            {/* 16:9 Video Container */}
            <Box
              sx={{
                position: 'relative',
                paddingTop: '56.25%',
                width: '100%',
                overflow: 'hidden',
                borderRadius: '16px',
              }}
            >
              <CardMedia
                component="iframe"
                src={aiVideos2024.playlistUrl}
                title={aiVideos2024.title}
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
          </Box>
        </motion.div>
      </Container>
    </Box>
  );
};

export default AIVideos2024;
