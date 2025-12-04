import { Card, CardContent, Typography, Box, Button, CardMedia } from '@mui/material';
import { motion } from 'framer-motion';
import { glassStyles } from '../theme/theme';

interface ProjectCardProps {
  title: string;
  subtitle: string;
  description: string;
  year: string;
  videoUrl?: string;
  link?: string;
  isVimeo?: boolean;
  index: number;
}

const ProjectCard = ({ 
  title, 
  subtitle, 
  description, 
  year, 
  videoUrl, 
  link,
  index 
}: ProjectCardProps) => {
  return (
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
        {/* Year badge */}
        <Box
          sx={{
            position: 'absolute',
            top: 20,
            right: 20,
            ...glassStyles.glass,
            px: 2,
            py: 1,
            zIndex: 2,
          }}
        >
          <Typography variant="body2" sx={{ fontWeight: 600 }}>
            {year}
          </Typography>
        </Box>

        {/* Video embed with 16:9 aspect ratio */}
        {videoUrl && (
          <Box
            sx={{
              position: 'relative',
              paddingTop: '56.25%', // 16:9 aspect ratio
              width: '100%',
              overflow: 'hidden',
            }}
          >
            <CardMedia
              component="iframe"
              src={videoUrl}
              title={title}
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
        )}

        <CardContent sx={{ flexGrow: 1, p: 3 }}>
          <Typography
            variant="h4"
            sx={{
              mb: 1,
              ...glassStyles.gradientText,
            }}
          >
            {title}
          </Typography>

          <Typography
            variant="h6"
            sx={{
              mb: 2,
              color: 'rgba(255, 255, 255, 0.8)',
              fontSize: '1rem',
            }}
          >
            {subtitle}
          </Typography>

          <Typography
            variant="body1"
            sx={{
              mb: 3,
              color: 'rgba(255, 255, 255, 0.7)',
              lineHeight: 1.7,
            }}
          >
            {description}
          </Typography>

          {link && (
            <Button
              variant="contained"
              href={link}
              target="_blank"
              sx={{ mt: 'auto' }}
            >
              Learn More
            </Button>
          )}
        </CardContent>

        {/* Decorative gradient overlay */}
        <Box
          sx={{
            position: 'absolute',
            bottom: 0,
            left: 0,
            right: 0,
            height: '4px',
            background: 'linear-gradient(90deg, #4A90E2 0%, #8B5CF6 50%, #06B6D4 100%)',
            opacity: 0,
            transition: 'opacity 0.3s ease',
            '.MuiCard-root:hover &': {
              opacity: 1,
            },
          }}
        />
      </Card>
    </motion.div>
  );
};

export default ProjectCard;
