import { Box, Container, Typography, Grid, Card, CardContent, Chip, Stack } from '@mui/material';
import { motion } from 'framer-motion';
import { portfolioData } from '../data/portfolio';
import { glassStyles } from '../theme/theme';

const PressSection = () => {
  const { press } = portfolioData;

  return (
    <Box sx={{ py: 10, position: 'relative' }} id="press">
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
            {press.title}
          </Typography>
          <Typography
            variant="h5"
            sx={{
              mb: 8,
              textAlign: 'center',
              color: 'rgba(255, 255, 255, 0.7)',
            }}
          >
            {press.subtitle}
          </Typography>
        </motion.div>

        <Grid container spacing={3}>
          {press.items.map((item, index) => (
            <Grid item xs={12} sm={6} md={4} key={index}>
              <motion.div
                initial={{ opacity: 0, scale: 0.9 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.05 }}
              >
                <Card
                  component={item.url ? 'a' : 'div'}
                  href={item.url}
                  target={item.url ? "_blank" : undefined}
                  sx={{
                    height: '100%',
                    textDecoration: 'none',
                    cursor: item.url ? 'pointer' : 'default',
                    display: 'block',
                    position: 'relative',
                    overflow: 'hidden',
                  }}
                >
                  <CardContent sx={{ p: 3 }}>
                    <Stack direction="row" spacing={1} sx={{ mb: 2 }}>
                      <Chip 
                        label={item.type} 
                        size="small"
                        color="secondary"
                      />
                      <Chip 
                        label={item.date} 
                        size="small"
                        sx={{ ...glassStyles.glass }}
                      />
                    </Stack>

                    <Typography
                      variant="h6"
                      sx={{
                        mb: 1,
                        color: '#4A90E2',
                        fontWeight: 600,
                        fontSize: '1.1rem',
                      }}
                    >
                      {item.publication}
                    </Typography>

                    <Typography
                      variant="body1"
                      sx={{
                        color: 'rgba(255, 255, 255, 0.9)',
                        lineHeight: 1.6,
                        fontSize: '0.95rem',
                      }}
                    >
                      {item.title}
                    </Typography>
                  </CardContent>

                  {/* Hover indicator */}
                  {item.url && (
                    <Box
                      sx={{
                        position: 'absolute',
                        bottom: 0,
                        left: 0,
                        right: 0,
                        height: '3px',
                        background: 'linear-gradient(90deg, #4A90E2 0%, #8B5CF6 100%)',
                        transform: 'scaleX(0)',
                        transformOrigin: 'left',
                        transition: 'transform 0.3s ease',
                        '.MuiCard-root:hover &': {
                          transform: 'scaleX(1)',
                        },
                      }}
                    />
                  )}
                </Card>
              </motion.div>
            </Grid>
          ))}
        </Grid>
      </Container>
    </Box>
  );
};

export default PressSection;
