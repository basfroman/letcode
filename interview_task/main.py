"""
Есть array содержащий id ['99', 'A1bb100', '100', 'С99' , 'A1bb99x' , 'А2']
Надо отсортировать так, чтобы сначала были цифры в порядке увеличения, потом буквы + цифры тоже in ascending order.
В итоге должно получиться:
Array ('99', '100', 'A1', 'A1bb99x', 'A1bb100' , 'A2', 'C99' и т.п)
"""

import re
from functools import cmp_to_key


def sort_key(key):
    # долго не мог понять почему не работает findall, потом почитал как работает использование своей функции к ключу
    # реально так и не понял до конца, но когда использовал сплит заработало)))
    # arr = re.findall(r"(['a-z]+|[0-9]+)", key, flags=re.I)
    arr = re.split(r'([0-9]+)', key)
    # print(arr)
    return [int(string) if string.isdigit() else string for string in arr]


def sort_array(arr: list):
    arr_nums = []
    arr_strs = []

    for item in arr:
        if item.isdigit():
            arr_nums.append(item)
        else:
            arr_strs.append(item)
    arr_nums.sort(key=int)
    arr_strs.sort(key=sort_key)
    return arr_nums + arr_strs


if __name__ == "__main__":
    random_array = ['1000', '99', 'B1', '991', 'A1bb100', 'a1', 'C2', 'A201', '100', 'C99', 'A1bb99x', 'A2', '100a2c34', '1A2C34', '1', 'a1bb99x']
    print(sort_array(random_array))

