import React from 'react'
import aboutImage from '../assets/about.jpg';

function About() {
  return (
    <section className='about'>
      <section className='about-container'>
        <article className='about-info'>
          <p className='about-title'>A good updated website<br />counts in a world that's<br /><span>constantly online</span></p>
          <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officia quisquam quo dicta nesciunt aut iste distinctio reiciendis, fugiat velit aliquam expedita, maxime nemo mollitia eum sint rem necessitatibus quas ducimus!</p>
          <ul>
            <li>It looks more professional than your competition</li>
            <li>It looks more professional than your competition</li>
            <li>It looks more professional than your competition</li>
          </ul>
        </article>

        <article className='about-image'>
          <img src={aboutImage} alt="" />
          <div className='about-image-information'>
            <i class="fa-solid fa-earth-americas"></i>
            <div>
              <h3>Thound of Works</h3>
              <p>Trusted and fasted</p>
            </div>
          </div>
        </article>
      </section>

    </section>
  )
}

export default About
