import requests

payload = {"email": "drobotunaleksandragen12@yandex.ru", 'password': "drobotun123"}
response = requests.post('https://qa-mesto.praktikum-services.ru/api/signin', data=payload)
print(response.status_code)
print(response.json()['data']['avatar'])
