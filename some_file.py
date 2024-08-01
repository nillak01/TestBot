def test_fun(number: int  | float = 1, name: str='Ivan') -> str:
    name = name.capitalize()
    print(f"Good test number:{number} \nDear {name} XD")
    return "Sucsessful"

def another_some_function(number: int | float | complex=0) -> None:
    pass

print("Hellow my dear friend")
print(test_fun(name="Vlad"))
