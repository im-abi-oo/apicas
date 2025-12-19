import requests

BASE_URL = "https://currency.api-sina-free.workers.dev/"

def get_full_crypto_info(symbol):
    res = requests.get(
        BASE_URL,
        params={"crypto": symbol},
        timeout=10
    )

    if res.status_code != 200:
        print("Server Error")
        return

    data = res.json()

    if data.get("activ") != 1:
        print("Service is inactive")
        return

    coin = data["list"][0]

    print("Name:", coin["name"])
    print("Symbol:", coin["iso"])
    print("Rank:", coin["rank"])
    print("USD Price:", coin["price"])
    print("IRR Price:", coin["price_rial"])
    print("Buy Price:", coin["price_buy"])
    print("Sell Price:", coin["price_sell"])
    print("Market Cap:", coin["market_cap"])
    print("Daily Change:", coin["daily_change_percent"])
    print("BTC Equivalent:", coin["price_bitcoin"])
    print("Logo URL:", coin["logo"])
    print("Last Update:", data["time"])

get_full_crypto_info("btc")
