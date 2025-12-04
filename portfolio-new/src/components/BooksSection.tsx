import { Box, Container, Typography, Grid, Card, CardContent, Button, Chip, Stack } from '@mui/material';
import { motion } from 'framer-motion';
import { portfolioData } from '../data/portfolio';
import { glassStyles } from '../theme/theme';

const BooksSection = () => {
  const { books } = portfolioData;

  return (
    <Box sx={{ py: 10, position: 'relative' }} id="books">
      {/* Decorative background */}
      <Box
        sx={{
          position: 'absolute',
          width: '700px',
          height: '700px',
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(74,144,226,0.15) 0%, transparent 70%)',
          top: '-200px',
          left: '50%',
          transform: 'translateX(-50%)',
          pointerEvents: 'none',
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
            {books.title}
          </Typography>
          <Typography
            variant="h5"
            sx={{
              mb: 8,
              textAlign: 'center',
              color: 'rgba(255, 255, 255, 0.7)',
              maxWidth: '800px',
              margin: '0 auto 4rem',
            }}
          >
            {books.subtitle}
          </Typography>
        </motion.div>

        <Grid container spacing={4}>
          {books.items.map((book, index) => (
            <Grid item xs={12} md={6} key={index}>
              <motion.div
                initial={{ opacity: 0, y: 50 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.6, delay: index * 0.1 }}
              >
                <Card
                  sx={{
                    height: '100%',
                    display: 'flex',
                    flexDirection: 'column',
                    position: 'relative',
                    overflow: 'hidden',
                  }}
                >
                  <CardContent sx={{ p: 4, flexGrow: 1 }}>
                    <Stack direction="row" spacing={2} sx={{ mb: 2 }}>
                      <Chip 
                        label={book.year} 
                        sx={{ 
                          ...glassStyles.glass,
                          fontWeight: 600,
                        }} 
                      />
                      <Chip 
                        label={book.language} 
                        color="primary"
                      />
                    </Stack>

                    <Typography
                      variant="h4"
                      sx={{
                        mb: 1,
                        ...glassStyles.gradientText,
                        fontSize: '1.8rem',
                      }}
                    >
                      {book.title}
                    </Typography>

                    <Typography
                      variant="h6"
                      sx={{
                        mb: 3,
                        color: 'rgba(255, 255, 255, 0.8)',
                        fontSize: '1.1rem',
                        fontStyle: 'italic',
                      }}
                    >
                      {book.subtitle}
                    </Typography>

                    <Typography
                      variant="body1"
                      sx={{
                        mb: 3,
                        color: 'rgba(255, 255, 255, 0.7)',
                        lineHeight: 1.8,
                      }}
                    >
                      {book.description}
                    </Typography>

                    <Stack direction="row" spacing={2} flexWrap="wrap">
                      {book.amazonUrl && (
                        <Button
                          variant="contained"
                          href={book.amazonUrl}
                          target="_blank"
                          sx={{ mb: 1 }}
                        >
                          View on Amazon
                        </Button>
                      )}
                      {book.pressUrl && (
                        <Button
                          variant="outlined"
                          href={book.pressUrl}
                          target="_blank"
                          sx={{ 
                            mb: 1,
                            borderColor: 'rgba(255, 255, 255, 0.2)',
                          }}
                        >
                          Press Coverage
                        </Button>
                      )}
                      {book.mediaUrl && (
                        <Button
                          variant="outlined"
                          href={book.mediaUrl}
                          target="_blank"
                          sx={{ 
                            mb: 1,
                            borderColor: 'rgba(255, 255, 255, 0.2)',
                          }}
                        >
                          Media Interview
                        </Button>
                      )}
                    </Stack>
                  </CardContent>

                  {/* Decorative gradient bar */}
                  <Box
                    sx={{
                      position: 'absolute',
                      top: 0,
                      left: 0,
                      right: 0,
                      height: '4px',
                      background: 'linear-gradient(90deg, #4A90E2 0%, #8B5CF6 50%, #06B6D4 100%)',
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

export default BooksSection;
