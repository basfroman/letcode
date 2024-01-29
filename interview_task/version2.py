import re
from functools import cmp_to_key


def compare_element(item1, item2):
    if item1.isdigit() and not item2.isdigit():
        return -1
    elif not item1.isdigit() and item2.isdigit():
        return 1
    elif item1.isdigit():
        return int(item1) - int(item2)
    elif item1 > item2:
        return 1
    elif item1 < item2:
        return -1
    return 0


def compare(item1, item2):
    arr1 = re.findall(r'([a-z]+|[0-9]+)', item1, flags=re.I)
    arr2 = re.findall(r'([a-z]+|[0-9]+)', item2, flags=re.I)
    minLen = min(len(arr1), len(arr2))

    result = ()
    for i in range(minLen):
        result = compare_element(arr1[i].lower(), arr2[i].lower())
        if result != 0:
            break
    if result == 0:
        if len(arr1) < len(arr2):
            return -1
        elif len(arr1) > len(arr2):
            return 1

    return result


if __name__ == "__main__":
     random_array = ['1000', '99', 'B1', '991', 'A1bb100', 'A1', 'C2', 'A201', '100', 'C99', 'A1bb99x', 'A2', '1a2c34', '1A2C34']
     random_array.sort(key=cmp_to_key(compare))
     print(random_array)
