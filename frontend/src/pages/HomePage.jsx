import React from "react";
import CreateProject from "../components/CreateProject";

function HomePage() {
  return (
    <div>
      <h2>Welcome to the Project Simulator</h2>
      <p>Please use the menu to navigate.</p>
      <CreateProject />
    </div>
  );
}

export default HomePage;
