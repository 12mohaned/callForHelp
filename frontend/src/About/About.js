import Navbar from '../shared/Navbar';
import Footer from '../shared/Footer';
import React from 'react';
import './About.css';
class About extends React.Component{
  render(){
    return(
      <div className = 'Home'>
      <Navbar />
      <div className = 'Paragraph'>
      <h2>You're are never alone, here's some stories and advices</h2>
      </div>
      <div className = 'Footer'>
      <Footer />
      </div>
      </div>
    )
  }
}
export default About;
