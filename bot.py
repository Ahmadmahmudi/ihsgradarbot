import requests

symbol = "BBCA.JK"

url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

print("Status Code:", r.status_code)
print("Response Text:", r.text)

if r.status_code == 200:
    try:
        data = r.json()['quoteResponse']['result']
        print(data)
    except Exception as e:
        print("JSON error:", e)
else:
    print("Request failed")