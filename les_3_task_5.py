# ДЗ к Уроку №3 Гладышев ВВ

"""
Задание №5

В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

import random

max_min = -100

list_r = [random.randint(max_min, 100) for _ in range(15)]
print(list_r)

for el in list_r:
    if 0 > el > max_min:
        max_min = el

print(max_min)
