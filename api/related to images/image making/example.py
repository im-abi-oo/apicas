import requests

url = "https://image.api-sina-free.workers.dev/generate?text=golden dragon in the sky"

res = requests.get(url)

with open("result.jpg", "wb") as f:
    f.write(res.content)

print("Image saved!")
