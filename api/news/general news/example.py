import requests

res = requests.get("https://news.api-sina-free.workers.dev/news")
data = res.json()

print("📰 Total News:", data["count"])

for item in data["news"]:
    print("🔸", item["title"])
    print("🔗", item["link"])
    print("-" * 30)
