from typing import Literal
from dataclasses import dataclass


class User:
    def __init__(self, user_id, name, age, email):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.email = email


# То же самое что и класс выше
@dataclass
class User1:
    user_id: int
    name: str
    age: int
    email: str


@dataclass
class DatabaseConfig:
    db_host: str       # URL-адрес базы данных
    db_user: str       # Username пользователя базы данных
    db_password: str   # Пароль к базе данных
    database: str      # Название базы данных


@dataclass
class TgBot:
    token: str             # Токен для доступа к телеграм-боту
    admin_ids: list[int]   # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def get_user_info(user: User1 | User) -> str:
    return f'Возраст пользователя {user.name} - {user.age}, ' \
           f'а email - {user.email}'


user_2: User = User(15, 'Ivan', 35, 'ivan_pupkin@pochta.ru')
print(get_user_info(user_2))
user_1: User1 = User1(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
print(get_user_info(user_1))


def test_fun(number: int | float = 1, name: str = 'Ivan') -> str:
    name = name.capitalize()
    print(f"Good test number:{number} \nDear {name} XD")
    return "Sucsessful"


def another_some_function(number: int | float | complex = 0) -> None:
    pass


lst_1: list[int]                # Все элементы списка lst_1 типа int
tpl_2: tuple[bool]              # Все элементы кортежа tpl_2 типа bool
tpl_3: tuple[int, bool, float]  # Кортеж tpl_3 состоит из трех элементов
# Первый типа int, второй типа bool, а третий типа float
# Элементы множества set_4 либо int, либо float типов
set_4: set[int | float]

# user: dict[Literal['name'] |
#            Literal['second_name'] |
#            Literal['username'], str] = {}

user: dict[Literal['name', 'second_name', 'username'], str] = {}

user['name'] = 'Male'

print(user)

# print("Hellow my dear friend")
# print(test_fun(name="Vlad"))
