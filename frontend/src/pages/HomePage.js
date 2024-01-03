import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Stack, Button, Typography } from '@mui/material';
import Navbar from '../components/Navbar';
import ImageGallery from '../components/ImageGallery';
import CardGrid from '../components/CardGrid';
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

const HomePage = () => {
    const navigate = useNavigate();

    const handleDiscoverGamesClick = () => {
        navigate('/games');
    };

    const buttonStyle = {
        height: '50px',
        textTransform: 'none',
    };

    return (
        <div style={{ textAlign: 'center', backgroundColor: 'black', color: 'white' }}>
            <Navbar />
            <Typography variant="h3" sx={{ marginTop: '200px', marginBottom: '50px', fontWeight: '600' }}>
                Your guide for finding the perfect game
            </Typography>
            <Stack direction="row" spacing={2} sx={{ justifyContent: 'center', marginBottom: '200px' }}>
                <Button variant="contained" color="success" size="large" style={buttonStyle} onClick={handleDiscoverGamesClick}>
                    Discover Games
                </Button>
                <Button variant="outlined" size="large" style={buttonStyle}>
                    Search Feature
                </Button>
            </Stack>
            <Typography variant="h6" sx={{ color: 'gray', marginBottom: '20px' }}>
                Platforms available on JustPlay
            </Typography>
            <ImageGallery />
            <CardGrid />
        </div>
    );
};

export default HomePage;
