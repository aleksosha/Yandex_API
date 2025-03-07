import requests
from Locators.locators import URL, TOKEN

response = requests.get("https://randomuser.me/api/")
response.json() # десериализация

r = response.json()
print(r["results"][0]["gender"]) #Сначала идет откуда и индекс места необходимых данных, далее выносим нужный параметр для получени
                                #Можно перечислять несколько: ['results'][0][dob][age]
                                #Если несколько вложенностей, то идет [data][results] -- далее внутри можно не по порядку[0][dob[age]