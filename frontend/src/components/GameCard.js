import React from 'react';
import { Card, CardContent, CardMedia, Typography } from '@mui/material';

const GameCard = () => {
  return (
    <Card>
      <CardMedia
        component="img"
        height="140"
        image="/path/to/placeholder-image.jpg"
        alt="Game Placeholder"
      />
      <CardContent>
        <Typography variant="h6">Game Title Placeholder</Typography>
        <Typography variant="body2">Rating: 4.5 (2.7K)</Typography>
        {/* Add more content placeholders as needed */}
      </CardContent>
    </Card>
  );
};

export default GameCard;
