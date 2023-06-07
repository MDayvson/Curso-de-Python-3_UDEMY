# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> 80
# https:// -> 443
url = 'http://127.0.0.1:5500/EXTRA_Landing%20Page/index.html'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
print(response.text)
