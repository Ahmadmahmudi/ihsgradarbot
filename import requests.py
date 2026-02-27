import requests

TOKEN = "bot8527933196:AAEayPXeIYoTJXq9k2iIau22Q7dyifNEzRUO"
CHAT_ID = "273491234"

message = "Bot berhasil jalan 🚀"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": message
}

requests.post(url, data=payload)