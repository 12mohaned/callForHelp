import React from 'react';
import ReactDOM from 'react-dom';
import {Router, Route} from "react-router";
import './index.css';
import Navbar from './shared/Navbar';
import Home from './Home/Home';
import Advice from './Advice/Advice';
import About  from './About/About';
import * as serviceWorker from './serviceWorker';
ReactDOM.render(
  <React.StrictMode>
    <Navbar />
    <Router>
   <Route path = "/" component = {Navbar}>
      <Route path = "home" component = {Home} />
      <Route path = "advice" component = {Advice} />
      <Route path = "about" component = {About} />
   </Route>
</Router>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
