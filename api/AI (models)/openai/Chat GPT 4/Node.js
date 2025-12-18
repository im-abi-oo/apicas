import fetch from "node-fetch";

const API_URL = "https://gpt4.api-sina-free.workers.dev/gpt4";
const text = "How are you today?";

fetch(`${API_URL}?text=${encodeURIComponent(text)}`)
  .then(res => res.json())
  .then(data => {
    console.log("🤖 GPT-4 Answer:", data.result);
    console.log("👤 Developer:", data["Developed By"]);
    console.log("📡 Channels:", data.Channels);
  })
  .catch(err => {
    console.error("❌ Error while connecting to API:", err);
  });
