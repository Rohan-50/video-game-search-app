import React from 'react';
import { AppBar, Toolbar, IconButton, Typography, Button, TextField } from '@mui/material';
import GamepadIcon from '@mui/icons-material/Gamepad';
import { createTheme, ThemeProvider } from '@mui/material/styles';

// Define a custom theme with the desired colors
const theme = createTheme({
  components: {
    MuiTextField: {
      styleOverrides: {
        root: {
          '& .MuiOutlinedInput-root': {
            '& fieldset': {
              borderColor: 'grey', // Change the outline color
            },
            '&:hover fieldset': {
              borderColor: 'darkgrey', // Change the outline color on hover
            },
          },
          '& .MuiInputLabel-root': {
            color: 'grey', // Change the label text color
          },
          '&:hover .MuiInputLabel-root': {
            color: 'darkgrey', // Change the label text color on hover
          },
          '& input': {
            color: 'white', // Change the text color
          },
        },
      },
    },
  },
});

const appButtonStyle = {
  margin: '0 10px',
  textTransform: 'none',
};

const MyAppBar = () => {
  return (
    <AppBar position="sticky" sx={{ color: 'grey', backgroundColor: '#000000' }}>
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

        <ThemeProvider theme={theme}>
          <TextField
            id="outlined-basic"
            label="Search"
            variant="outlined"
            size="small"
            sx={{ marginLeft: 2, width: '400px' }}
          />
        </ThemeProvider>
      </Toolbar>
    </AppBar>
  );
};

export default MyAppBar;
