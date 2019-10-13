# ДЗ к Уроку №4 Гладышев ВВ

"""
Задание №1
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков.

Урок 3 Задание №7

В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

# import timeit
# import cProfile
import random

list_r = [random.randint(-500000, 500000) for _ in range(1000000)]


def two_min_in_list_1():
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
    return min_1, min_2


def two_min_in_list_2():
    min_1 = list_r[0]
    for el in list_r[1:]:
        if el < min_1:
            min_1 = el

    list_r.remove(min_1)
    min_2 = list_r[0]
    for el in list_r[1:]:
        if el < min_2:
            min_2 = el

    return min_1, min_2


def two_min_in_list_3():
    min_1 = min(list_r)
    list_r.remove(min_1)
    min_2 = min(list_r)
    return min_1, min_2


# cProfile.run('two_min_in_list_1()')
# exit(0)

if __name__ == "__main__":
    print(list_r)
    print("\t1 Поиск за один проход")
    print("\t2 Поиск за два прохода")
    print("\t3 Поиск функциями Python")
    alg = str(input("Выберите алгоритм определения двух наименьших элементов в массиве: "))
    if alg == '1':
        m_1, m_2 = two_min_in_list_1()
    elif alg == '2':
        m_1, m_2 = two_min_in_list_2()
    elif alg == '3':
        m_1, m_2 = two_min_in_list_3()
    else:
        print("Некорректный ввод!")
        exit()
    print(f"Первый наименьший: {m_1} второй наименьший: {m_2}")

# 1 Поиск за один проход

# c:\Projects\Alg_Ess>python -m timeit -n 6 -s "import les_4_task_1" "les_4_task_1.two_min_in_list_1()"
# 6 loops, best of 5: 43.7 msec per loop

# C:\Users\Лариса\Les01\Scripts\python.exe C:/Projects/Alg_Ess/les_4_task_1.py
#          4 function calls in 0.052 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.043    0.043 <string>:1(<module>)
#         1    0.043    0.043    0.043    0.043 les_4_task_1.py:21(two_min_in_list_1)
#         1    0.009    0.009    0.052    0.052 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 2 Поиск за два прохода

# c:\Projects\Alg_Ess>python -m timeit -n 6 -s "import les_4_task_1" "les_4_task_1.two_min_in_list_2()"
# 6 loops, best of 5: 95.7 msec per loop

# C:\Users\Лариса\Les01\Scripts\python.exe C:/Projects/Alg_Ess/les_4_task_1.py
#          5 function calls in 0.097 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.088    0.088 <string>:1(<module>)
#         1    0.087    0.087    0.088    0.088 les_4_task_1.py:37(two_min_in_list_2)
#         1    0.009    0.009    0.097    0.097 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.001    0.001    0.001    0.001 {method 'remove' of 'list' objects}

# 3 Поиск функциями Python

# c:\Projects\Alg_Ess>python -m timeit -n 6 -s "import les_4_task_1" "les_4_task_1.two_min_in_list_3()"
# 6 loops, best of 5: 61.9 msec per loop

# C:\Users\Лариса\Les01\Scripts\python.exe C:/Projects/Alg_Ess/les_4_task_1.py
#          7 function calls in 0.070 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.061    0.061 <string>:1(<module>)
#         1    0.000    0.000    0.060    0.060 les_4_task_1.py:52(two_min_in_list_3)
#         1    0.009    0.009    0.070    0.070 {built-in method builtins.exec}
#         2    0.054    0.027    0.054    0.027 {built-in method builtins.min}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.007    0.007    0.007    0.007 {method 'remove' of 'list' objects}

# Вариант 1 - самый быстрый т.к. выполняет только один проход
