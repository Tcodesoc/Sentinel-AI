import "./App.css";
import { useState } from "react";

function App() {

  const [message, setMessage] = useState("");
  const [reply, setReply] = useState("AI response will appear here.");

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

      <p>Your AI Cybersecurity Assistant</p>

      <input
        type="text"
        placeholder="Ask me something..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button onClick={sendMessage}>
        Send
      </button>

      <div className="response">
        {reply}
      </div>

    </div>
  );
}

export default App;