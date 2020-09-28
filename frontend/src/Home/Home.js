import Navbar from '../shared/Navbar';
import React from 'react';
import './Home.css';
class Home extends React.Component{
  render(){
    return(
      <div className = 'Home'>
      <Navbar />
      <div className = 'Paragraph'>
      <h2>Feel Like you wanna talk ?</h2>
      </div>
      <button class="button button4">Let's Chat</button>
      </div>
    )
  }
}
export default Home;
