import React, { useEffect, useState } from "react";

export default function ControlPanel() {
  const [status, setStatus] = useState("Betöltés...");
  const [power, setPower] = useState(0);
  const [mode, setMode] = useState("AutoTrade");

  useEffect(() => {
    const interval = setInterval(() => {
      // Simulált valós idejű adat – később a backendből jön majd
      setPower(Math.floor(Math.random() * 100));
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="control-panel">
      <h2>Fusion vezérlő</h2>
      <p><b>AI mód:</b> {mode}</p>
      <p><b>Állapot:</b> {status}</p>
      <div className="power-bar">
        <div className="power-fill" style={{ width: `${power}%` }}></div>
      </div>
      <p>Fusion Power: {power}%</p>
    </div>
  );
}
