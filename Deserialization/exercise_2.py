import requests
from Locators.locators import URL_ME, TOKEN, EMAIL

def test_email_name():
   response = requests.get(URL_ME, headers={'Authorization': TOKEN})
   r = response.json()
   print(r)
   print(response.status_code)
   assert 'drobotunaleksandragen12@yandex.ru' == r['data']['email']

#test_email_name()
