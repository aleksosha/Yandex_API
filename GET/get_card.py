import requests
from Locators.locators import TOKEN, URL_CARDS

#пишем функцию
def test_status_code():
    response = requests.get(URL_CARDS, headers={'Authorization': TOKEN})
    print(response.status_code)
    assert response.status_code == 200

test_status_code()