import React, { useState,useEffect} from "react";
import './Otp.css';
import {useNavigate} from 'react-router-dom';
import axios from "axios";

function Otp(){
    const [otp, setOtp] = useState("");
    const [gotp, setgOtp] = useState("");
    const navigate=useNavigate()
    useEffect(()=>{
		axios.get('http://127.0.0.1:5000/otp').then((response)=>{
		  console.log(response.data);
		  setgOtp(response.data)
		  
		})
	  })

    const handleOtpChange = (e, index) => {
        let value = e.target.value;
        let newOtp = otp.split('');
        newOtp[index] = value;
        setOtp(newOtp.join(''));
        if(index===5){ console.log(otp);}
        else{
        if (value !== '' && e.target.nextSibling) {
            e.target.nextSibling.focus();
            console.log('heee')
        }
    }
    }

    const check = (e) =>{
        
        console.log("Submit button clicked");
        console.log(otp);
        if(otp===gotp){
          alert('Account Created Successfully')  
          navigate('/')
        }
        else{
          alert('Invalid OTP')
        }

    }
    
    return(
        <div className="body">
            <div className="box-form">
    <div className="left">
      <div className="overlay">
      <h1>Final Steps</h1>
   
      <span>
        <div className="inputs">
        </div>
      </span>
      </div>
    </div>
    
    
      <div className="right">

        <div className="container">
            <header>
              <i className="bx bxs-check-shield"></i>
            </header>
            <h3>Enter OTP</h3>
            <form onSubmit={check}>
              <div className="input-field">
              <input type="number" min="0" max="9" maxLength="1" onChange={(e) => handleOtpChange(e, 0)} value={otp[0] || ''} required/>
                <input type="number" min="0" max="9" maxLength="1" onChange={(e) => handleOtpChange(e, 1)} value={otp[1] || ''} required/>
                <input type="number" min="0" max="9" maxLength="1" onChange={(e) => handleOtpChange(e, 2)} value={otp[2] || ''} required/>
                <input type="number" min="0" max="9" maxLength="1" onChange={(e) => handleOtpChange(e, 3)} value={otp[3] || ''} required/>
                <input type="number" min="0" max="9" maxLength="1" onChange={(e) => handleOtpChange(e, 4)} value={otp[4] || ''} required/>
                <input type="number" min="0" max="9" maxLength="1" onChange={(e) => handleOtpChange(e, 5)} value={otp[5] || ''} required/>

              </div>
              <div><button style={{marginTop:'30px'}} type="submit" >Verify</button></div>
            </form>
          </div>

      </div>
    
  </div>

        </div>
    )
}
export default Otp;