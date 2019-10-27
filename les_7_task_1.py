# ДЗ к Уроку №7 Гладышев ВВ

"""
Задание №1
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
"""

import random

size = 10
array = [random.randint(-100, 99) for _ in range(size)]
# random.shuffle(array)
# array = [i for i in range(9, -1, -1)]
print(array)


def bubble_sort(arr):
    n = 1
    print(n, end="")
    while n < len(arr):
        change = False
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
        if not change:
            return arr
        n += 1
        print(f', {n}', end="")
        # print(arr)
    return arr


print("\n", bubble_sort(array))
