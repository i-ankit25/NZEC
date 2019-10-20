import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
     <h1 style = {{'font-family': 'Lobster, cursive', 'fontSize': '40px'}}>Video Streaming Demonstration !!</h1>
     <h2 style = {{'fontSize':'30px'}}>Find your loved ones, anytime, anywhere !!</h2>
     <img style={{'border': '1px solid',
    'padding': '10px',
    'box-shadow' : '7px 12px 10px #888888'}} id="bg" src="http://10.42.0.186:5000/video_feed" width="800" height="600"></img>
    </div>
  );
}

export default App;
