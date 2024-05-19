import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Cards from "./pages/Cards";
import About from "./pages/About";
import NavBar from "./components/Navbar";
function App() {
  return (
    <>
      <NavBar />

        <Routes>
          <Route path="/" element={<Home />}></Route>
          <Route path="/about" element={<About />}></Route>
          <Route path="/cards" element={<Cards />}></Route>
        </Routes>

    </>
  );
}

export default App;
