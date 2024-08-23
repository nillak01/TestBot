from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType, UserProfilePhotos
from aiogram import F

from config import BOT_TOKEN, API_CATS_URL, API_DOG_URL, API_FOX_URL
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
        '/dog - для картнки песика\n'
        '/fox - для картнки лисички\n'
    )


# Этот хэндлер будет срабатывать на команду "/cat"
# @dp.message(Command(commands=["cat"]))
async def process_cat_command(message: Message, bot: Bot):
    cat_response = requests.get(API_CATS_URL)
    if cat_response.status_code == 200:
        cat_link = cat_response.json()[0]['url']
        await bot.send_photo(message.chat.id, cat_link)
    else:
        await bot.send_message(message.chat.id,
                               text='Тут должен был быть котейка :()')


# Этот хэндлер будет срабатывать на команду "/dog"
# @dp.message(Command(commands=["dog"]))
async def process_dog_command(message: Message, bot: Bot):
    dog_response = requests.get(API_DOG_URL)
    if dog_response.status_code == 200:
        dog_link = dog_response.json()['url']
        await bot.send_photo(message.chat.id, dog_link)
    else:
        await bot.send_message(message.chat.id,
                               text='Тут должен был быть песик :()')


# Этот хэндлер будет срабатывать на команду "/fox"
# @dp.message(Command(commands=["fox"]))
async def process_fox_command(message: Message, bot: Bot):
    # send_photo_command(
    #     message=message, bot=bot, API_STR=API_FOX_URL, setting="image")
    fox_response = requests.get(API_FOX_URL)
    if fox_response.status_code == 200:
        fox_link = fox_response.json()["image"]
        await bot.send_photo(message.chat.id, fox_link)
    else:
        await bot.send_message(message.chat.id,
                               text='Тут должна был быть лисичка :()')

# Функция не работает
# def send_photo_command(
#         message: Message, bot: Bot, API_STR: str, setting: str
#         ):
#     response = requests.get(API_STR)
#     if response.status_code == 200:
#         link = response.json()[setting]
#         bot.send_photo(message.chat.id, link)
#     else:
#         bot.send_message(
#             message.chat.id, text='Тут должна была быть картинка :()')


# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    # print(message)
    await message.reply_photo(message.photo[0].file_id)


# Этот хендлер пересылает стикеры
async def send_sticker_echo(message: Message):
    # print(message)
    # if message.sticker:
    await message.answer_sticker(message.sticker.file_id)
    # else:
    #     print(message.sticker)


# # Этот хендлер пересылает gif
async def send_gif_echo(message: Message):
    # print(message)
    await message.answer_animation(message.animation.file_id)


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# @dp.message()
async def send_echo(message: Message):
    # print(message)

    # print(message.model_dump_json(indent=4, exclude_none=True))
    text_m = ''
    user_profile_photo: UserProfilePhotos = await bot.get_user_profile_photos(
        message.from_user.id)
    if len(user_profile_photo.photos[0]) > 0:
        await bot.send_photo(chat_id=637603487,
                             photo=user_profile_photo.photos[0][0].file_id)
    else:
        text_m = 'У пользователя нет фото в профиле.\n'
    text_m += f'''{message.date}\n
    {message.from_user.full_name}\n
    is Bot?={message.from_user.is_bot}\n
    login={message.from_user.username}
    user_id={message.from_user.id}
    text={message.text}'''
    await bot.send_message(chat_id=637603487,
                           text=text_m)
    await message.reply(
        text=message.text)


# Этот хэндлер будет срабатывать на любые ваши сообщения
# он пересылает почти любые сообщения заменяя почти весь код выше
# @dp.message()
# async def send_echo(message: Message):
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(
#             text='Данный тип апдейтов не поддерживается '
#                  'методом send_copy'
#         )


# Тут мы регестрируем наши хендлеры
# То же самое если обратить в декоратор @dp.message()
dp.message.register(process_cat_command, Command(commands='cat'))
dp.message.register(process_dog_command, Command(commands='dog'))
dp.message.register(process_fox_command, Command(commands='fox'))
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_sticker_echo, F.content_type == ContentType.STICKER)
dp.message.register(send_gif_echo, F.content_type == ContentType.ANIMATION)
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)
