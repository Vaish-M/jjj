import React from "react";
import {BrowserRouter as Router,Routes, Route } from "react-router-dom";
import Home from "./Home";
import Details,{ResultRouter} from "./Details";
import Navbar from "./Navbar";
import About from "./About";
export default function UserRouting(){
    return(
        
        <>
        <Navbar />
            <Routes>
                <Route path="/home" element={<Home />}></Route>
                <Route path="/details" element={<ResultRouter />}></Route>
                <Route path="/about" element={<About/>}></Route>
               
            </Routes>
        </>
    )
}