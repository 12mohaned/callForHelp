import Navbar from '../shared/Navbar';
import Footer from '../shared/Footer';
import React from 'react';
import './Home.css';
class Visuals extends React.Component{
  render(){
    return(
      <div className = 'Home'>
      <Navbar />

      <Footer />
      </div>
    )
  }
}
export default Home;
