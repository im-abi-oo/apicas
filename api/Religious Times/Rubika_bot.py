import requests
from rubpy import Client, filters

API_BASE = "https://abolfazlzarei.sbs/ReligiousTimes.php/oghat?q="

bot = Client(name="religious_times_full_bot")


@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if not (
        text.startswith("اوقات شرعی")
        or text.startswith("/oghat")
        or text.lower().startswith("prayer")
    ):
        return

    parts = text.split(" ", 1)
    if len(parts) < 2:
        return await message.reply(
            "❌ Please enter a city name.\nExample:\nاوقات شرعی مشهد"
        )

    city = parts[1]

    try:
        res = requests.get(API_BASE + city, timeout=10)
        data = res.json()
    except Exception as e:
        return await message.reply(f"❌ Connection error:\n{e}")

    if data.get("status") != 200:
        return await message.reply(
            f"❌ Error:\n{data.get('message', 'Unknown error')}"
        )

    location = data["data"]["location"]
    out = data["data"]["prayer_times"]["out"]

    # ساخت پاسخ (استفاده از همه داده‌ها)
    reply_text = (
        f"🕌 **Religious Times**\n\n"
        f"📍 **Location Info**\n"
        f"🏙 City: {location['city']}\n"
        f"🗺 Province: {location['province']}\n"
        f"📌 Address: {location['full_address']}\n"
        f"🌍 Coordinates: {location['coordinates']['latitude']}, "
        f"{location['coordinates']['longitude']}\n\n"

        f"🕰 **Prayer Times**\n"
        f"🌅 Fajr: {out['Fajr']} (Exact: {out['FFajr']})\n"
        f"☀️ Sunrise: {out['Sunrise']} (Exact: {out['FSunrise']})\n"
        f"🕛 Dhuhr: {out['Dhuhr']}\n"
        f"🕒 Asr: {out['Asr']}\n"
        f"🌇 Sunset: {out['Sunset']}\n"
        f"🌙 Maghrib: {out['Maghrib']}\n"
        f"🌃 Isha: {out['Isha']}\n"
        f"🕰 Midnight: {out['Midnight']}\n\n"

        f"📅 **Dates**\n"
        f"🇮🇷 Shamsi: {out['ys']}/{out['ms']}/{out['ds']}\n"
        f"🌙 Hijri: {out['yg']} {out['mg']} {out['dg']}\n"
        f"🌍 Gregorian: {out['ym']}/{out['mm']}/{out['dm']}\n"
        f"📆 Weekday: {out['week']}\n\n"

        f"👨‍💻 Developer: {data['developer']}\n"
        f"⏱ Timestamp: {data['timestamp']}"
    )

    await message.reply(reply_text, parse_mode="markdown")


bot.run()
