import fetch from "node-fetch";

const text = "What is artificial intelligence?";
const url = `https://deepseek-v3.api-sina-free.workers.dev/?text=${encodeURIComponent(text)}`;

fetch(url)
  .then(res => res.json())
  .then(data => {
    console.log("🧠 Answer:", data.answer);
    console.log("👤 Creator:", data.creator);
    console.log("📡 Channel:", data.channel);
  })
  .catch(err => {
    console.error("❌ Error:", err);
  });
