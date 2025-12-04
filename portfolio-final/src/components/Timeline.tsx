import { Box, Typography } from '@mui/material';
import { GlassPanel } from './GlassPanel';

interface TimelineItem {
  year: string;
  title: string;
  description: string;
  side?: 'left' | 'right';
}

interface TimelineProps {
  items: TimelineItem[];
  variant?: 'vertical' | 'horizontal';
}

export const Timeline = ({ items, variant = 'vertical' }: TimelineProps) => {
  if (variant === 'horizontal') {
    return (
      <Box sx={{ display: 'flex', gap: 3, overflowX: 'auto', pb: 4 }}>
        {items.map((item, i) => (
          <Box key={i} sx={{ minWidth: 300, flex: '0 0 auto' }}>
            <GlassPanel sx={{ height: '100%' }}>
              <Typography variant="h6" sx={{ color: '#0071E3', mb: 1 }}>
                {item.year}
              </Typography>
              <Typography variant="h5" sx={{ color: '#fff', mb: 2 }}>
                {item.title}
              </Typography>
              <Typography variant="body2" sx={{ color: 'rgba(255,255,255,0.7)' }}>
                {item.description}
              </Typography>
            </GlassPanel>
          </Box>
        ))}
      </Box>
    );
  }

  return (
    <Box sx={{ position: 'relative', pl: { xs: 0, md: 6 } }}>
      {/* Timeline line */}
      <Box
        sx={{
          display: { xs: 'none', md: 'block' },
          position: 'absolute',
          left: 0,
          top: 0,
          bottom: 0,
          width: '2px',
          background: 'linear-gradient(to bottom, transparent, rgba(0,113,227,0.5), transparent)',
        }}
      />
      
      {items.map((item, i) => (
        <Box
          key={i}
          sx={{
            position: 'relative',
            mb: 6,
            ml: { xs: 0, md: item.side === 'left' ? -20 : 0 },
          }}
        >
          {/* Timeline dot */}
          <Box
            sx={{
              display: { xs: 'none', md: 'block' },
              position: 'absolute',
              left: -28,
              top: 8,
              width: 12,
              height: 12,
              borderRadius: '50%',
              background: '#0071E3',
              boxShadow: '0 0 20px rgba(0,113,227,0.8)',
            }}
          />
          
          <GlassPanel>
            <Typography variant="h6" sx={{ color: '#0071E3', mb: 1 }}>
              {item.year}
            </Typography>
            <Typography variant="h4" sx={{ color: '#fff', mb: 2 }}>
              {item.title}
            </Typography>
            <Typography variant="body1" sx={{ color: 'rgba(255,255,255,0.7)' }}>
              {item.description}
            </Typography>
          </GlassPanel>
        </Box>
      ))}
    </Box>
  );
};

export default Timeline;
