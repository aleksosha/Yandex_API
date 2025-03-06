import requests
from Locators.locators import URL, TOKEN

response = requests.post(URL, data={
    'name': 'Красивое место',
    'link': 'https://code.s3.yandex.net/qa-automation-engineer/python/files/photoSelenide.jpeg'}, headers={'Authorization': TOKEN})
print(response.status_code)