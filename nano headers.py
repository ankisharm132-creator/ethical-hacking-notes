import requests

response = requests.get("https://google.com")
print("Server:", response.headers.get("server"))
print("Content Type:", response.headers.get("content-type"))
