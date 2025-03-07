import json
import requests

payload = {
    'item': 'pear',
    'price': '5$'
}

payload_string = json.dumps(payload)
response = requests.post('https://httpbin.org/post', data=payload_string)
print(response.json())
