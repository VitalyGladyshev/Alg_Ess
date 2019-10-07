# ДЗ к Уроку №3 Гладышев ВВ

"""
Задание №4

Определить, какое число в массиве встречается чаще всего.
"""

import random

list_r = [random.randint(0, 7) for _ in range(35)]

print(list_r)

numbers = {}
for num in frozenset(list_r):
    numbers[num] = 0

for el in list_r:
    numbers[el] += 1

print(numbers)

el_max = 0
key_max = 0
for key, val in numbers.items():
    if val > el_max:
        el_max = val
        key_max = key

print(f"Элемент: {key_max} количество: {el_max}")
