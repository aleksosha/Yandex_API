import requests
from Locators.locators import URL_CARDS, TOKEN

url = 'https://qa-mesto.praktikum-services.ru'
response = requests.post(URL_CARDS, data={'name': 'Мест',
                                          'link': 'https://code.s3.yandex.net/qa-automation-engineer/java/files/paid-track/sprint1/photoSelenide.jpg'},headers={'Authorization': TOKEN})
id_photo = response.json()['data']['_id']

response_delete = requests.delete(f"{URL_CARDS}/{id_photo}", headers={'Authorization': TOKEN})

assert response_delete.status_code == 200