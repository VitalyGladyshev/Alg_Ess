# ДЗ к Уроку №3 Гладышев ВВ

"""
Задание №6

В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

list_r = [random.randint(-100, 100) for _ in range(20)]
print(list_r)

below_b = int(input("Задайте нижнюю границу:"))
if below_b > len(list_r):
    below_b = len(list_r)
below_b -= 1
if below_b < 0:
    below_b = 0
above_b = int(input("Задайте верхнюю границу:"))
if above_b > len(list_r):
    above_b = len(list_r)
above_b -= 1
if above_b < 0:
    above_b = 0

if below_b > above_b:
    below_b, above_b = above_b, below_b

sum_el = 0
for el in list_r[below_b + 1: above_b]:
    sum_el += el

print(sum_el)
