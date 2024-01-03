import React from 'react';

class connectionExample extends React.Component {
  apiUrl = 'http://localhost:8000/api';

  async componentDidMount() {
    try {
      const response = await fetch(this.apiUrl);
      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error);
    }
  }
  render() {
    return (
      <div>
        <h1>Connection Example</h1>
      </div>
    );
  }
}

export default connectionExample;