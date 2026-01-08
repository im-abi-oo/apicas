import requests
from rubpy import Client, filters

API = "https://minecraft-api-sina-free.leapcell.app/minecraft-news"

bot = Client(name="minecraftnewsbot")

@bot.onmessageupdates(filters.text)
async def handler(message):
    text = message.text.strip().lower()

    if text not in ["اخبار ماینکرفت", "/minecraft", "minecraft"]:
        return

    try:
        res = requests.get(API, timeout=10)
        data = res.json()
    except Exception as e:
        return await message.reply(f"❌ خطا در ارتباط با سرور:\n{e}")

    news_list = data.get("items", [])
    if not news_list:
        return await message.reply("❌ خبری دریافت نشد.")

    news = news_list[0]

    title = news.get("title", "-")
    summary = news.get("summary", "-")
    image = news.get("image_url", "")

    reply_text = (
        f"🎮 {title}\n\n"
        f"📰 {summary}"
    )

    if image:
        await message.reply_photo(
            photo=image,
            caption=reply_text,
            parse_mode="markdown"
        )
    else:
        await message.reply(
            reply_text,
            parse_mode="markdown"
        )

bot.run()
