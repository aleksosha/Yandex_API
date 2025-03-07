import requests
from Locators.locators import URL_CARDS, TOKEN

#выносим аргументы
payload = {"name": "Mesto",
            'link': 'https://code.s3.yandex.net/qa-automation-engineer/python/files/photoSelenide.jpeg'}
response = requests.post(URL_CARDS, data=payload,
                         headers={'Authorization': TOKEN})
print(response.status_code)
#десериализация
print(response.json()['data'])