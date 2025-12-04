import { Box, Container, Typography, Grid } from '@mui/material';
import { motion } from 'framer-motion';
import { portfolioData } from '../data/portfolio';
import { glassStyles } from '../theme/theme';
import ProjectCard from './ProjectCard';

const ProductsSection = () => {
  const { products } = portfolioData;

  return (
    <Box sx={{ py: 10 }} id="products">
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
            World Class Products
          </Typography>
          <Typography
            variant="h6"
            sx={{
              mb: 6,
              textAlign: 'center',
              color: 'rgba(255, 255, 255, 0.7)',
            }}
          >
            Building innovative solutions that shape the future
          </Typography>
        </motion.div>

        <Grid container spacing={4}>
          {products.map((product, index) => (
            <Grid item xs={12} key={product.id}>
              <ProjectCard
                title={product.title}
                subtitle={product.subtitle}
                description={product.description}
                year={product.year}
                videoUrl={product.videoUrl}
                link={product.link}
                index={index}
              />
            </Grid>
          ))}
        </Grid>
      </Container>
    </Box>
  );
};

export default ProductsSection;
