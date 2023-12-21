// src/components/CardGrid.js
import React from 'react';
import { Card, CardContent, CardMedia, Grid, Pagination, Typography } from '@mui/material';

const itemsPerPage = 4;

const data = [
  { id: 1, title: 'Item 1', imageUrl: 'https://via.placeholder.com/150' },
  { id: 2, title: 'Item 2', imageUrl: 'https://via.placeholder.com/150' },
  { id: 3, title: 'Item 3', imageUrl: 'https://via.placeholder.com/150' },
  // Add more items as needed
];

const CardGrid = () => {
  const [page, setPage] = React.useState(1);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const startIndex = (page - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const displayedItems = data.slice(startIndex, endIndex);

  return (
    <div>
      <Grid container spacing={3}>
        {displayedItems.map(item => (
          <Grid item key={item.id} xs={12} sm={6} md={4} lg={3}>
            <Card>
              <CardMedia component="img" height="140" image={item.imageUrl} alt={item.title} />
              <CardContent>
                <Typography variant="h6">{item.title}</Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
      <Pagination
        count={Math.ceil(data.length / itemsPerPage)}
        page={page}
        onChange={handleChangePage}
        color="primary"
        style={{ marginTop: '20px' }}
      />
    </div>
  );
};

export default CardGrid;
