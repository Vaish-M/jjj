import React from 'react';
import './About.css'; // Create this CSS file for styling
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {faEnvelope, faPhone, faLocation, faPeopleGroup} from '@fortawesome/free-solid-svg-icons';
import harsh from './images/harsh.jpeg'
import dd from './images/dhivya.jpeg'
import abbi from './images/abbi.jpeg'

const About = () => {
  return (
    <div className="about-us-container">
      <div className="about-us-content">
        <h1>About Us - Placement Prediction</h1><br></br>
        <p>
          Welcome to Placement Prediction, your trusted platform for predicting and optimizing
          placement opportunities. Our mission is to provide accurate placement predictions and help students and employers make informed decisions.
        </p>
        <p>
          At Placement Prediction, we believe in the power of data and technology to streamline the placement process. Our team of experts is dedicated to ensuring that your placement journey is as smooth and successful as possible.
        </p>
      </div>
      <div className="developers">
      <br></br>
        <h2>Meet Our Team <FontAwesomeIcon icon={faPeopleGroup} /></h2><br></br>
        <div className="developer-tiles">
          
            <div className="developer-tile">
              <img src={harsh} alt="harsh" width="50px" />
              <h3>Harshithaa MS</h3>
              <p>Front End Developer</p>
              <p> Creates user interfaces and client-side functionality for websites and applications.</p>
            </div>

            <div className="developer-tile">
              <img src={abbi} alt="harsh" width="50px" />
              <h3>Abbijananee M</h3>
              <p>Back End Developer</p>
              <p>Develops database systems to support the functionality of websites and applications.</p>
            </div>

            <div className="developer-tile">
              <img src={dd} alt="harsh" width="50px" />
              <h3>Dhiya Dharshini G
              </h3>
              <p>PowerBi </p>
              <p>Specializes in designing and implementing data visualizations, dashboards, and reports</p>
            </div>
          
        </div>
      </div>
      <div><br></br>
      <div className="contact-us-container">
      <div className="contact-details">
        <h2>Contact Us</h2>
        <div className="contact-icons">
          <p><FontAwesomeIcon icon={faEnvelope} /> Email: it.sonatech.ac.in</p>
          <p><FontAwesomeIcon icon={faPhone} /> Phone: +91 427 4099999</p>
          <p><FontAwesomeIcon icon={faLocation} /> Address: Junction Main Road, Salem.</p>
        </div>
      </div>
    </div>
    </div>
    </div>
  );
};

export default About;
