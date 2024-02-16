import "./HomePage.css";

function HomePage() {
  return (
    <div id="root-container">
      <div id="container">
        <div id="sidebar">
          <div id="workspaces" className="selected">Workspaces</div>
          <div id="channels">Channels</div>
          <div id="direct-messages">Direct messages</div>
        </div>
        <div id="main-content">
          MAIN COTENT
        </div>
      </div>
    </div>
  );
}

export default HomePage;
