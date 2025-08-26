"use-client";
import * as React from 'react';
import Box from '@mui/material/Box';
import Avatar from '@mui/material/Avatar';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import Home from '@mui/icons-material/Home';
import Settings from '@mui/icons-material/Settings';
import Logout from '@mui/icons-material/Logout';
import Lightbulb from '@mui/icons-material/Lightbulb';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import FavoriteIcon from '@mui/icons-material/Favorite';
import AccountBalance from '@mui/icons-material/AccountBalance';
import AddShoppingCart from '@mui/icons-material/AddShoppingCart';
import SettingsPhone from '@mui/icons-material/SettingsPhone';
import Link from 'next/link';

export function MobileAccountMenu() {
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl);
  const handleClick = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };
  return (
    <React.Fragment>
      <Box sx={{ display: 'flex', alignItems: 'center', textAlign: 'center' }}>
          <IconButton
            onClick={handleClick}
            size="small"
            aria-controls={open ? 'account-menu' : undefined}
            aria-haspopup="true"
            aria-expanded={open ? 'true' : undefined}
          >
            <Avatar sx={{ width: 32, height: 32 }}></Avatar>
          </IconButton>
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
        <MenuItem component={Link} href='/' onClick={handleClose}>
          <ListItemIcon>
            <Home fontSize="small" />
          </ListItemIcon>
          Home
        </MenuItem>
        <MenuItem component={Link} href='/catalog' onClick={handleClose}>
          <ListItemIcon>
            <AddShoppingCart fontSize="small" />
          </ListItemIcon>
          Catálogo
        </MenuItem>
        <MenuItem component={Link} href='/about' onClick={handleClose}>
          <ListItemIcon>
            <AccountBalance fontSize="small" />
          </ListItemIcon>
          Sobre Nós
        </MenuItem>
        <MenuItem component={Link} href='/faq' onClick={handleClose}>
          <ListItemIcon>
            <Lightbulb fontSize="small" />
          </ListItemIcon>
          FAQ
        </MenuItem>
        <MenuItem component={Link} href='/contact' onClick={handleClose}>
          <ListItemIcon>
            <SettingsPhone fontSize="small" />
          </ListItemIcon>
          Contato
        </MenuItem>
        <MenuItem component={Link} href='/cart' onClick={handleClose}>
          <ListItemIcon>
            <ShoppingCartIcon fontSize="small" />
          </ListItemIcon>
          Carrinho
        </MenuItem>
        <MenuItem component={Link} href='/favorites' onClick={handleClose}>
          <ListItemIcon>
            <FavoriteIcon fontSize="small" />
          </ListItemIcon>
          Favoritos
        </MenuItem>
        <Divider />
        <MenuItem component={Link} href='/settings' onClick={handleClose}>
          <ListItemIcon>
            <Settings fontSize="small" />
          </ListItemIcon>
          Settings
        </MenuItem>
        <MenuItem component={Link} href='/logout' onClick={handleClose}>
          <ListItemIcon>
            <Logout fontSize="small" />
          </ListItemIcon>
          Logout
        </MenuItem>
      </Menu>
    </React.Fragment>
  );
}
