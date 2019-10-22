# ДЗ к Уроку №6 Гладышев ВВ

"""
Задание №1
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Урок 3 Задание №7

В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

import sys
import random

list_r = [random.randint(-10, 10) for _ in range(20)]


def two_min_in_list_1(list_v1):
    min_1 = list_v1[0]
    min_2 = list_v1[1]
    if min_1 > min_2:
        min_1, min_2 = min_2, min_1

    for el in list_v1[2:]:
        if el < min_2:
            if el <= min_1:
                min_2 = min_1
                min_1 = el
            else:
                min_2 = el

    total_size = show_size(list_v1)
    total_size += show_size(min_1)
    total_size += show_size(min_2)
    print(f'total_size: {total_size}')
    return min_1, min_2


def two_min_in_list_2(list_v2):
    min_1 = list_v2[0]
    for el in list_v2[1:]:
        if el < min_1:
            min_1 = el

    list_v2.remove(min_1)
    min_2 = list_v2[0]
    for el in list_v2[1:]:
        if el < min_2:
            min_2 = el

    total_size = show_size(list_v2)
    total_size += show_size(min_1)
    total_size += show_size(min_2)
    print(f'total_size: {total_size}')
    return min_1, min_2


def two_min_in_list_3(list_v3):
    min_1 = min(list_v3)
    list_v3.remove(min_1)
    min_2 = min(list_v3)

    total_size = show_size(list_v3)
    total_size += show_size(min_1)
    total_size += show_size(min_2)
    print(f'total_size: {total_size}')
    return min_1, min_2


def show_size(x, t_size=0, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')
    t_size += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                t_size = show_size(xx, t_size, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                t_size = show_size(xx, t_size, level + 1)
    # if level == 0:
        # print(f'total_size: {t_size}')
    return t_size


if __name__ == "__main__":
    print(sys.version, sys.platform)
# 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] win32
    print(list_r)
    print(f'total_size: {show_size(list_r)}')
    print("\t1 Поиск за один проход")
    v1_1, v1_2 = two_min_in_list_1(list_r[:])
    print(f"Первый наименьший: {v1_1} второй наименьший: {v1_2}")
    print("\t2 Поиск за два прохода")
    v2_1, v2_2 = two_min_in_list_2(list_r[:])
    print(f"Первый наименьший: {v2_1} второй наименьший: {v2_2}")
    print("\t3 Поиск функциями Python")
    v3_1, v3_2 = two_min_in_list_3(list_r[:])
    print(f"Первый наименьший: {v3_1} второй наименьший: {v3_2}")

# В варианте "Поиск за один проход" использовано 422 байт
# В варианте "Поиск за два прохода" использовано 408 байт
# В варианте "Поиск функциями Python" использовано 408 байт
