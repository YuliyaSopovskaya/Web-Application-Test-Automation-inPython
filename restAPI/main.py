#  Написать тест с использованием pytest и requests, в котором:
# Адрес сайта, имя пользователя и пароль хранятся в config.yaml
# conftest.py содержит фикстуру авторизации по адресу https://test-stand.gb.ru/gateway/login 
# с передачей параметров “username" и "password" и возвращающей токен авторизации
# Тест с использованием DDT проверяет наличие поста
# с определенным заголовком в списке постов другого пользователя, для этого 
# выполняется get запрос по адресу https://test-stand.gb.ru/api/posts c хедером, содержащим токен авторизации
#  в параметре "X-Auth-Token". Для отображения постов другого пользователя передается "owner": "notMe".
# http://restapi.adequateshop.com/api/authaccount/registration
# http://restapi.adequateshop.com/api/authaccount/login

import requests
import yaml

with open('config.yaml') as file:
 my_dict=yaml.safe_load(file)

url = my_dict['url']
url1 = my_dict['url1']
username = 'GB20230583da08'
password = 'a2382aba8d'

# def login(username, password):
# obj_data = requests.post(url=url, data ={'username':username, 'password':password})
# #print(obj_data.json()) #
# token = obj_data.json()['token']
# #print(token)
# return token

def token_auth(token):
 response=requests.get(url=url1, headers={'X-Auth-Token':token}, params={'owner':"notMe"})
content_var = [item['content'] for item in response.json()['data']]
return content_var

def test_step2(login):
 assert 'content' in token_auth(login)


#if __name__ == '__main__':
# print(token_auth(login(username,password)))
