import requests

res = requests.get("https://dastan.api-sina-free.workers.dev")
data = res.json()

if data["status"]:
    print("📖 Random Story:\n")
    print(data["result"])
