import requests
from tgData import token


chat_id = 637603487
text = "Привет Ярик, у тебя получилось!"
methodName = 'sendMessage?' + f"chat_id={chat_id}&" + f"text={text}"
api_url = f'https://api.telegram.org/bot{token}/{methodName}'

# Прмер получения API
# https://api.telegram.org/bot<token>/METHOD_NAME
# Отправляем GET-запрос и сохраняем ответ в переменной response
response = requests.get(api_url)

print(api_url)
# Если код ответа на запрос - 200, то смотрим, что пришло в ответе
if response.status_code == 200:
    print(response.text)
# При другом коде ответа выводим этот код
else:
    print(response.status_code)
