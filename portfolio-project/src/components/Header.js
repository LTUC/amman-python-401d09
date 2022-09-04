import React from 'react'
import logo from '../assets/logo.png';

function Header() {
  return (
    <header>
      <div className="header-logo">
        <img src={logo} alt="" srcset="" />
      </div>

      <nav className="header-nav">
        <a href="">Home</a>
        <a href="">services</a>
        <a href="">portfolio</a>
        <a href="">about</a>
        <a className='btn btn-primary' href="">contact</a>
      </nav>
    </header>
  )
}

export default Header
