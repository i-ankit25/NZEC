import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
     <h1>Video Streaming Demonstration</h1>
     <br/>
     <img id="bg" src="http://localhost:5000/video_feed" width="1200" height="900"></img>
    </div>
  );
}

export default App;
