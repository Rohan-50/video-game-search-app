import React from 'react';
import { Card, CardContent, CardMedia, Typography, Grid } from '@mui/material';
import GameCollageImage from '../images/Game_Collage.jpg'
import SearchFeatureImage from '../images/Search_Feature.png'
import GameListImage from '../images/Game_List.jpeg'

const cardData = [
    {
        id: 1,
        image: GameCollageImage,
        heading: 'ALL IN ONE PLACE',
        subheading: 'A large collection of video games',
        description: 'Access a full database of video games where you can filter \
        (platform, tags, publishers, genres) and sort (release date, A-Z, ratings) \
        the entire gaming catalog of over 9,000 games!',
    },
    {
        id: 2,
        image: SearchFeatureImage,
        heading: 'NEW SEARCH FEATURES',
        subheading: 'Use natural language to search',
        description: 'A new feature (still being tested) is available that allows you to \
        search for games using natural language. Now you can find that perfect game without \
        having to spend time playing with filters.',
    },
    {
        id: 3,
        image: GameListImage,
        heading: 'MANAGE MULTIPLE LISTS',
        subheading: 'Create lists for all your gaming needs',
        description: 'You can now create as many lists as you want to manage your gaming \
        backlog. Whether you have a list of games that you still need to play, or have a \
        list of favorites that you enjoy playing with friends, our lists can help with it all.',
    },
];

const CardGrid = () => {
    return (
        <Grid container spacing={10} justifyContent="center">
            {cardData.map((card) => (
                <Grid item key={card.id} sx={{ display: 'flex' }}>
                    <Card sx={{ marginBottom: '50px', width: '40vh', backgroundColor: '#151515' }}>
                        <CardMedia component="img" height="50%" width="50%" image={card.image} alt={card.heading} />
                        <CardContent>
                            <Typography variant="h5" sx={{ color: 'white', marginBottom: '30px' }}>
                                {card.heading}
                            </Typography>
                            <Typography variant="h6" sx={{ color: 'white', marginBottom: '30px' }}>
                                {card.subheading}
                            </Typography>
                            <Typography variant="body2" sx={{ color: 'white'}}>
                                {card.description}
                            </Typography>
                        </CardContent>
                    </Card>
                </Grid>
            ))}
        </Grid>
    );
};

export default CardGrid;
