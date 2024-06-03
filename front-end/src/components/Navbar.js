import React from 'react';
import './Navbar.css'; // Create this CSS file for styling
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHouse, faUser, faCircleInfo, faRightFromBracket } from '@fortawesome/free-solid-svg-icons';
import { NavLink, useNavigate } from 'react-router-dom';

const Navbar = () => {
    const navigate = useNavigate();

    const handleLogout = (e) => {
        navigate('/');
    }

    return (
        <div className="vertical-navbar">
            <div className="vertical-navbar-brand">
                <NavLink className="navbar-logo navlink-custom" exact>
                <div class="logo-text"> 
                <div class="anim-letter-1">P</div>
                <div class="anim-letter-2">l</div>
                <div class="anim-letter-3">a</div>
                <div class="anim-letter-4">c</div>
                <div class="anim-letter-5">e</div>
                <div class="anim-letter-6">m</div>
                <div class="anim-letter-7">e</div>
                <div class="anim-letter-8">n</div>
                <div class="anim-letter-9">t</div>
                <div class="anim-letter-10"> </div>
                <div class="anim-letter-11">P</div>
                <div class="anim-letter-12">r</div>
                <div class="anim-letter-13">e</div>
                <div class="anim-letter-14">d</div>

                </div>
</NavLink>
            </div>

            <ul className="vertical-navbar-nav">
                <li className="nav-button">
                    <NavLink className="nav-link" to="/user/home" exact>
                        <FontAwesomeIcon icon={faHouse} />
                        Home
                    </NavLink>
                </li>

                <li className="nav-button">
                    <NavLink className="nav-link" to="/user/details" exact>
                        <FontAwesomeIcon icon={faCircleInfo} />
                        Details
                    </NavLink>
                </li>

                <li className="nav-button">
                    <NavLink className="nav-link" to="/user/about" exact>
                        <FontAwesomeIcon icon={faUser} />
                        About Us
                    </NavLink>
                </li>

                <li className="nav-button">
                <button onClick={handleLogout} style={{ backgroundColor: 'transparent', border: 'none', fontFamily:'Cardo' }}>
                    <FontAwesomeIcon icon={faRightFromBracket} rotation={180} />
                    Logout
                </button>

                </li>
            </ul>
        </div>
    )
}

export default Navbar;
