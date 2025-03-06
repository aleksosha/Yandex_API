import requests

response_delete = requests.delete('https://dummyjson.com/products/15')
r = response_delete.json()
print(response_delete.status_code)
print(r)