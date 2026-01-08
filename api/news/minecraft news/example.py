import requests

API = "https://minecraft-api-sina-free.leapcell.app/minecraft-news"

def getminecraftnews(page=1):
    try:
        res = requests.get(API, params={"page": page}, timeout=10)
        return res.json()
    except Exception as e:
        return {
            "ok": False,
            "error": str(e)
        }

newsdata = getminecraft_news()

for news in news_data.get("items", []):
    print(news["title"], news["link"])
