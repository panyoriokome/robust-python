from typing import Union, Optional, Set

class HotDog:
    pass

class Pretzel:
    pass

def dispense_hot_dog():
    return True

def dispense_pretzel():
    return True 

def print_error_code(err):
    return True

def get_order():
    return True

def dispense_snack(user_input: str) -> Union[HotDog, Pretzel]:
    # Hotdogを返すケース
    if user_input == "Hot Dog":
        return dispense_hot_dog()
    # Pretzelを返すケース
    elif user_input == "Pretzel":
        return dispense_pretzel()
    raise RuntimeError("Should never reach this code,"
                       "as an invalid input has been entered")

# どっちが正しい？
# def place_order() -> Union[HotDog, Pretzel]:
def place_order() -> Optional[Union[HotDog, Pretzel]]:
    order = get_order()
    # dispense_snacllを呼ぶ。返される値としてHotDogかNoneを想定する
    result = dispense_snack(order.name)
    if result is None:
        print_error_code("An error occurred" + result)
        return None
    # Return our HotDog
    return result


# Product and Sum Type
from dataclasses import dataclass

# @dataclass
# class Snack:
#     # 3つの選択肢があるとする
#     name: str
#     # 4つの組み合わせがあるとする
#     condiments: Set[str]
#     # 0から5の6つの選択肢があるとする
#     error_code: int
#     # TrueかFalseの2つの選択肢があるとする
#     disposed_of: bool


# Snack("Hotdog", {"Mustard", "Ketchup"}, 5, False)

# def serve(snack):
#     # error_codeの値をチェックせずにdisposed_ofの値を使う
#     if snack.disposed_of:
#         return
#     # ...

# @dataclass
# class Error:
#     error_code: int
#     disposed_of: bool

# @dataclass
# class Snack:
#     name: str
#     condiments: Set[str]

# snack: Union[Snack, Error] = Snack("Hotdog", {"Mustard", "Ketchup"})
# print(snack) # Snack(name='Hotdog', condiments={'Ketchup', 'Mustard'})

# snack = Error(5, True)
# print(snack) # Error(error_code=5, disposed_of=True)


from typing import Literal

@dataclass
class Error:
    error_code: Literal[1,2,3,4,5]
    disposed_of: bool

@dataclass
class Snack:
    name: Literal["Pretzel", "Hot Dog", "Veggie Burger"]
    condiments: Set[Literal["Mustard", "Ketchup"]]

Error(0, False)
Snack("Invalid", Set())
Snack("Pretzel", {"Mustard", "Relish"})
Snack("Pretzel", {"Mustard"})
Snack("Pretzel", {"Ketchup"})
Snack("Pretzel", {"Mustard", "Ketchup"})
Snack("Pretzel", {None})