import React, { useEffect, useState } from 'react';
import { Typography, Container, Grid, Select, MenuItem } from '@mui/material';
import Navbar from '../components/Navbar';
import GameCard from '../components/GameCard';

const GamesPage = () => {
  const [games, setGames] = useState([]);

  useEffect(() => {
    fetch('/api/games')
      .then(response => response.json())
      .then(data => {
        console.log('API Response:', data);
        setGames(data.games);
      })
      .catch(error => console.error('Error fetching games data:', error));
  }, []);
  

  return (
    <div style={{ backgroundColor: 'black', color: 'white' }}>
      <Navbar />
      <Container sx={{ marginTop: '20px' }}>
        <Typography variant="h5" gutterBottom>
          What can you view on JustPlay?
        </Typography>
        <Typography variant="body1" paragraph>
          This is a placeholder for the content that describes what users can view on JustPlay.
        </Typography>
        {/* Filter dropdowns */}
        <Grid container spacing={2} sx={{ marginBottom: '20px' }}>
          {/* Add your filter dropdowns here */}
          {/* Example: */}
          <Grid item>
            <Select defaultValue="" variant="outlined" displayEmpty>
              <MenuItem value="" disabled>
                Platforms
              </MenuItem>
              {/* Add platform options here */}
            </Select>
          </Grid>
          {/* Add more filter dropdowns as needed */}
        </Grid>

        {/* Number of games placeholder */}
        <Typography variant="body1" sx={{ marginBottom: '10px' }}>
          {games.length} games
        </Typography>

        {/* Sorting dropdown */}
        <Typography variant="body1" sx={{ display: 'inline', marginRight: '10px' }}>
          Sorted by:
        </Typography>
        <Select defaultValue="reviewCount" variant="outlined" displayEmpty>
          <MenuItem value="reviewCount">Review count</MenuItem>
          {/* Add more sorting options as needed */}
        </Select>

        {/* Game cards */}
        <Grid container spacing={2}>
          {games.map((game) => (
            <Grid item key={game.id} xs={12} sm={6} md={4} lg={3} xl={2}>
              <GameCard
                image={game.background_image}
                name={game.name}
                rating={game.rating}
                reviewsCount={game.reviews_count}
              />
            </Grid>
          ))}
        </Grid>
      </Container>
    </div>
  );
};

export default GamesPage;
