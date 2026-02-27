import requests

# ====== SETTING ======
TOKEN = "bot8527933196:AAEayPXeIYoTJXq9k2iIau22Q7dyifNEzRU"
CHAT_ID = "273491234"
SYMBOL = "BBCA.JK"   # ganti saham lo
ALERT_PERCENT = 1    # alert kalau naik > 1%

# =====================

url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={SYMBOL}"
headers = {"User-Agent": "Mozilla/5.0"}

r = requests.get(url, headers=headers)

if r.status_code != 200:
    print("Gagal ambil data")
    exit()

data = r.json()['quoteResponse']['result']

if not data:
    print("Data kosong")
    exit()

price = data[0]['regularMarketPrice']
prev_close = data[0]['regularMarketPreviousClose']

change_percent = ((price - prev_close) / prev_close) * 100

message = f"""
📊 {SYMBOL}
Harga: {price}
Perubahan: {change_percent:.2f}%
"""

# ALERT jika naik lebih dari batas
if change_percent >= ALERT_PERCENT:
    message += "\n🚀 ALERT: Harga naik signifikan!"

telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": message
}

requests.post(telegram_url, data=payload)

print("Pesan terkirim")