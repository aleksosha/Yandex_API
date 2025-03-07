import requests
from Locators.locators import URL_SIGNUP

payload = {'email': 'lolkekreb@yandex.ru', 'password': 'qwerty'}
response = requests.post(URL_SIGNUP, data=payload)
print(response.status_code)
print(response.json())