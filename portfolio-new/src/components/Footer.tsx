import { Box, Container, Typography } from '@mui/material';
import { portfolioData } from '../data/portfolio';
import { glassStyles } from '../theme/theme';

const Footer = () => {
  const { contact } = portfolioData;

  return (
    <Box
      component="footer"
      sx={{
        py: 6,
        mt: 10,
        borderTop: '1px solid rgba(255, 255, 255, 0.1)',
      }}
    >
      <Container maxWidth="lg">
        <Box
          sx={{
            ...glassStyles.glass,
            p: 4,
            textAlign: 'center',
          }}
        >
          <Typography
            variant="h4"
            sx={{
              mb: 2,
              ...glassStyles.gradientText,
            }}
          >
            Get In Touch
          </Typography>
          <Typography
            variant="h6"
            sx={{
              mb: 4,
              color: 'rgba(255, 255, 255, 0.9)',
            }}
          >
            <a
              href={`mailto:${contact.email}`}
              style={{
                color: 'inherit',
                textDecoration: 'none',
                transition: 'all 0.3s ease',
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.color = '#4A90E2';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.color = 'rgba(255, 255, 255, 0.9)';
              }}
            >
              {contact.email}
            </a>
          </Typography>
          <Typography
            variant="body2"
            sx={{
              color: 'rgba(255, 255, 255, 0.5)',
            }}
          >
            © {new Date().getFullYear()} Hassan Uriostegui. All rights reserved.
          </Typography>
        </Box>
      </Container>
    </Box>
  );
};

export default Footer;
