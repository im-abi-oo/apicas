import requests

url = "https://gpt4.api-sina-free.workers.dev/gpt4?text=How are you?"
res = requests.get(url)
data = res.json()

print("👤 Developer:", data["Developed By"])
print("📡 Channels:", data["Channels"])
print("🤖 GPT-4 Answer:", data["result"])
