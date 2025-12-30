from rubpy import Client, filters
import requests

bot = Client(name="myket_bot")
API = "https://myket.api-sina-free.workers.dev/"

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()
    if not text.lower().startswith("مایکت"):
        return

    query = text[6:].strip()
    if not query:
        return await message.reply("❗ لطفاً نام اپلیکیشن را وارد کنید.")

    try:
        res = requests.get(API, params={
            "text": query,
            "lang": "fa",
            "count": 1,
            "format": "full"
        }, timeout=10)
        data = res.json()
    except Exception as e:
        return await message.reply(f"❌ خطا در ارتباط با سرور:\n{e}")

    if not data.get("ok"):
        return await message.reply(f"❌ خطا: {data.get('data')}")

    apps = data.get("data", [])
    if not apps:
        return await message.reply("❌ اپلیکیشنی پیدا نشد.")

    app = apps[0]

    name = app.get("name", "-")
    description = app.get("description", "-")
    screenshots_count = len(app.get("screenshots", []))
    download = app.get("download", "-")
    icon = app.get("icon", "")

    text_reply = (
        f"📝 **{name}**\n\n"
        f"📂 توضیحات:\n{description}\n\n"
        f"🖼 تعداد اسکرین‌شات‌ها: {screenshots_count}\n"
        f"⬇️ [دانلود]({download})"
    )

    if icon:
        await message.reply_photo(photo=icon, caption=text_reply, parse_mode="markdown")
    else:
        await message.reply(text_reply, parse_mode="markdown")

bot.run()
