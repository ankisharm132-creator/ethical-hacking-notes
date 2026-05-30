import requests

websites = ["https://google.com", "https://facebook.com", "https://youtube.com"]

for site in websites:
    response = requests.get(site)
    if response.status_code == 200:
        print(site + " — ONLINE ✅")
    else:
        print(site + " — OFFLINE ❌")
