import React from 'react';
import { Card, CardContent, CardMedia, Typography } from '@mui/material';

const GameCard = ({ image, name, rating, reviewsCount }) => {
  return (
    <Card>
      <CardMedia
        component="img"
        height="140"
        image={image}
        alt={name}
      />
      <CardContent>
        <Typography variant="h6">{name}</Typography>
        <Typography variant="body2">Rating: {rating} ({reviewsCount} reviews)</Typography>
      </CardContent>
    </Card>
  );
};

export default GameCard;
