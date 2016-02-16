import json, requests

#адрес для отправки json-запросов
url = 'https://api.direct.yandex.ru/v4/json/'

#данные для OAuth-авторизации
token = 'e4d3b4d2a7444fa384a18cda5cd1c8d9'

#логин в Директе
login = 'agrom'

#структура входных данных (словарь)
data = {
   'method': 'GetClientInfo',
   'token': token,
   'locale': 'ru',
   'param': [login]
}


ph_data = {
   'method': '',
   'GeoID': [213]
}

data={
   "method": "CreateNewWordstatReport",
   'token': token,
   'locale': 'ru',   'Phrases': [u'пух -винни',u'синтепон'],
   "param": {
      "Phrases": [
          "малако",
          "яйко"
      ]
   }
}

jdata = json.dumps(data, ensure_ascii=False).encode('utf8')

#выполнить запрос
response = requests.post(url,data=jdata)

#вывести результат
print (response.text) # .decode('utf8'))
