import React, { Component } from 'react';
import './App.css';
import {Signin} from './Component/Signin.js'
import {Signup} from './Component/Signup.js'


function App() {
  return (
    <div className="App">
      
        Car Mechanic Near You
      {/* <Signin/>   */}
      <Signup/>
      
    </div>
  );
}

export default App;
