import { Box, Container, Typography, Grid, Button } from '@mui/material';
import { motion } from 'framer-motion';
import { portfolioData } from '../data/portfolio';
import { glassStyles } from '../theme/theme';
import ProjectCard from './ProjectCard';

const FilmographySection = () => {
  const { filmography } = portfolioData;

  return (
    <Box sx={{ py: 10 }} id="filmography">
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
            {filmography.title}
          </Typography>
          <Typography
            variant="h6"
            sx={{
              mb: 2,
              textAlign: 'center',
              color: 'rgba(255, 255, 255, 0.7)',
            }}
          >
            {filmography.description}
          </Typography>
          <Typography
            variant="body1"
            sx={{
              mb: 4,
              textAlign: 'center',
              color: 'rgba(255, 255, 255, 0.6)',
            }}
          >
            {filmography.ves}
          </Typography>
          <Box sx={{ textAlign: 'center', mb: 6 }}>
            <Button
              variant="contained"
              href={filmography.imdbLink}
              target="_blank"
            >
              View IMDB Profile
            </Button>
          </Box>
        </motion.div>

        <Grid container spacing={4}>
          {filmography.projects.map((project, index) => (
            <Grid item xs={12} md={6} key={index}>
              <ProjectCard
                title={project.title}
                subtitle={project.subtitle}
                description={project.description}
                year="2006-2011"
                videoUrl={project.videoUrl}
                index={index}
              />
            </Grid>
          ))}
        </Grid>
      </Container>
    </Box>
  );
};

export default FilmographySection;
