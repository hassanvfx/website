import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';

export const Navigation = () => {
  const menuItems = [
    { label: 'Home', href: '#home' },
    { label: 'Projects', href: '#twinchat' },
    { label: 'Press', href: '#press' },
    { label: 'Books', href: '#books' },
    { label: 'Recognition', href: '#recognition' },
    { label: 'Contact', href: '#contact' },
  ];

  return (
    <AppBar 
      position="sticky" 
      sx={{ 
        background: 'rgba(0, 0, 0, 0.7)',
        backdropFilter: 'blur(20px)',
        borderBottom: '1px solid rgba(255, 255, 255, 0.1)',
        boxShadow: '0 4px 30px rgba(0, 0, 0, 0.5)',
      }}
    >
      <Toolbar sx={{ justifyContent: 'space-between' }}>
        <Typography variant="h6" sx={{ fontWeight: 700, color: '#fff' }}>
          Hassan Uriostegui
        </Typography>
        <Box sx={{ display: { xs: 'none', md: 'flex' }, gap: 1 }}>
          {menuItems.map((item) => (
            <Button
              key={item.label}
              href={item.href}
              sx={{
                color: 'rgba(255, 255, 255, 0.8)',
                '&:hover': {
                  color: '#0071E3',
                  background: 'rgba(0, 113, 227, 0.1)',
                },
              }}
            >
              {item.label}
            </Button>
          ))}
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navigation;
