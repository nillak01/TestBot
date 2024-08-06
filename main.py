from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN
from config import API_CATS_URL
from config import API_DOG_URL
from config import API_FOX_URL
import requests


# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Я бот который может отправлять тебе разные картиночки\n'
        '/cat - для картнки котейки\n'
        '/dog - для картнки котейки\n'
        '/fox - для картнки котейки\n'
    )


# Этот хэндлер будет срабатывать на команду "/cat"
@dp.message(Command(commands=["cat"]))
async def process_cat_command(message: Message, bot: Bot):
    cat_response = requests.get(API_CATS_URL)
    if cat_response.status_code == 200:
        cat_link = cat_response.json()[0]['url']
        await bot.send_photo(message.chat.id, cat_link)
    else:
        await bot.send_message(message.chat.id,
                               text='Тут должен был быть котейка :()')


# Этот хэндлер будет срабатывать на команду "/dog"
@dp.message(Command(commands=["dog"]))
async def process_dog_command(message: Message, bot: Bot):
    dog_response = requests.get(API_DOG_URL)
    if dog_response.status_code == 200:
        dog_link = dog_response.json()['url']
        await bot.send_photo(message.chat.id, dog_link)
    else:
        await bot.send_message(message.chat.id,
                               text='Тут должен был быть песик :()')


# Этот хэндлер будет срабатывать на команду "/fox"
@dp.message(Command(commands=["fox"]))
async def process_fox_command(message: Message, bot: Bot):
    fox_response = requests.get(API_FOX_URL)
    if fox_response.status_code == 200:
        fox_link = fox_response.json()["image"]
        await bot.send_photo(message.chat.id, fox_link)
    else:
        await bot.send_message(message.chat.id,
                               text='Тут должна был быть лисичка :()')


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    dp.run_polling(bot)
