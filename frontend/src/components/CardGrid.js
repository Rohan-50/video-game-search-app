import React from 'react';
import { Card, CardContent, CardMedia, Typography, Grid } from '@mui/material';

const cardData = [
  {
    id: 1,
    image: 'image1.jpg', // Replace with actual image URL
    heading: 'Card 1 Heading',
    subheading: 'Card 1 Subheading',
    description: 'Description for Card 1.',
  },
  {
    id: 2,
    image: 'image2.jpg', // Replace with actual image URL
    heading: 'Card 2 Heading',
    subheading: 'Card 2 Subheading',
    description: 'Description for Card 2.',
  },
  {
    id: 3,
    image: 'image3.jpg', // Replace with actual image URL
    heading: 'Card 3 Heading',
    subheading: 'Card 3 Subheading',
    description: 'Description for Card 3.',
  },
];

const CardGrid = () => {
  return (
    <Grid container spacing={30} justifyContent="center">
      {cardData.map((card) => (
        <Grid item key={card.id} sx={{display: 'flex'}}>
          <Card style={{ width: '240px', height: '540px' }}>
            <CardMedia component="img" height="140" image={card.image} alt={card.heading} />
            <CardContent>
              <Typography variant="h6">{card.heading}</Typography>
              <Typography variant="subtitle1" color="textSecondary">{card.subheading}</Typography>
              <Typography variant="body2">{card.description}</Typography>
            </CardContent>
          </Card>
        </Grid>
      ))}
    </Grid>
  );
};

export default CardGrid;
