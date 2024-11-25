import requests

BASE_URL = 'http://127.0.0.1:5000/'

resp = requests.get(BASE_URL + 'hello')
# resp = requests.post(BASE_URL + 'hello')

# print(resp.status_code)
print(resp.json())