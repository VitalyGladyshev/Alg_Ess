# ДЗ к Уроку №4 Гладышев ВВ

"""
Задание №2

Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
"""

import math
# import timeit
# import cProfile


def sieve(num):
    pr_number = 2
    pr_cnt = 1
    pr_lst = [2]
    while True:
        if pr_cnt == num:
            return pr_number
        pr_number += 1
        b_prime = True
        border = math.sqrt(pr_number)//1 + 1
        for i in pr_lst:
            if i > border:
                break
            if not pr_number % i:
                b_prime = False
                break
        if b_prime:
            pr_cnt += 1
            pr_lst.append(pr_number)


def prime(num):
    pr_number = 2
    pr_cnt = 1
    while True:
        if pr_cnt == num:
            return pr_number
        pr_number += 1
        b_prime = True
        for i in range(2, int(math.sqrt(pr_number)//1 + 2)):
            if not pr_number % i:
                b_prime = False
                break
        if b_prime:
            pr_cnt += 1


# cProfile.run('sieve(100000)')
# exit(0)

if __name__ == "__main__":
    number = str(input("Задайте номер простого числа: "))
    if number.isdigit():
        number = int(number)
    else:
        print("Некорректный ввод!")
        exit(0)
    print("1 Алгоритм \"Решето Эратосфена\"")
    print("2 Без использования \"Решета Эратосфена\"")
    alg = str(input("Выберите алгоритм: "))
    if alg == '1':
        print(f'Номер числа: {number} Простое число: {sieve(number)}')
    elif alg == '2':
        print(f'Номер числа: {number} Простое число: {prime(number)}')
    else:
        print("Некорректный ввод!")

# c:\Projects\Alg_Ess>python -m timeit -n 6 -s "import les_4_task_2" "les_4_task_2.sieve(100000)"
# 6 loops, best of 5: 3.54 sec per loop

# c:\Projects\Alg_Ess>python -m timeit -n 6 -s "import les_4_task_2" "les_4_task_2.prime(100000)"
# 6 loops, best of 5: 10.6 sec per loop

# cProfile.run('sieve(100000)')
# C:\Users\Лариса\venv\Scripts\python.exe C:/Projects/Alg_Ess/les_4_task_2.py
#          1399710 function calls in 3.759 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    3.759    3.759 <string>:1(<module>)
#         1    3.514    3.514    3.758    3.758 les_4_task_2.py:19(sieve)
#         1    0.000    0.000    3.759    3.759 {built-in method builtins.exec}
#   1299707    0.236    0.000    0.236    0.000 {built-in method math.sqrt}
#     99999    0.008    0.000    0.008    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime(100000)')
# C:\Users\Лариса\venv\Scripts\python.exe C:/Projects/Alg_Ess/les_4_task_2.py
#          1299711 function calls in 10.783 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   10.783   10.783 <string>:1(<module>)
#         1   10.549   10.549   10.783   10.783 les_4_task_2.py:40(prime)
#         1    0.000    0.000   10.783   10.783 {built-in method builtins.exec}
#   1299707    0.234    0.000    0.234    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
