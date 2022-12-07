"""
Есть array содержащий id ['99', 'A1bb100', '100', 'С99' , 'A1bb99x' , 'А2']
Надо отсортировать так, чтобы сначала были цифры в порядке увеличения, потом буквы + цифры тоже in ascending order.
В итоге должно получиться:
Array ('99', '100', 'A1', 'A1bb99x', 'A1bb100' , 'A2', 'C99' и т.п)
"""

import re


def sort_key(key):
    if key.isdigit():
        return ['', int(key), '']

    arr = re.split(r'([0-9]+)', key)
    return ['_'] + [int(string) if string.isdigit() else string for string in arr]


def sort_array(arr: list):
    arr.sort(key=sort_key)
    return arr


if __name__ == "__main__":
    random_array = ['1000', '99', 'B1', '991', 'A1bb100', 'a1', 'C2', 'A201', '100', 'C99', 'A1bb99x', 'A2', '100a2c34', '1A2C34', '1', 'a1bb99x']
    print(sort_array(random_array))

