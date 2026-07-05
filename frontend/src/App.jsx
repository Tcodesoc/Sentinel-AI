import "./App.css";
import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("Run a security scan to begin.");

  const sendMessage = async () => {
    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: "Sharon",
        message: message,
      }),
    });

    const data = await response.json();
    setReply(data.reply);
  };

  return (
    <div className="container">

      <h1>🛡️ Sentinel AI</h1>

      <p className="subtitle">
        AI-Powered Cybersecurity Assistant
      </p>

      <div className="searchBox">
        <input
          type="text"
          placeholder="Example: scan openai.com"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />

        <button onClick={sendMessage}>
          Scan
        </button>
      </div>

      <div className="report">
        <pre>{reply}</pre>
      </div>

    </div>
  );
}

export default App;