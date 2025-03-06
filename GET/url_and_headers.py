#Задание на вывод кода ответа и содержимаого

import requests

response = requests.get(
    'https://qa-mesto.praktikum-services.ru/api/users/me',
    headers={'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2N2M5ODVjNmQ3MjkyYTAwM2RmMjkxNmMiLCJpYXQiOjE3NDEyNjAyMzAsImV4cCI6MTc0MTg2NTAzMH0.tubkBqJ6wGbhpwscjdJezgyfSlfCm5vKnFgsR0SZ9aY'}
)

assert response.status_code == 200

print(response.status_code)
print(f"Тело ответа: {response.text}")
