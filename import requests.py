import requests

TOKEN = "bot8527933196:AAEayPXeIYoTJXq9k2iIau22Q7dyifNEzRUO"
CHAT_ID = "273491234"

message = "Bot berhasil jalan 🚀"

url = f"https://api.telegram.org/bot8527933196:AAEayPXeIYoTJXq9k2iIau22Q7dyifNEzRUO/sendMessage"

payload = {
    "chat_id": 273491234,
    "text": hai bro
}

requests.post(url, data=payload)