import requests as r

# resp = r.get('http://127.0.0.1:5000/')
# if resp.status_code == 200: # Check is "OK"
#     print(resp.json()) # Print JSON data

resp = r.get('http://127.0.0.1:5000/person/tim')
print(resp.json())