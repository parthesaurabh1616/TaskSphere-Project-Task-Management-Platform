import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../../contexts/AuthContext';
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Box,
  IconButton,
  Menu,
  MenuItem
} from '@mui/material';
import {
  Dashboard as DashboardIcon,
  Assignment as ProjectIcon,
  Task as TaskIcon,
  Person as PersonIcon,
  Logout as LogoutIcon
} from '@mui/icons-material';

const Navbar = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [anchorEl, setAnchorEl] = React.useState(null);

  const handleMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  const handleLogout = () => {
    logout();
    navigate('/login');
    handleMenuClose();
  };

  const handleProfile = () => {
    navigate('/profile');
    handleMenuClose();
  };

  const isActive = (path) => {
    return location.pathname === path;
  };

  if (!user) {
    return null;
  }

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          TaskSphere
        </Typography>
        
        <Box sx={{ display: 'flex', gap: 1 }}>
          <Button
            color="inherit"
            startIcon={<DashboardIcon />}
            onClick={() => navigate('/dashboard')}
            sx={{ 
              backgroundColor: isActive('/dashboard') ? 'rgba(255,255,255,0.1)' : 'transparent'
            }}
          >
            Dashboard
          </Button>
          
          <Button
            color="inherit"
            startIcon={<ProjectIcon />}
            onClick={() => navigate('/projects')}
            sx={{ 
              backgroundColor: isActive('/projects') ? 'rgba(255,255,255,0.1)' : 'transparent'
            }}
          >
            Projects
          </Button>
          
          <Button
            color="inherit"
            startIcon={<TaskIcon />}
            onClick={() => navigate('/tasks')}
            sx={{ 
              backgroundColor: isActive('/tasks') ? 'rgba(255,255,255,0.1)' : 'transparent'
            }}
          >
            Tasks
          </Button>
          
          <IconButton
            color="inherit"
            onClick={handleMenuOpen}
            aria-label="account menu"
          >
            <PersonIcon />
          </IconButton>
          
          <Menu
            anchorEl={anchorEl}
            open={Boolean(anchorEl)}
            onClose={handleMenuClose}
          >
            <MenuItem onClick={handleProfile}>
              <PersonIcon sx={{ mr: 1 }} />
              Profile
            </MenuItem>
            <MenuItem onClick={handleLogout}>
              <LogoutIcon sx={{ mr: 1 }} />
              Logout
            </MenuItem>
          </Menu>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
