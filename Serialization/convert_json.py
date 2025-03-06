# импортируем библиотеку
import json
import requests

# словарь
data = {
    'item': 'pear',
    'price': '5$'
}

# сериализуем словарь в JSON-структуру
json_string = json.dumps(data)
r = requests.post('https://httpbin.org/post', data=json_string)
response_json = r.json()

print(json.dumps(response_json))
