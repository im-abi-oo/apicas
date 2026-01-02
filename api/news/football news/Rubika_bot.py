import requests
from rubpy import Client, filters

API = "https://football.api-sina-free.workers.dev/news"

bot = Client(name="football_news_bot")

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip().lower()

    if text not in ["اخبار فوتبال", "/news", "football"]:
        return

    try:
        res = requests.get(API, timeout=10)
        data = res.json()
    except Exception as e:
        return await message.reply(f"❌ خطا در ارتباط با سرور:\n{e}")

    news_list = data.get("data", [])
    if not news_list:
        return await message.reply("❌ خبری دریافت نشد.")

    news = news_list[0]

    title = news.get("title", "-")
    subtitle = news.get("subtitle", "-")
    image = news.get("image", "")

    text_reply = (
        f"⚽ **{title}**\n\n"
        f"📰 {subtitle}"
    )

    if image:
        await message.reply_photo(
            photo=image,
            caption=text_reply,
            parse_mode="markdown"
        )
    else:
        await message.reply(
            text_reply,
            parse_mode="markdown"
        )

bot.run()
