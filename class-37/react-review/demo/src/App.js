import './App.css';
import React, { Suspense, Profiler } from 'react';
import { Routes, Route } from "react-router-dom";

import Header from './components/Header';
// import Form from './components/Form'; // this is wohout lazy loading
const Form = React.lazy(() => import('./components/Form'));


function App() {

  console.log("App is rendering");
  return (
    <>
      <Routes>
        <Route path="/" element={<Header />} />
        <Route path="form" element={
          <Suspense>
            <Form />
          </Suspense>
        } />
      </Routes>


      <p>Reviewing React</p>

      <Profiler
        id="formProfiler"
        onRender={(id, phase, time) => {
          console.log(id, phase, time)
        }}
      >

      </Profiler>
    </>
  )
}

export default App;