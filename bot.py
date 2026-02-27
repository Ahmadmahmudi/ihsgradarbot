import requests

TOKEN = "8527933196:AAEayPXeIYoTJXq9k2iIau22Q7dyifNEzRU"
CHAT_ID = "273491234"

url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=%5EJKSE,%5EGSPC"
r = requests.get(url)
data = r.json()['quoteResponse']['result']

ihsg = data[0]
sp = data[1]

ihsgChange = ihsg['regularMarketChangePercent']
spChange = sp['regularMarketChangePercent']

score = 0
if ihsgChange < 0:
    score -= 1
if spChange < 0:
    score -= 1

if score <= -2:
    signal = "⚠️ Bearish Kuat"
elif score == -1:
    signal = "⚠️ Bearish Ringan"
elif score == 0:
    signal = "🤔 Sideways"
else:
    signal = "🚀 Bullish Bias"

message = f"""
📊 IHSG Radar Update

IHSG: {ihsg['regularMarketPrice']} ({ihsgChange:.2f}%)
S&P500: {sp['regularMarketPrice']} ({spChange:.2f}%)

Bias Besok:
{signal}

Gunakan risk management ⚠️
"""

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": message}
)