import React from 'react'

function Skill() {
  return (
    <section className='skills'>
      <section className="inner-skill">
        <div className="section-header">
          <h3>My Skill</h3>
          <h2>I Develop <span>Skills</span> Regularly</h2>
        </div>

        <div className="skill-container">
          <div className="skill">
            <div className="skill-name">
              <i class="fa-brands fa-html5"></i>
              HTML
            </div>
            <div className="skill-bar">
              <div className="skill-per" per="90%" style={{maxWidth: '90%'}}></div>
            </div>
          </div>

          <div className="skill">
            <div className="skill-name">
            <i class="fa-brands fa-css3-alt"></i>
              CSS
            </div>
            <div className="skill-bar">
              <div className="skill-per" per="75%" style={{maxWidth: '75%'}}></div>
            </div>
          </div>

          <div className="skill">
            <div className="skill-name">
              <i class="fa-brands fa-html5"></i>
              HTML
            </div>
            <div className="skill-bar">
              <div className="skill-per" per="60%" style={{maxWidth: '60%'}}></div>
            </div>
          </div>
        </div>
      </section>

    </section>
  )
}

export default Skill
