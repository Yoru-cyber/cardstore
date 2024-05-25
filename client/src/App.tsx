import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Cards from "./pages/Cards";
import About from "./pages/About";
import NavBar from "./components/Navbar";
import SignUp from "./pages/SignUp";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
function App() {
  return (
    <>
      <NavBar />
      <ToastContainer
      theme="dark"
        position="top-right"
        newestOnTop={true}
        autoClose={5000}
        closeOnClick={true}
        draggablePercent={60}
      />
      <Routes>
        <Route path="/" element={<Home />}></Route>
        <Route path="/about" element={<About />}></Route>
        <Route path="/cards" element={<Cards />}></Route>
        <Route path="/signup" element={<SignUp />}></Route>
      </Routes>
    </>
  );
}

export default App;
