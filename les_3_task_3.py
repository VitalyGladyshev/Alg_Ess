# ДЗ к Уроку №3 Гладышев ВВ

"""
Задание №3

В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random

list_r = [random.randint(-100, 100) for _ in range(10)]

min_p = 0
max_p = 0

print(list_r)

for ind, val in enumerate(list_r):
    if val > list_r[max_p]:
        max_p = ind
    if val < list_r[min_p]:
        min_p = ind

list_r[max_p], list_r[min_p] = list_r[min_p], list_r[max_p]
print(list_r)
