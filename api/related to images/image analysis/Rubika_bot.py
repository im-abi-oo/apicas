from rubpy import Client, filters
import requests

bot = Client(name="sina_ocr_bot")

@bot.on_message_updates(filters.text)
async def handler(message):
    txt = message.text.strip()

    if txt.startswith("ocr "):
        arg = txt.replace("ocr ", "")
        if arg.startswith("http"):
            link = f"https://image-analysis.api-sina-free.workers.dev/?url={arg}"
            res = requests.get(link).json()
        else:
            with open(arg, "rb") as f:
                res = requests.post("https://image-analysis.api-sina-free.workers.dev/", files={"image": f}).json()

        await message.reply_text(f"Extracted Text:\n{res.get('text','No text found')}")

bot.run()
