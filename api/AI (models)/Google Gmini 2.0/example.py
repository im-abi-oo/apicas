import requests

url = "https://gemini.api-sina-free.workers.dev/?text=What%20is%20AI?"
response = requests.get(url, timeout=15)
data = response.json()

print("👤 Creator:", data["creator"])
print("📡 Channel:", data["channel"])
print("🤖 Gemini Answer:", data["answer"])
