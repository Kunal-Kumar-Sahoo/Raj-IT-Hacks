import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useNavigate } from 'react';
// import { NavBar } from "./components/NavBar";
// import { Banner } from "./components/Banner";
// import { Startup } from "./components/Startup";
// import { Projects } from "./components/Projects";
// import { Contact } from "./components/Contact";
// import { Footer } from "./components/Footer";
// import { Investors } from './Investors';
import { Link } from 'react-router-dom';
import Login from './components/Login';
import Layout from './Layout';
import { Navbar } from 'react-bootstrap';
import { Startup } from './components/Startup';
import { Routes, Route, BrowserRouter } from 'react-router-dom';
import Register from './components/Register';

function App() {
  // let navigate = useNavigate();
  // const routeChange = () => {
  //   let path = `./components/login`;
  //   navigate(path);
  // };

  return (
    <div className='App'>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />} />
          <Route path="/login" element={<Login />} />
          <Route path="/registerStartup" element={<Register />} />
        </Routes>
       </BrowserRouter>
    </div>

  )
}

export default App;
