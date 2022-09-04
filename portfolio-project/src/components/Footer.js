import React from 'react'
import logo from '../assets/logo.png';

function Footer() {
  return (
    <footer>
      <section className="inner-footer">
        <div className="top-footer">
          <div className="footer-contact">
            <h3>Contact</h3>
            <p>Let's connect and get<br />your problem <span>solved with code.</span></p>
            <div>
              <a href="" className="btn btn-primary">Contact Us</a>
            </div>
          </div>

          <div className="footer-contact-info">
            <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Blanditiis unde placeat deserunt ut natus laudantium. Temporibus sunt, ducimus reiciendis fugit nulla expedita similique unde iste magnam enim odit incidunt nobis?</p>
            <p><i class="fa-sharp fa-solid fa-location-dot"></i> Plaestine, Gaza</p>
            <p><i class="fa-solid fa-envelope"></i> info@waleedafifi.me</p>
            <p><i class="fa-solid fa-phone"></i> +972 599 950093</p>
          </div>
        </div>
        <div className='bottom-footer'>
          <div className="footer-logo">
            <img src={logo} alt="" />
          </div>
          <nav className="footer-social-link">
            <a href=""><i class="fa-brands fa-facebook-f"></i></a>
            <a href=""><i class="fa-brands fa-twitter"></i></a>
            <a href=""><i class="fa-brands fa-instagram"></i></a>
            <a href=""><i class="fa-brands fa-linkedin"></i></a>
          </nav>
        </div>
      </section>
    </footer>
  )
}

export default Footer
