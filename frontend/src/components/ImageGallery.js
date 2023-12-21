import React from 'react';
import { Grid, Card, CardMedia } from '@mui/material';
import image1 from '../images/Nintendo_Icon.png';
import image2 from '../images/PlayStation_Icon.jpeg';
import image3 from '../images/Steam_Icon.jpeg';
import image4 from '../images/Xbox_Icon.png';

const ImageGallery = () => {
    const imageContainerStyle = {
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      marginBottom: '100px',
    };
  
    const galleryImageStyle = {
      width: 50,
      height: 'auto',
      margin: '0 10px',
      borderRadius: 8,
    };
  
    return (
      <Grid container spacing={0} style={imageContainerStyle}>
        <Grid item>
          <Card sx={{backgroundColor: 'black'}}>
            <CardMedia
              component="img"
              alt="Nintendo"
              image={image1}
              style={galleryImageStyle}
            />
          </Card>
        </Grid>
        <Grid item>
          <Card sx={{backgroundColor: 'black'}}>
            <CardMedia
              component="img"
              alt="Playstation"
              image={image2}
              style={galleryImageStyle}
            />
          </Card>
        </Grid>
        <Grid item>
          <Card sx={{backgroundColor: 'black'}}>
            <CardMedia
              component="img"
              alt="Steam"
              image={image3}
              style={galleryImageStyle}
            />
          </Card>
        </Grid>
        <Grid item>
          <Card sx={{backgroundColor: 'black'}}>
            <CardMedia
              component="img"
              alt="Xbox"
              image={image4}
              style={galleryImageStyle}
            />
          </Card>
        </Grid>
      </Grid>
    );
  };

export default ImageGallery;
