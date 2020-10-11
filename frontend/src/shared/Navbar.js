import React from 'react';
import './Navbar.css';
import {
  BrowserRouter as Router,
  Link
} from "react-router-dom";
class Navbar extends React.Component{
  render(){
  return (
    <Router>
    <div className = 'Navbar'>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <ul>
      <li> <Link to = "/"><a>Home</a></Link></li>
      <li> <Link to = "/Advice"><a>Advice</a></Link></li>
      <li> <Link to = "/Visual"><a>Visual Data</a></Link></li>
      <li> <Link to = "/About"><a>About</a></Link></li>
    </ul>
    {this.props.children}

</nav>
    </div>
    </Router>
  )
}
}
export default Navbar;
