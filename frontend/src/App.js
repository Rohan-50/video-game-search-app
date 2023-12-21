import React, { useState, useEffect } from 'react';
import './App.css';
import CardGrid from './components/CardGrid';
import Navbar from './components/Navbar';
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';
import Typography from '@mui/material/Typography';
import GamepadRoundedIcon from '@mui/icons-material/GamepadRounded';
import { AppBar, IconButton } from '@mui/material';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('/api')
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  return (
    <div className="App">
        <Navbar/>
      <div>
        <Typography variant="h4" style={{ marginTop: "200px" }}>
          Your guide for finding the perfect game
        </Typography>
      </div>
      
    </div>
  );
}

export default App;
