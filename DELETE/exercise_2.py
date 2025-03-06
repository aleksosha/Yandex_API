import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2N2M5OWM2ZGQ3MjkyYTAwM2RmMjkxNzMiLCJpYXQiOjE3NDEyNjYxMDQsImV4cCI6MTc0MTg3MDkwNH0.CR80dPmouMh2ehK2ta4XaJXNdLPpVWTKfswayIHy6tk"
card_id = "66cf4c27fe4bf3003d7557e0"

url = f"https://qa-mesto.praktikum-services.ru/api/cards/{card_id}/likes"
headers = {"Authorization": f"Bearer {token}"}

response_put = requests.put(url, headers=headers)
print(response_put.status_code)
print(response_put.json().get("likes", []))

response_del = requests.delete(url, headers=headers)
print(response_del.status_code)
print(response_del.json().get("likes", []))
