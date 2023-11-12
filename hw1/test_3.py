# Условие: Добавить в 
# задание с REST API ещё один тест, в котором создаётся новый пост, 
# а потом проверяется его наличие на сервере по полю «описание».
# Подсказка: создание поста выполняется запросом к 
# https://test-stand.gb.ru/api/posts с передачей параметров title, description, content.


# import requests
# import pytest
# from conftest import login

# url = "https://test-stand.gb.ru/api/posts"

# def test_create_and_verify_post(login):
#     new_post_data = {
#         'title': 'заголовок поста',
#         'description': 'описание поста',
#         'content': 'cодержание'
#     }
#     headers = {'X-Auth-Token': login}
#     response = requests.post(url=url, json=new_post_data, headers=headers)
#     assert response.status_code == 201

#     # Список постов и проверка наличия нового поста по описанию
#     response = requests.get(url=url, headers=headers, params={'owner': 'username'})
#     content_var = [item['description'] for item in response.json()['data']]
#     assert new_post_data['description'] in content_var

#     # Проверка по полю content
#     assert new_post_data['content'] in content_var


import requests
from conftest import login  # Import the login fixture from conftest

url1 = "https://test-stand.gb.ru/api/posts"


def token_auth(token):
    response = requests.get(url=url1, headers={'X-Auth-Token': token}, params={'owner': "notMe"})

    #поверяем успешность запроса
    assert response.status_code == 200, f"Token Auth request failed with status code {response.status_code}"

    try:
        content_var = [item['content'] for item in response.json()['data']]
        return content_var
    except KeyError:
        #обработка ошибки, если ключ 'content' отсутствует в JSON-ответе
        raise KeyError("Content not found in the response JSON")

def create_post(token):
    #сreate a new post
    data = {
        'title': 'New Post Title',
        'description': 'New Post Description',
        'content': 'New Post Content'
    }
    response = requests.post(url=url1, headers={'X-Auth-Token': token}, data=data)

    #проверяем успешность запроса
    assert response.status_code == 200, f"Create Post request failed with status code {response.status_code}"

    try:
        created_description = response.json()['data']['description']
        return created_description
    except KeyError:
        #обработка ошибки, если ключ 'description' отсутствует в JSON-ответе
        raise KeyError("Description not found in the response JSON")

def test_step2(login):
    created_description = create_post(login)
    content_var = token_auth(login)
    assert created_description in content_var
