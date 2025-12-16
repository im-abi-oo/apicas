import fetch from "node-fetch";

const url = "https://number.api-sina-free.workers.dev/98765";

fetch(url)
  .then(res => res.json())
  .then(data => console.log(data));
