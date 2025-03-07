import json
import requests

payload = {
    'userId': 2,
    'title': 'Alea jacta est.'
}

payload_string = json.dumps(payload)
headers = {'Content-type': 'application/json'}
response = requests.post('https://jsonplaceholder.typicode.com/albums', data=payload_string, headers=headers)

print(response.text)