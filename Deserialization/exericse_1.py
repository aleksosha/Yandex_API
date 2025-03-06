import requests

response = requests.get('https://jsonplaceholder.typicode.com/albums')
r = response.json()
print(r)