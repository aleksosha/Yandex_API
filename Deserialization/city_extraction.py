import requests
from Locators.locators import URL_CARDS, TOKEN

response = requests.get(URL_CARDS, headers={'Authorization': TOKEN})
#фигачим десериализацию
r = response.json()
assert 'Москва' == r['data'][0]['name']
print(r['data'][0]['name'])
