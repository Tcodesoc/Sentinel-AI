import "./App.css";
import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [scan, setScan] = useState(null);

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

    // FIX: safe assignment
    setScan(typeof data.reply === "string" ? null : data.reply);
  };

  return (
    <div className="container">
      <h1>🛡️ Sentinel AI</h1>

      <p className="subtitle">
        AI-Powered Cybersecurity Assistant
      </p>

      <div className="searchBox">
        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Example: scan openai.com"
        />

        <button onClick={sendMessage}>
          Scan
        </button>
      </div>

      {scan?.website && (
        <div className="report">
          <h2>🌐 {scan.website}</h2>

          <p style={{ color: "#94a3b8" }}>
            🕒 Scan Time: {scan.scan_time}
          </p>

          <div className="stats">
            <div className="card">
              <h3>🌐 Status</h3>
              <p>{scan.status}</p>
            </div>

            <div className="card">
              <h3>🔒 HTTPS</h3>
              <p>{scan.https ? "✅ Enabled" : "❌ Disabled"}</p>
            </div>

            <div className="card">
              <h3>📡 HTTP Code</h3>
              <p>{scan.status_code}</p>
            </div>

            <div className="card">
              <h3>⚡ Response</h3>
              <p>
                {scan.response_time !== null
                  ? `${scan.response_time} ms`
                  : "N/A"}
              </p>
            </div>
          </div>

          <h2
            style={{
              color:
                scan.score >= 80
                  ? "#22c55e"
                  : scan.score >= 60
                  ? "#facc15"
                  : "#ef4444",
            }}
          >
            {scan.risk}
          </h2>

          <hr />

          <h3>Header Summary</h3>
          <p>
            {scan.passed_headers} / {scan.total_headers} Security Headers Present
          </p>

          <ul>
            <li>
              HSTS:{" "}
              {scan.headers?.["Strict-Transport-Security"] ? "✅" : "❌"}
            </li>

            <li>
              CSP:{" "}
              {scan.headers?.["Content-Security-Policy"] ? "✅" : "❌"}
            </li>

            <li>
              X-Frame-Options:{" "}
              {scan.headers?.["X-Frame-Options"] ? "✅" : "❌"}
            </li>

            <li>
              X-Content-Type-Options:{" "}
              {scan.headers?.["X-Content-Type-Options"] ? "✅" : "❌"}
            </li>
          </ul>

          <hr />

          <h3>Recommendations</h3>

          <ul>
            {(scan.recommendations || []).map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
          <hr />
          <hr />

<h3>🔐 SSL Certificate</h3>

{scan.ssl?.valid ? (
  <div>
    <p>
      ✅ Certificate Valid
    </p>

    <p>
      Issuer: {scan.ssl.issuer}
    </p>

    <p>
      TLS Version: {scan.ssl.tls_version}
    </p>

    <p>
      Expires: {scan.ssl.expires}
    </p>

    <p>
      Days Remaining: {scan.ssl.days_remaining} days
    </p>
  </div>
) : (
  <p>
    ❌ SSL certificate information unavailable
  </p>
)}

<h3>🤖 AI Security Analysis</h3>

<p>
  {scan.explanations}
</p>
        </div>
      )}
    </div>
  );
}

export default App;