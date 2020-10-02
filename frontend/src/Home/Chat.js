import Navbar from '../shared/Navbar';
import Footer from '../shared/Footer';
import React from 'react';
import './Chat.css';
class Chat extends React.Component{
  render(){
    return(
      <div className = 'Chat'>
      <Navbar />
      <div className = 'Paragraph'>
      <h2>This is private and no one is going to see it since it</h2>
      </div>
      <input type = "textarea" id = "MessageForm" name = "MessageForm"/>
      <button id = "MessageForm" type="submit" class="btn btn-primary black">Save</button>
      <div className = 'Footer'>
      <Footer />
      </div>
      </div>
    )
  }
}
export default Chat;
