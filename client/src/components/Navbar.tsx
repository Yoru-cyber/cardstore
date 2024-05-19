function NavBar() {
  return (
    <>
      <nav className="flex flex-row p-2 items-center">
        <span className="flex flex-row items-center mr-5">
          <h2 className="font-bold">Cardstore</h2>
        </span>
        <a href="/" className="m-2">
          Home
        </a>
        <a href="/about" className="m-2">
          About
        </a>
        <a href="/cards" className="m-2">
          Cards
        </a>
      </nav>
    </>
  );
}
export default NavBar;
