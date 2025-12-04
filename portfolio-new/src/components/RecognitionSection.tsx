import { Box, Container, Typography, Grid, Card, CardContent } from '@mui/material';
import { motion } from 'framer-motion';
import { portfolioData } from '../data/portfolio';
import { glassStyles } from '../theme/theme';

const RecognitionSection = () => {
  const { recognition } = portfolioData;

  return (
    <Box sx={{ py: 10, position: 'relative' }} id="recognition">
      {/* Decorative elements */}
      <Box
        sx={{
          position: 'absolute',
          width: '400px',
          height: '400px',
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(139,92,246,0.15) 0%, transparent 70%)',
          bottom: '10%',
          right: '-200px',
          pointerEvents: 'none',
          animation: 'float 12s ease-in-out infinite',
          '@keyframes float': {
            '0%, 100%': { transform: 'translateY(0px)' },
            '50%': { transform: 'translateY(-40px)' },
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
            {recognition.title}
          </Typography>
          <Typography
            variant="h5"
            sx={{
              mb: 8,
              textAlign: 'center',
              color: 'rgba(255, 255, 255, 0.7)',
            }}
          >
            Extraordinary achievements in technology and innovation
          </Typography>
        </motion.div>

        <Grid container spacing={3}>
          {recognition.items.map((item, index) => (
            <Grid item xs={12} sm={6} md={4} key={index}>
              <motion.div
                initial={{ opacity: 0, y: 50 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
                whileHover={{ y: -10 }}
              >
                <Card
                  sx={{
                    height: '100%',
                    textAlign: 'center',
                    position: 'relative',
                    overflow: 'hidden',
                  }}
                >
                  <CardContent sx={{ p: 4 }}>
                    {/* Icon */}
                    <Box
                      sx={{
                        fontSize: '3.5rem',
                        mb: 2,
                        filter: 'drop-shadow(0 0 20px rgba(74,144,226,0.5))',
                      }}
                    >
                      {item.icon}
                    </Box>

                    {/* Year badge */}
                    <Box
                      sx={{
                        ...glassStyles.glass,
                        display: 'inline-block',
                        px: 2,
                        py: 0.5,
                        borderRadius: '12px',
                        mb: 2,
                      }}
                    >
                      <Typography variant="body2" sx={{ fontWeight: 600 }}>
                        {item.year}
                      </Typography>
                    </Box>

                    <Typography
                      variant="h5"
                      sx={{
                        mb: 2,
                        ...glassStyles.gradientText,
                        fontSize: '1.3rem',
                        fontWeight: 600,
                      }}
                    >
                      {item.title}
                    </Typography>

                    <Typography
                      variant="body1"
                      sx={{
                        color: 'rgba(255, 255, 255, 0.7)',
                        lineHeight: 1.7,
                      }}
                    >
                      {item.description}
                    </Typography>
                  </CardContent>

                  {/* Decorative corner accent */}
                  <Box
                    sx={{
                      position: 'absolute',
                      top: 0,
                      right: 0,
                      width: '60px',
                      height: '60px',
                      background: 'linear-gradient(135deg, rgba(74,144,226,0.3) 0%, transparent 70%)',
                      borderBottomLeftRadius: '100%',
                    }}
                  />
                </Card>
              </motion.div>
            </Grid>
          ))}
        </Grid>
      </Container>
    </Box>
  );
};

export default RecognitionSection;
