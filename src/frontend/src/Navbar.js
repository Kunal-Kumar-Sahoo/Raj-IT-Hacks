import { useState } from "react";
import { Link } from "react-scroll";


const Navbar = () => {
    const [click, setClick] = useState(false)
    const handleClick = () => setClick(!click);

    const closeMenu = () => setClick(false)
    return (
        <nav>
            <ul>
                <li><button onClick={handleClick}>About Us</button></li>
                <li><Link to="Start-Up" spy={true} smooth={true} offset={50} duration={500} onClick={closeMenu}>Start-up</Link></li>
                <li><a href="#investors" onClick={handleClick}>Investor</a></li>
                <li><button onClick={handleClick}>Public</button></li>
            </ul>
        </nav>
    );
};

export default Navbar;