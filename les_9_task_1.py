# ДЗ к Уроку №9 Гладышев ВВ

"""
Задание №1
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
"""

import hashlib


def sub_string(str_in: str, str_len=-1, str_cnt=0) -> int:
    if str_len == -1:
        str_len = len(str_in) - 1
    full_len = len(str_in)
    hash_list = []

    for ind in range(full_len - str_len + 1):
        print(f'Подстрока: {str_in[ind:ind + str_len]}')
        sub_str_hash = hashlib.sha1(str_in[ind:ind + str_len].encode('utf-8')).hexdigest()
        if sub_str_hash not in hash_list:
            hash_list.append(sub_str_hash)
            str_cnt += 1
            print(f'hash: {sub_str_hash} str_cnt: {str_cnt}')

    if str_len-1 > 0:
        str_cnt = sub_string(str_in, str_len-1, str_cnt)
    return str_cnt


str_inc = input('Введите строку: ')

print(f'Количество уникальных подстрок: {sub_string(str_inc)}')
