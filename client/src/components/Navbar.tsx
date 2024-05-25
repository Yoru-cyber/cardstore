import { Link } from "react-router-dom";
function NavBar() {
  return (
    <>
      <nav className="flex flex-row p-2 items-center">
        <span className="flex flex-row items-center mr-5">
          <Link to="/" className="font-bold text-2xl mr-2">Cardstore</Link>
          <img src="./vite.svg" alt="" />
        </span>
        <Link to="/" className="m-2">
          Home
        </Link>
        <Link to="/about" className="m-2">
          About
        </Link>
        <Link to="/cards" className="m-2">
          Cards
        </Link>
        <Link
          to="/signup"
          className="m-2 outline outline-1 outline-blue-800/80 bg-blue-800/30 rounded-md p-1 text-blue-100/90 text-indigo-300"
        >
         Sign up
        </Link>
      </nav>
    </>
  );
}
export default NavBar;
