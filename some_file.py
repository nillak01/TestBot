from typing import Literal


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
