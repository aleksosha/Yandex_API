import requests
from Locators.locators import URL, TOKEN
def test_city_name():
    response = requests.get(URL, headers={
        'Authorization': TOKEN})
    r = response.json()
    assert "Москва сити" == r['data'][0]['name']