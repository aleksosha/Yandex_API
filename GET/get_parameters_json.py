import requests
from Locators.locators import URL_JSON_COMMENTS

payload = {'postId': 1}
response  = requests.get(URL_JSON_COMMENTS, params=payload)
print(response.url) #Вывожу ручку, которая получается в параметрами
print(response.content) #Вывожу данные этой ручки
