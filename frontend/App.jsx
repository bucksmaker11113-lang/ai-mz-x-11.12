import React from "react";
import "./styles/global.css";
import FusionCanvas from "./components/FusionCanvas";
import ControlPanel from "./components/ControlPanel";
import LogFeed from "./components/LogFeed";

export default function App() {
  return (
    <div className="dashboard">
      {/* Bal oldal – Piaci vezérlőpanel */}
      <div className="side-panel">
        <h2>Piaci Adatok</h2>
        <ControlPanel />
      </div>

      {/* Középső rész – Fusion Core AI motor */}
      <div className="fusion-core">
        <FusionCanvas />
      </div>

      {/* Jobb oldal – Napló és riportok */}
      <div className="side-panel">
        <h2>AI Napló</h2>
        <LogFeed />
      </div>

      {/* Alsó rész – Chat konzol */}
      <div className="chat-console">
        <input
          type="text"
          placeholder="Írj be egy parancsot... (pl. Elemzés indítása)"
          className="chat-input"
        />
        <button className="chat-button">Küldés</button>
      </div>
    </div>
  );
}
