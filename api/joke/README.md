# 😂 SinaJokeAPI version : 1.0.0

وب‌سرویس **SinaJokeAPI** یک API سرگرم‌کننده و سبک برای دریافت **جوک‌های رندوم** و **جوک‌های فانتزی** است 🤣🎭  
مناسب برای ربات‌ها، اپلیکیشن‌ها و سایت‌ها — فقط با یک درخواست GET  
**بدون نیاز به API Key** 🚀

---

## 🌐 آدرس وب‌سرویس‌ها

### 🔹 جوک معمولی
https://jok.api-sina-free.workers.dev/jok

### 🔹 جوک فانتزی
https://jok.api-sina-free.workers.dev/fantezi

---

## 📥 ورودی وب‌سرویس

این API **هیچ ورودی یا پارامتری ندارد**  
با هر درخواست، یک متن تصادفی برگردانده می‌شود 🎲

---

## 📦 ساختار خروجی وب‌سرویس

| کلید | نوع | توضیح |
|-----|-----|--------|
| `channel` | `string` | شناسه کانال منتشرکننده |
| `creator` | `string` | نام توسعه‌دهنده |
| `result` | `string` | متن جوک (رندوم) |

---

## 🧪 نمونه درخواست‌ها

### دریافت جوک معمولی
`GET` https://jok.api-sina-free.workers.dev/jok

### دریافت جوک فانتزی
`GET` https://jok.api-sina-free.workers.dev/fantezi

---

## 🧾 نمونه خروجی جوک معمولی

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "result": "طرف با موتور اومد از کنارم رد شد داشت میخوند ... مدیونید اگه فک کنید طرف با سرعت جت رفت تو افق"
}
```

---

# 🧾 نمونه خروجی جوک فانتزی

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "result": "یکی از فانتزیام اینه که تو کلاس استاد ازم بپرسه شغل پدرت چیه ... هدف فقط شوخی و خنده بود"
}
```

---

# 💻 نمونه استفاده در Python

```py
import requests

# Joke
jok_res = requests.get("https://jok.api-sina-free.workers.dev/jok")
jok_data = jok_res.json()
print("😂 Joke:", jok_data["result"])

# Fantasy Joke
fan_res = requests.get("https://jok.api-sina-free.workers.dev/fantezi")
fan_data = fan_res.json()
print("🎭 Fantasy Joke:", fan_data["result"])
```

---

# 🤖 استفاده در ربات روبیکا / بات‌ها

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_joke_bot")

JOK_URL = "https://jok.api-sina-free.workers.dev/jok"
FAN_URL = "https://jok.api-sina-free.workers.dev/fantezi"

def fetch(url):
    try:
        return requests.get(url, timeout=5).json()
    except:
        return None

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text == "جوک":
        data = fetch(JOK_URL)
        if not data:
            return await message.reply("❌ خطا در دریافت جوک")
        await message.reply(f"😂 {data['result']}")

    elif text == "جوک فانتزی":
        data = fetch(FAN_URL)
        if not data:
            return await message.reply("❌ خطا در دریافت جوک فانتزی")
        await message.reply(f"🎭 {data['result']}")

bot.run()
```

---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers                     
🗳 Rubika: https://rubika.ir/Sinabani_api                    
🔗 Joke Endpoint: https://jok.api-sina-free.workers.dev/jok                    
🔗 Fantasy Endpoint: https://jok.api-sina-free.workers.dev/fantezi

---

---

# 😂 SinaJokeAPI version : 1.0.0

**SinaJokeAPI** is a lightweight and entertaining API for delivering **random jokes** and **fantasy jokes** 🤣🎭  
Perfect for bots, applications, and websites — accessible via simple GET requests  
**No API key required** 🚀

---

## 🌐 API Endpoints

### 🔹 Normal Joke
https://jok.api-sina-free.workers.dev/jok

### 🔹 Fantasy Joke
https://jok.api-sina-free.workers.dev/fantezi

---

## 📥 API Input

This API **does not require any input parameters**  
Each request returns a randomly selected joke 🎲

---

## 📦 API Response Structure

| Key | Type | Description |
|-----|------|-------------|
| `channel` | `string` | Publisher channel identifier |
| `creator` | `string` | Developer username |
| `result` | `string` | Joke text (random) |

---

## 🧪 Sample Requests

### Get a Normal Joke
`GET` https://jok.api-sina-free.workers.dev/jok

### Get a Fantasy Joke
`GET` https://jok.api-sina-free.workers.dev/fantezi

---

## 🧾 Sample Response (Normal Joke)

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "result": "A guy passed by me on a motorcycle while singing... you’d be wrong if you think he disappeared into the horizon at jet speed"
}
```

---

# 🧾 Sample Response (Fantasy Joke)

```json
{
  "channel": "@Sinabani_api",
  "creator": "@Sinabanis",
  "result": "One of my fantasies is that the professor asks me in class what my father does... the whole story was just for fun and laughter"
}
```

---

# 💻 Python Usage Example

```py
import requests

# Normal Joke
jok_res = requests.get("https://jok.api-sina-free.workers.dev/jok")
jok_data = jok_res.json()
print("😂 Joke:", jok_data["result"])

# Fantasy Joke
fan_res = requests.get("https://jok.api-sina-free.workers.dev/fantezi")
fan_data = fan_res.json()
print("🎭 Fantasy Joke:", fan_data["result"])
```

---

# 🤖 Rubika Bot / Chatbot Example

```py
from rubpy import Client, filters
import requests

bot = Client(name="sina_joke_bot")

JOK_URL = "https://jok.api-sina-free.workers.dev/jok"
FAN_URL = "https://jok.api-sina-free.workers.dev/fantezi"

def fetch(url):
    try:
        return requests.get(url, timeout=5).json()
    except:
        return None

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text.lower() == "joke":
        data = fetch(JOK_URL)
        if not data:
            return await message.reply("❌ Failed to fetch joke.")
        await message.reply(f"😂 {data['result']}")

    elif text.lower() == "fantasy joke":
        data = fetch(FAN_URL)
        if not data:
            return await message.reply("❌ Failed to fetch fantasy joke.")
        await message.reply(f"🎭 {data['result']}")

bot.run()
```

---

# 👤 Developer

mir sina banihashem

📍 Hosted on: Cloudflare Workers              
🗳 Rubika: https://rubika.ir/Sinabani_api                       
🔗 Joke Endpoint: https://jok.api-sina-free.workers.dev/jok              
🔗 Fantasy Endpoint: https://jok.api-sina-free.workers.dev/fantezi
