import requests

# Generate Captcha
res = requests.get("https://captcha.api-sina-free.workers.dev/captcha")
data = res.json()

print("👤 Creator:", data["creator"])
print("📝 Captcha ID:", data["captcha_id"])
print("🖼 Captcha Base64:", data["captcha_base64"])

# Verify Captcha
captcha_id = data["captcha_id"]
user_input = "1234"

verify = requests.get(
    f"https://captcha.api-sina-free.workers.dev/captcha/verify?captcha_id={captcha_id}&user_input={user_input}"
)

print(verify.json())
