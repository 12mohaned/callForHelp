import Navbar from '../shared/Navbar';
import Footer from '../shared/Footer';
import React from 'react';
import './Advice.css';
class Advice extends React.Component{
  render(){
    return(
      <div className = 'Home'>
      <Navbar />
      <div className = 'quotes'>
      <h2>These quotes can make all the difference </h2>
      <div class="card">
      <div class="container">
      <p>We must accept finite disappointment, but never lose infinite hope.</p>
      <h4><b>Martin Luther King, Jr</b></h4>
      </div>
      </div>
      <div class="card">
      <div class="container">
      <p>Most of the important things in the world have been accomplished by people
         who have kept on trying when there seemed to be no hope at all.</p>
      <h4><b>Dale Carnegie</b></h4>
      </div>
      </div>
      <div class="card">
      <div class="container">
      <p>However difficult life may seem, there is always something you can do and succeed at.</p>
      <h4><b>Stephen Hawking</b></h4>
      </div>
      </div>
      <div class="card">
      <div class="container">
      <p>But man is not made for defeat. A man can be destroyed but not defeated.</p>
      <h4><b>Ernest Hemingway</b></h4>
      </div>
      </div>
      </div>
      <Footer />
      </div>
    )
  }
}
export default Advice;
