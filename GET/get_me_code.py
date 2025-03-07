import requests
from Locators.locators import URL_ME, TOKEN

response = requests.get(URL_ME, headers={'Authorization': TOKEN})
assert response.status_code == 200
print(response.status_code)