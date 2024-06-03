import {BrowserRouter as Router,Routes, Route } from "react-router-dom";
import './App.css';
import Register,{RegisterRouter} from "./components/Register";
import Login from "./components/Login";
import Otp from "./components/Otp";

import Navbar from './components/Navbar';
import UserRouting from "./components/UserRouting";

function App() {
  return (
    <>
        {
        <Router>
          <Routes>
          <Route path="/" exact element={<Login />} />
          <Route path="/register" element={<RegisterRouter />} />
          <Route path="/otp" element={<Otp />} />
          <Route path="/user/*" element={<UserRouting />} />
          </Routes>
        </Router>


        }
      </>
  );
}

export default App;
