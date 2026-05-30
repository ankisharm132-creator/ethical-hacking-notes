import requests

response = requests.get("https://google.com")
print("Status Code:", response.status_code)
print("Website size:", len(response.text), "characters")
