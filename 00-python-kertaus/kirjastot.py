import requests

r = requests.get("https://samk.fi")
print(r.status_code)
