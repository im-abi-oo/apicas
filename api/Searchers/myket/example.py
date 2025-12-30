import requests

API = "https://myket.api-sina-free.workers.dev/"

def search_app(text, lang="fa", count=10, page=1, sort="", format="full"):
    params = {
        "text": text,
        "lang": lang,
        "count": count,
        "page": page,
        "sort": sort,
        "format": format
    }
    res = requests.get(API, params=params, timeout=10)
    data = res.json()
    return data

apps = search_app("Telegram")
print(apps)
