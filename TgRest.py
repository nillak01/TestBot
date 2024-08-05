import requests
import time
from config import BOT_TOKEN


API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
ERROR_TEXT = "Тут должен был быть котик :(())"
TEXT = 'Купи слона'
MAX_COUNTER = 200

offset = -2
counter = 0
cat_response: requests.Response
cat_link: str
chat_id: int


while counter < MAX_COUNTER:

    # Чтобы видеть в консоли, что код живет
    print('attempt =', counter)

    updates = requests.get(
        f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    cat_url = requests.get(API_CATS_URL).json()
    print(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}')

    if updates['result']:
        for result in updates['result']:
            # Получаем ID чата с пользователем
            chat_id = result['message']['from']['id']
            offset = result['update_id']
            chat_id = result['message']['from']['id']

            messege_1 = result['message']['text']
            TEXT = f'Все говорят: {messege_1} \nА ты лучше на котеек посмотри'
            # mess1 = f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}'
            # requests.get(mess1)
            # print(mess1)

            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(
                    f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
                requests.get(
                    f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
                print(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(
                    f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(10)
    counter += 1
