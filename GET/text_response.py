import requests
from Locators.locators import URL_CAT_NINJA, TOKEN

response = requests.get(URL_CAT_NINJA)
#Получаем тело ответа, text = атрибут по типу status_code, нужен для вывода json
print(response.text)