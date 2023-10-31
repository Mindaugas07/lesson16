# # 1. Create at least 5 different functions by your own and test it

# def make_a_list(text: str) -> list:
#     try:
#         return [sign for sign in text]
#     except TypeError:
#         print("Not the string! ")
    

# print(make_a_list("5"))
# def reverse_string(text: str) -> str:
#     return text[::-1]

# def count_length_string(text: str) -> int:
#     return len(text)

# def is_divided_by_three(number: int) -> bool:
#     return number % 3 == 0

# def what_type(varable) -> type:
#     return type(varable)


# Write a Python program that prompts the user to input an integer and raises a ValueError exception
# if the input is not a valid integer.
# exception ValueError:
# Raised when an operation or function receives an argument that has the right type but an inappropriate value,
# and the situation is not described by a more precise exception such as IndexError.


# from typing import Optional


# def user_input_integer() -> Optional[int]:
#     user_input = input("Please enter an integer: ")
#     try:
#         print(f"Bravo, you entered integer {int(user_input)}")
#     except ValueError:
#         print("Not the integer!")

# user_input_integer()

# Create a mini python program which would take two numbers as an input and would return
# their sum, subtraction, division, multiplication. Handle all possible errors that may occur.

# def oparations_with_two_numbers(nuber_one: int, number_two: int) -> int:

# write a function called calculate, function accepts sign as string, and two variables as integers.
# Do the calculation between two numbers according to sign and return result Handle all possible errors that may occur.

# def calculate(sign: str, number_one: int, number_two: int) -> int:
#     if sign not in "+-/*":
#         raise ValueError("You entered incorrect sign, please use '+', '-', '*' or '/' ")
#     if type(number_one) is not int and type(number_two) is not int:
#         raise TypeError("Please enter two integers ")
#     if sign == "/" and number_two == 0:
#         raise ZeroDivisionError("You can't divide with 0 ")
#     if sign == "+":
#             result = number_one + number_two
#     if sign == "-":
#             result = number_one - number_two
#     if sign == "*":
#             result = number_one * number_two
#     if sign == "/":
#             result = number_one / number_two
    
#     return result


# # print(calculate())

# try:
#       print(calculate("+", r, 8))
# except TypeError:
#       print("You entered incorrect sign, please use '+', '-', '*' or '/' ")
# except ValueError as e:
#       print(e.args)
# except ZeroDivisionError:
#       print("You can't divide with 0")

# import calc as calculator

# a = 10
# b = 20

# result = calculator.add(a, b)

# print(result)

# from echo import echo

# print(f"main name is {__name__}")

# from stringsai import string_to_capital_letters as capitalize
# from lists import list_to_string
# from numbers_ import print_number_1000_times
# from webcam import show_webcam

# # print(capitalize("afsdafsdf"))
# # print(list_to_string([4, 8, 7]))
# # print(print_number_1000_times(5))

# show_webcam()

import logging, time

# logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# input_information = input("Enter something:\n")
# logging.info(f"The input was {input_information}")
from typing import List

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

# def move_to_end(list_of_elements: List[int], element: int) -> list:
#     for some_element in list_of_elements:
#         if some_element == element:
#             list_of_elements.append(list_of_elements.pop(list_of_elements.index(some_element)))
#     logging.info(f"The input was {list_of_elements} and {element}, the result was {list_of_elements}")
#     return list_of_elements



# move_to_end([1, 1, 5, 1, 7, 78], 1)

def consume_gas_level(starting_level: int = 50, engine_running: bool = False) -> int:
    if engine_running:
        logging.debug(f"After consuming gas there is left {starting_level}")
        return starting_level - 5
    else:
        logging.critical("Car can't consume gas while the engine is turned off!")
        raise ValueError("Engine is not running, can't consume gas!")
    

def car_toggle_switch(state: bool=False) -> bool:
    if state == True:
        logging.debug("Car was turned on!")
        print("Engine is running!")
    else:
        logging.debug("Car was turned off!")
        print("Engine is not running!")
    return state
    

def drive() -> None:
    car_state = car_toggle_switch(True)
    gas_level = 80
    logging.debug(f"Car was turned on with {gas_level} L of gas ")
    while gas_level > 0:
        message = f"Wroom wroom I have {gas_level} Litres in tank"
        gas_level = consume_gas_level(gas_level, car_state)
        print(message)
        time.sleep(1)
    print("I ran out of gass..")
    car_state = car_toggle_switch()


drive()
