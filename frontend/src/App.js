import React from 'react';
import './App.css';
import Posts from './components/Posts';
import PostLoadingComponent from './components/PostLoading';

function App() {
  const PostLoading = PostLoadingComponent(Posts);
  const [appState, setAppState] = React.useState({
    loading : false,
    posts : null,
  });
  React.useEffect(() => {
    setAppState({ loading : true });
    fetch('http://localhost:8000/api')
      .then(response => response.json())
      .then(posts => {
        setAppState({loading : false, posts : posts});
      })
  }, [setAppState]);
  return (
    <div className="App">
      <h1>Latest Posts</h1>
      <PostLoading isLoading={appState.loading} posts={appState.posts} />
    </div>
  );
}

export default App;