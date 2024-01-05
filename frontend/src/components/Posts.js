import React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';

const Posts = (props) => {
    const { posts } = props;

    if (!posts || posts.length === 0) {
        return <p>No posts found, sorry.</p>;
    }

    return (
        <Container maxWidth='md' component='main'>
            <Grid container spacing={5} alignItems='flex-end'>
                {posts.map((post) => (
                    <Grid item key={post.id} xs={12} sm={6} md={4}>
                        <Card sx={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
                            <CardMedia
                                sx={{ paddingTop: '56.25%' }}
                                image='https://source.unsplash.com/random'
                                title='image title'
                            />
                            <CardContent sx={{ flexGrow: 1 }}>
                                <Typography
                                    gutterBottom
                                    variant='h5'
                                    component='h2'
                                    sx={{ fontSize: '16px', textAlign: 'left' }}
                                >
                                    {post.title.substr(0, 50)}...
                                </Typography>
                                <div
                                    sx={{
                                        display: 'flex',
                                        justifyContent: 'left',
                                        alignItems: 'baseline',
                                        fontSize: '12px',
                                        textAlign: 'left',
                                        marginBottom: '2px',
                                    }}
                                >
                                    <Typography component='p' color='textPrimary'></Typography>
                                    <Typography variant='p' color='textSecondary'>
                                        {post.excerpt.substr(0, 60)}...
                                    </Typography>
                                </div>
                            </CardContent>
                        </Card>
                    </Grid>
                ))}
            </Grid>
        </Container>
    );
};

export default Posts;
