import React from 'react';
import { AppBar, Toolbar, IconButton, Typography, Button, TextField } from '@mui/material';
import GamepadIcon from '@mui/icons-material/Gamepad';

const appButtonStyle = {
  margin: '0 10px',
  textTransform: 'none',
};

const MyAppBar = () => {
  return (
    <AppBar position="static" color='info'>
      <Toolbar>
        {/* Gamepad Icon Logo and Title */}
        <IconButton edge="start" color="inherit" aria-label="gamepad">
          <GamepadIcon />
        </IconButton>
        <Typography variant="h4" component="div" sx={{ flexGrow: 1, textAlign: 'left' }}>
          JustPlay
        </Typography>

        {/* Text Buttons */}
        <Button color="inherit" style={appButtonStyle}>
          New Games
        </Button>
        <Button color="inherit" style={appButtonStyle}>
          Most Popular
        </Button>
        <Button color="inherit" style={appButtonStyle}>
          Top Rated
        </Button>

        {/* Search Bar */}
        <TextField
          id="outlined-basic"
          label="Search"
          variant="outlined"
          size="small"
          sx={{ marginLeft: 2, width: '400px' }}
        />
      </Toolbar>
    </AppBar>
  );
};

export default MyAppBar;
