const API = "https://myket.api-sina-free.workers.dev/";

async function searchApp(text) {
  const params = new URLSearchParams({
    text,
    lang: "fa",
    count: 10,
    page: 1,
    sort: "popular",
    format: "full"
  });
  const res = await fetch(`${API}?${params}`);
  const data = await res.json();
  console.log(data);
}

searchApp("Telegram");
