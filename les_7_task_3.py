# ДЗ к Уроку №7 Гладышев ВВ

"""
Задание №3
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
"""

import random
import statistics
from les_7_task_2 import merge_sort

M = 5
size = 2*M + 1
array = [random.randint(0, 100) for _ in range(size)]
# array = [i for i in range(9, -1, -1)]
print(array)

array = merge_sort(array)   # Знаю, что нехорошо, но иначе не успею :(

print(array)

print(f'Медиана с использованием функции median из модуля statistic: {statistics.median(array)}')
print(f'Медиана в отсортированном list: {array[len(array)//2]}')
