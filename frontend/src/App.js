import React, { useState, useEffect } from 'react';
import './App.css';
import CardGrid from './components/CardGrid';
import Navbar from './components/Navbar';
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';
import { Stack, Button, Typography } from '@mui/material';

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
      <Navbar />
      <div>
        <Typography variant="h3" style={{ marginTop: "200px", marginBottom: "50px", fontWeight: "600" }}>
          Your guide for finding the perfect game
        </Typography>
        <Stack direction="row" spacing={2} sx={{ justifyContent: 'center', marginBottom: '200px' }}>
          <Button variant="contained" color='success' size='large' sx={{ height: '50px' }}>
            Discover Popular Games
          </Button>
          <Button variant="outlined" size='large' sx={{ height: '50px' }}>
            Search Feature
          </Button>
        </Stack>
      </div>
    </div>
  );
}

export default App;
