import requests
from Locators.locators import URL_SIGNIN

payload = {"email": "drobotunaleksandragen12@yandex.ru", 'password': "drobotun123"}
response = requests.post(URL_SIGNIN, data=payload)
print(response.status_code)
print(response.json()['data']['avatar'])