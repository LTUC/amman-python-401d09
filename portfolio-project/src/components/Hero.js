import React from 'react'

function Hero() {
  return (
    <section className='hero'>
      <div className="hero-content">
        <div>
          <h2>Welcome I'm Waleed</h2>
          <h1>I design and <br /> build <span>websites</span></h1>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. <br /> Corrupti itaque quisquam laboriosam ipsam repudiandae eaque molestias <br /> cumque est vel eveniet veniam totam, vero minima</p>
        </div>

        <div className='hero-content-footer'>
          <a href="" className="btn btn-primary">My Work</a>
          <div className="hero-social-link">
            <a href=""><i class="fa-brands fa-facebook-f"></i></a>
            <a href=""><i class="fa-brands fa-twitter"></i></a>
            <a href=""><i class="fa-brands fa-instagram"></i></a>
            <a href=""><i class="fa-brands fa-linkedin"></i></a>
          </div>
        </div>
      </div>
      
    </section>
  )
}

export default Hero
