# ДЗ к Уроку №3 Гладышев ВВ

"""
Задание №2

Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5, если индексация
начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""

import random

list_1 = [random.randint(0, 100) for _ in range(20)]

list_2 = [i for i in list_1 if i % 2 == 0]

print(list_1, "\n", list_2)
