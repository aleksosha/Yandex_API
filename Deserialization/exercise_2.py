import requests
from Locators.locators import URL, TOKEN

def test_email_name():
   response = requests.get('https://qa-mesto.praktikum-services.ru/api/users/me', headers={'Authorization':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2N2M5ODVjNmQ3MjkyYTAwM2RmMjkxNmMiLCJpYXQiOjE3NDEyNjM3MzgsImV4cCI6MTc0MTg2ODUzOH0.9XTgqHBbbA6LGULpHL-zCqpNAGWgyF78z0vzoIh25J4'})
   print(response.status_code)
   r = response.json()
   result = r["data"].get('email')
   print(result)
   assert 'drobotunalexandra12345@yandex.ru' == r['data']['email']

test_email_name()