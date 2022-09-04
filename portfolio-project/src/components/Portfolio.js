import React from 'react'

function Portfolio() {
  return (
    <section className='portfolio'>
      <section className='inner-portfolio'>
        <div className="section-header">
          <h3>My Projects</h3>
          <h2>My <span>Portfolio</span></h2>
        </div>

        <div className="portfolio-filter">
          <ul className="filter">
            <li className="filter-nav-item">All</li>
            <li className="filter-nav-item">Education</li>
            <li className="filter-nav-item">Company</li>
            <li className="filter-nav-item">Personal</li>
            <li className="filter-nav-item">Dashboard</li>
            <li className="filter-nav-item">Tavel</li>
          </ul>

          <div className="protfolio-container">
            <div className="porto-item">
              <img src="https://cdn.dribbble.com/users/554465/screenshots/14479806/media/a79261628856eab13c6a477d878a6b7b.png?compress=1&resize=400x300" alt="" />
              <div className='porto-hidden-content'>
                <h3>Sample Project</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium cum</p>
                <div>
                  <a href='#' className="btn btn-primary">See Project</a>
                </div>
              </div>
            </div>

            <div className="porto-item">
              <img src="https://cdn.dribbble.com/users/554465/screenshots/14479806/media/a79261628856eab13c6a477d878a6b7b.png?compress=1&resize=400x300" alt="" />
              <div className='porto-hidden-content'>
                <h3>Sample Project</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium cum</p>
                <div>
                  <a href='#' className="btn btn-primary">See Project</a>
                </div>
              </div>
            </div>

            <div className="porto-item">
              <img src="https://cdn.dribbble.com/users/554465/screenshots/14479806/media/a79261628856eab13c6a477d878a6b7b.png?compress=1&resize=400x300" alt="" />
              <div className='porto-hidden-content'>
                <h3>Sample Project</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium cum</p>
                <div>
                  <a href='#' className="btn btn-primary">See Project</a>
                </div>
              </div>
            </div>

            <div className="porto-item">
              <img src="https://cdn.dribbble.com/users/554465/screenshots/14479806/media/a79261628856eab13c6a477d878a6b7b.png?compress=1&resize=400x300" alt="" />
              <div className='porto-hidden-content'>
                <h3>Sample Project</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium cum</p>
                <div>
                  <a href='#' className="btn btn-primary">See Project</a>
                </div>
              </div>
            </div>

            <div className="porto-item">
              <img src="https://cdn.dribbble.com/users/554465/screenshots/14479806/media/a79261628856eab13c6a477d878a6b7b.png?compress=1&resize=400x300" alt="" />
              <div className='porto-hidden-content'>
                <h3>Sample Project</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium cum</p>
                <div>
                  <a href='#' className="btn btn-primary">See Project</a>
                </div>
              </div>
            </div>

            <div className="porto-item">
              <img src="https://cdn.dribbble.com/users/554465/screenshots/14479806/media/a79261628856eab13c6a477d878a6b7b.png?compress=1&resize=400x300" alt="" />
              <div className='porto-hidden-content'>
                <h3>Sample Project</h3>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium cum</p>
                <div>
                  <a href='#' className="btn btn-primary">See Project</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

    </section>
  )
}

export default Portfolio
