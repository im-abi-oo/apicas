const API = "https://minecraft-api-sina-free.leapcell.app/minecraft-news";

async function getMinecraftNews() {
  try {
    const res = await fetch(API + "?page=1");
    const data = await res.json();
    console.log(data.items);
  } catch (err) {
    console.error("Error fetching news:", err);
  }
}

getMinecraftNews();
