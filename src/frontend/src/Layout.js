import React from "react";

// import { Outlet } from "react-router-dom";
import { Banner } from "./components/Banner";
import { Startup } from "./components/Startup";
import { Projects } from "./components/Projects";
import { Investors } from "./components/Investors";
import { Contact } from "./components/Contact";
import { Nav, Navi } from "./components/Navi.js";
// import Navbar from './Navbar';
import { Footer } from "./components/Footer";
import { NavBar } from "./components/Navi";

const Layout = () => {
    return (
        <div className="App">
            {/* <NavBar/> */}
            {/* <Oulet /> */}
            <Navi/>
            <Banner />
            <Startup />
            <Projects />
            <Investors />
            <Contact />
            <Footer />
        </div>
    );
};

export default Layout;