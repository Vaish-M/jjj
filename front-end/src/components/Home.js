import React,{useState} from 'react';

import './Home.css';
import abp from './plots/acad_bar_plot.png';
import mobp from './plots/mock_bar_plot.png';
import apb from './plots/apt_bar_plot.png';
import cbp from './plots/cert_bar_plot.png';
import cobp from './plots/comm_bar_plot.png';

import fbp from './plots/fsd_bar_plot.png';
import ibp from './plots/intern_bar_plot.png';
import jbp from './plots/java_bar_plot.png';
import mbp from './plots/ml_bar_plot.png';
import pbp from './plots/pyth_bar_plot.png';

import dbs from './plots/dbnja_scatter_plot.png';
import jas from './plots/janpy_scatter_plot.png';


function Home(){
	const [isAcadImageVisible, setIsAcadImageVisible] = useState(false);

  const toggleAcadImageVisibility = () => {
    setIsAcadImageVisible(!isAcadImageVisible);
  };
  return (
    <div className='container'>
      <h1>Welcome to Placement Prediction</h1>
      <p>Find your future career path with our prediction system.</p>
      <p>Have a look on the dataset visualization of our students</p>

      <div id="content" className='center'>
      {/* <div className='mfp-3d'>
      <div className='mfp-content'>
            <img src={abp} className='mfp-with-anim' alt="Acad Bar Plot" style={{ display: isAcadImageVisible ? 'block' : 'none' }}/>
            <img src={mobp} className='mfp-with-anim' alt="Mock Bar Plot" onClick={toggleAcadImageVisibility}/>
           
            
          </div> */}
      <img src={abp}></img>
      <img src={mobp}></img>
      <img src={apb}></img>
      <img src={cobp}></img>
      
      <img src={fbp}></img>
      <img src={mbp}></img>
      <img src={pbp}></img>
      <img src={jbp}></img>
      <img src={cbp}></img>
      <img src={ibp}></img>

      <img src={dbs}></img>
      <img src={jas}></img>

      </div> 

      </div>
   
      
    
  );
}
export default Home;