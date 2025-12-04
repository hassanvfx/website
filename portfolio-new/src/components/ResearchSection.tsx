import { Box, Container, Typography, Grid } from '@mui/material';
import { motion } from 'framer-motion';
import { portfolioData } from '../data/portfolio';
import { glassStyles } from '../theme/theme';
import ProjectCard from './ProjectCard';

const ResearchSection = () => {
  const { research } = portfolioData;

  return (
    <Box sx={{ py: 10, position: 'relative' }} id="research">
      {/* Parallax background element */}
      <Box
        sx={{
          position: 'absolute',
          width: '400px',
          height: '400px',
          borderRadius: '50%',
          background: 'radial-gradient(circle, rgba(139,92,246,0.1) 0%, transparent 70%)',
          top: '10%',
          left: '-200px',
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
            Research & Development
          </Typography>
          <Typography
            variant="h6"
            sx={{
              mb: 6,
              textAlign: 'center',
              color: 'rgba(255, 255, 255, 0.7)',
            }}
          >
            Pioneering technologies ahead of their time
          </Typography>
        </motion.div>

        <Grid container spacing={4}>
          {research.map((project, index) => (
            <Grid item xs={12} md={6} key={project.id}>
              <ProjectCard
                title={project.title}
                subtitle={project.subtitle}
                description={project.description}
                year={project.year}
                videoUrl={project.videoUrl}
                isVimeo={project.isVimeo}
                index={index}
              />
            </Grid>
          ))}
        </Grid>
      </Container>
    </Box>
  );
};

export default ResearchSection;
