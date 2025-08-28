"use-client";
import * as React from 'react';
import Box from '@mui/material/Box';
import Avatar from '@mui/material/Avatar';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Tooltip from '@mui/material/Tooltip';
// import Lightbulb from '@mui/icons-material/Lightbulb';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import FavoriteIcon from '@mui/icons-material/Favorite';
import Login from '@mui/icons-material/Login';
import Link from 'next/link';

export function DesktopAccountMenu() {
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl);
  const handleClick = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };

  //  // Estado do tema: "light" ou "dark"
  //   const [theme, setTheme] = React.useState<'light' | 'dark'>(() => {
  //     if (typeof window !== 'undefined') {
  //       const stored = localStorage.getItem('theme');
  //       if (stored === 'light' || stored === 'dark') return stored;
  //       return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  //     }
  //     return 'light';
  //   });
  
  //   // Função para alternar tema
  //   const toggleTheme = () => {
  //     const newTheme = theme === 'light' ? 'dark' : 'light';
  //     setTheme(newTheme);
  
  //     if (typeof window !== 'undefined') {
  //       localStorage.setItem('theme', newTheme);
  //       if (newTheme === 'dark') {
  //         document.documentElement.classList.add('dark');
  //       } else {
  //         document.documentElement.classList.remove('dark');
  //       }
  //     }
  //   };
  
  //   React.useEffect(() => {
  //     // Aplica a classe dark no carregamento
  //     if (theme === 'dark') {
  //       document.documentElement.classList.add('dark');
  //     } else {
  //       document.documentElement.classList.remove('dark');
  //     }
  //   }, [theme]);

  return (
    <React.Fragment>
      <Box sx={{ display: 'flex', alignItems: 'center', textAlign: 'center', gap: 0 }}>
        <Tooltip title="Carrinho">
          <Typography sx={{ minWidth: 100 }}><Link href='/cart'><ShoppingCartIcon /></Link></Typography>
        </Tooltip>
        <Tooltip title="Favoritos">
          <Typography sx={{ minWidth: 100 }}><Link href='/favorites'><FavoriteIcon /></Link></Typography>
        </Tooltip>
        <Tooltip title="Account settings">
          <IconButton
            onClick={handleClick}
            size="small"
            sx={{ ml: 2 }}
            aria-controls={open ? 'account-menu' : undefined}
            aria-haspopup="true"
            aria-expanded={open ? 'true' : undefined}
          >
            <Avatar sx={{ width: 32, height: 32}}></Avatar>
          </IconButton>
        </Tooltip>
      </Box>
      <Menu
        anchorEl={anchorEl}
        id="account-menu"
        open={open}
        onClose={handleClose}
        onClick={handleClose}
        slotProps={{
          paper: {
            elevation: 0,
            sx: {
              overflow: 'visible',
              filter: 'drop-shadow(0px 2px 8px rgba(0,0,0,0.32))',
              mt: 1.5,
              '& .MuiAvatar-root': {
                width: 32,
                height: 32,
                ml: -0.5,
                mr: 1,
              },
              '&::before': {
                content: '""',
                display: 'block',
                position: 'absolute',
                top: 0,
                right: 14,
                width: 10,
                height: 10,
                bgcolor: 'background.paper',
                transform: 'translateY(-50%) rotate(45deg)',
                zIndex: 0,
              },
            },
          },
        }}
        transformOrigin={{ horizontal: 'right', vertical: 'top' }}
        anchorOrigin={{ horizontal: 'right', vertical: 'bottom' }}
      >
        <MenuItem component={Link} href='/profile' onClick={handleClose}>
          <Avatar /> Profile
        </MenuItem>

        <Divider />

        {/* <MenuItem onClick={(e) => { e.stopPropagation(); toggleTheme(); }}>
          <ListItemIcon>
            <Lightbulb fontSize="small" color={theme === 'light' ? 'warning' : 'primary'} />
          </ListItemIcon>
          Tema {theme === 'light' ? 'Claro' : 'Escuro'}
        </MenuItem> */}

        <MenuItem component={Link} href='/login' onClick={handleClose}>
          <ListItemIcon>
            <Login fontSize="small" />
          </ListItemIcon>
          Login
        </MenuItem>
      </Menu>
    </React.Fragment>
  );
}
