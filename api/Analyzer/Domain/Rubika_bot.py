from rubpy import Client, filters
import requests

bot = Client(name="domain_analyzer_bot")

def analyze_domain(domain):
    url = f"https://abolfazlzarei.sbs/domain/?action=analyze&domain={domain}"
    try:
        res = requests.get(url, timeout=10)
        return res.json()
    except:
        return None

@bot.on_message_updates(filters.text)
async def handler(message):
    text = message.text.strip()

    if text.startswith("دامنه"):
        domain = text.replace("دامنه", "").strip()

        if not domain:
            return await message.reply("❗ لطفاً نام دامنه را وارد کنید.\nمثال:\nدامنه tabairan.com")

        data = analyze_domain(domain)
        if not data or "data" not in data:
            return await message.reply("❌ خطا در دریافت اطلاعات دامنه.")

        d = data["data"]

        output = (
            f"🌐 *آنالیز دامنه*\n\n"
            f"🔹 دامنه: `{domain}`\n"
            f"📡 IP: `{d['dns_lookup']['results']['ip']}`\n"
            f"🏢 Registrar: {d['domain_whois']['registrar']['name']}\n"
            f"📍 کشور: {d['ip_whois']['country']}\n"
            f"☁️ ISP: {d['ip_whois']['isp']}\n"
            f"🛡 Fraud Score: {d['ip_location']['fraud_score']}\n"
            f"⏳ عمر دامنه: {d['domain_whois']['domain_age']} روز"
        )

        await message.reply(output, parse_mode="markdown")

bot.run()
