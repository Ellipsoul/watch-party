import React, { ReactElement } from 'react';
import './App.css';
import { BrowserRouter as Router } from "react-router-dom";
import Home from './Home'

function App():ReactElement {

  console.log("Front-end is now running!")

	return (
    
		<>
			<Router>
        <Home />
			</Router>
		</>
	);
}

export default App;
