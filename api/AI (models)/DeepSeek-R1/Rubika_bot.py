from rubpy import Client, filters
import requests

bot = Client(name="deepseek_bot")

API_URL = "https://deepseek.api-sina-free.workers.dev/"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if not text.startswith("هوش"):
        return

    query = text.replace("هوش", "", 1).strip()
    if not query:
        return await message.reply("❗️ لطفاً یک متن وارد کنید.")

    try:
        res = requests.get(f"{API_URL}?text={query}", timeout=15)
        data = res.json()
        await message.reply(f"🧠 *پاسخ DeepSeek:*\n\n{data['answer']}", parse_mode="markdown")
    except Exception as e:
        await message.reply(f"❌ خطا در ارتباط با سرور:\n{e}")

bot.run()
