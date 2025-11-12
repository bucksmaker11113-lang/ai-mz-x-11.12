import React, { useEffect, useState } from "react";

export default function LogFeed() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    const addLog = () => {
      const newLog = {
        time: new Date().toLocaleTimeString(),
        msg: "Fusion ciklus lefutott – predikció frissítve."
      };
      setLogs(prev => [newLog, ...prev.slice(0, 4)]);
    };
    const interval = setInterval(addLog, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="log-feed">
      <h3>Valós idejű Fusion napló</h3>
      <ul>
        {logs.map((log, i) => (
          <li key={i}>
            <span>[{log.time}]</span> {log.msg}
          </li>
        ))}
      </ul>
    </div>
  );
}
