# С использованием фреймворка pytest написать тест операции checkText 
# SOAP API https://speller.yandex.net/services/spellservice?WSDL
# Тест должен использовать DDT и проверять наличие определенного
# верного слова в списке предложенных исправлений к определенному неверному слову.
# Слова должны быть заданы через фикстуры в conftest.py,
# адрес wsdl должен быть вынесен в config.yaml.

# Методы работы с SOAP должны быть вынесены в отдельную библиотеку.
from zeep import Client, Settings
import yaml

with open('config.yaml') as f:
# читаем документ YAML
    data = yaml.safe_load(f)
    wsdl = data['wsdl']

settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings = settings)

def check_works(word: str):
    box = client.service.checkText(word)
    if box:
        return box[0]['s']

    # print(box)

if __name__ == '__main__':
    check_works("Малако")
