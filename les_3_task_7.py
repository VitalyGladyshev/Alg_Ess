# ДЗ к Уроку №3 Гладышев ВВ

"""
Задание №7

В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import random

list_r = [random.randint(-10, 10) for _ in range(20)]
print(list_r)

min_1 = list_r[0]
min_2 = list_r[1]
if min_1 > min_2:
    min_1, min_2 = min_2, min_1

for el in list_r[2:]:
    if el < min_2:
        if el <= min_1:
            min_2 = min_1
            min_1 = el
        else:
            min_2 = el

print(f"Первый наименьший: {min_1} второй наименьший: {min_2}")
