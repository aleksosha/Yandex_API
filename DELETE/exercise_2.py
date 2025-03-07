import requests

URL_CARDS = 'https://qa-mesto.praktikum-services.ru/api/cards'
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2N2NhYWU4MjRkY2Q5MzAwM2QwZDMxYzYiLCJpYXQiOjE3NDEzMzYyMDcsImV4cCI6MTc0MTk0MTAwN30.q3RENITLr4YUabRaZ7pmXECYYKoKFwtE2YAl4bdN4-A'

card_id = '66cf4c27fe4bf3003d7557e0'  # Убедитесь, что у вас правильный card_id
headers = {'Authorization': TOKEN}

# Добавляем лайк на фото
response_put = requests.put(f"{URL_CARDS}/{card_id}/likes", headers=headers)

if response_put.status_code == 200:
    # Проверяем, если данные есть в 'data' и извлекаем лайки
    data = response_put.json().get('data', [])
    if data:
        likes_after_put = data[0].get('likes', [])
        print("Лайк добавлен. Список лайков после добавления:", likes_after_put)
    else:
        print("Нет данных о карточке.")
else:
    print(f"Ошибка при добавлении лайка: {response_put.status_code}, {response_put.text}")

# Удаляем лайк
response_delete = requests.delete(f"{URL_CARDS}/{card_id}/likes", headers=headers)

if response_delete.status_code == 200:
    # Проверяем, если данные есть в 'data' и извлекаем лайки
    data = response_delete.json().get('data', [])
    if data:
        likes_after_delete = data[0].get('likes', [])
        print("Лайк удален. Список лайков после удаления:", likes_after_delete)
    else:
        print("Нет данных о карточке.")
else:
    print(f"Ошибка при удалении лайка: {response_delete.status_code}, {response_delete.text}")
