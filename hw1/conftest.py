import pytest
import requests
import yaml

with open('config.yaml') as file:
    my_dict = yaml.safe_load(file)

url = my_dict['url']
url1 = my_dict['url1']

username = my_dict['username']
password = my_dict['password']


@pytest.fixture()
def login():
    response = requests.post(url=url, data={'username': username, 'password': password})

    #проверяем успешность запроса
    assert response.status_code == 200, f"Login request failed with status code {response.status_code}"

    try:
        #пытаемся извлечь токен из JSON-ответа
        token = response.json()['token']
        return token
    except KeyError:
        #если ключ 'token' отсутствует, выводим сообщение об ошибке
        raise KeyError("Token not found in the response JSON")
