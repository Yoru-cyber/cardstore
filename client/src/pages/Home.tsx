import { Text, Em } from "@radix-ui/themes";
function Home() {
  return (
    <main className="p-3 text-center">
      <h2 className="text-xl">This is a fake e-commerce to buy cards.</h2>
      <Text>
        You can see the cards, sign up and as many as you wish. <Em>All fake of course :)</Em>
      </Text>
    </main>
  );
}
export default Home;