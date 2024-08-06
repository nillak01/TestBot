import requests


api_url = 'http://numbersapi.com/43'

# Отправляем GET-запрос и сохраняем ответ в переменной response
response = requests.get(api_url)

# Если код ответа на запрос - 200, то смотрим, что пришло в ответе
if response.status_code == 200:
    print(response.text)
# При другом коде ответа выводим этот код
else:
    print(response.status_code)
