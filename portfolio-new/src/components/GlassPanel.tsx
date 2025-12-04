import { Box } from '@mui/material';

interface GlassPanelProps {
  children: React.ReactNode;
  sx?: any;
}

export const GlassPanel = ({ children, sx = {} }: GlassPanelProps) => (
  <Box
    sx={{
      background: 'rgba(255, 255, 255, 0.03)',
      backdropFilter: 'blur(20px)',
      border: '1px solid rgba(255, 255, 255, 0.1)',
      borderRadius: '24px',
      padding: 4,
      boxShadow: '0 8px 32px 0 rgba(0, 0, 0, 0.37)',
      position: 'relative',
      overflow: 'hidden',
      '&::before': {
        content: '""',
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        height: '1px',
        background: 'linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent)',
      },
      ...sx,
    }}
  >
    {children}
  </Box>
);

export default GlassPanel;
