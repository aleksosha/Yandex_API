#Задание с параметрами

import requests

payload = {'postId': '1'} #Может быть в виде {'userId': '3', 'id': '29'}
response = requests.get('https://jsonplaceholder.typicode.com/comments', params=payload)
print(response.url)

print(response.content)