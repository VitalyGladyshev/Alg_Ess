# ДЗ к Уроку №7 Гладышев ВВ

"""
Задание №2
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge_sort(s_arr, i_beg=0, i_end=None):
    if i_end is None:
        i_end = len(s_arr)-1
    if i_end - i_beg > 1:
        delta = (i_end - i_beg) // 2
        # print(f'merge_sort 1 i_beg: {i_beg},  i_beg+delta: {i_beg+delta}')
        t_arr_1 = merge_sort(s_arr, i_beg, i_beg+delta)
        # print(f'merge_sort 2 i_beg+delta+1: {i_beg+delta+1},  i_end: {i_end}')
        t_arr_2 = merge_sort(s_arr, i_beg+delta+1, i_end)
        # print("1: ", t_arr_1)
        # print("2: ", t_arr_2)
        res_arr = []
        while True:
            if not len(t_arr_1):
                res_arr.extend(t_arr_2)
                return res_arr
            if not len(t_arr_2):
                res_arr.extend(t_arr_1)
                return res_arr
            if t_arr_1[0] < t_arr_2[0]:
                res_arr.append(t_arr_1.pop(0))
            else:
                res_arr.append(t_arr_2.pop(0))
        return res_arr
    else:
        t_arr = []
        if i_end == i_beg:
            t_arr.append(s_arr[i_beg])
            return t_arr
        elif s_arr[i_end] > s_arr[i_beg]:
            t_arr.append(s_arr[i_beg])
            t_arr.append(s_arr[i_end])
            return t_arr
        else:
            t_arr.append(s_arr[i_end])
            t_arr.append(s_arr[i_beg])
            return t_arr


if __name__ == "__main__":
    size = 10
    array = [random.randint(0, 49) for _ in range(size)]
    # array = [i for i in range(9, -1, -1)]

    print(array)

    print(merge_sort(array))
