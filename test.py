import requests

BASE_URL = 'http://127.0.0.1:5000/'

# resp = requests.get(BASE_URL + 'hw')
# resp = requests.get(BASE_URL + 'hello/john')
# resp = requests.get(BASE_URL + 'student/john/doe/19/12312')
# resp = requests.get(BASE_URL + 'persons')
# resp = requests.get(BASE_URL + 'anime/1')
resp = requests.put(BASE_URL + 'anime/1', {'episodes': 80})

# print(resp.status_code)
print(resp.json())