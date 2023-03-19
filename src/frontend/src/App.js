import Header from "./Header";
import Landingpage from "./Landingpage";
import Footer from "./Footer";
import Navbar from "./Navbar";
import Sections from "./Sections";
// import Login from "./login/Login";
// import { useRef } from "react";

function App() {
  const handleClick = (e) => {
    e.preventDefault();
    const element = document.getElementById('Public View')
    if (element) {
      element.scrollIntoView({ behaviour:'smooth' })
    }
  };
  // const ref = useRef(null);

  // const handleClick = () => {
  //   ref.current?.scrollIntoView({ behavior: 'smooth' });
  // };

  return (
    <div className="App">
      <Navbar handleClick={handleClick} />
      <Header />
      <Landingpage />
      <Sections />
      <Footer />
    </div>
  );
}

export default App;
