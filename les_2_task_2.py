# ДЗ к Уроку №2 Гладышев ВВ

"""
Задание №2

Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def odd_even_digits_count(numb, odd_cnt=0, even_cnt=0):
    remainder = numb % 10
    if remainder % 2:
        odd_cnt += 1
    else:
        even_cnt += 1
    numb //= 10
    if numb > 0:
        odd_cnt, even_cnt = odd_even_digits_count(numb, odd_cnt, even_cnt)
    return odd_cnt, even_cnt


number = float(input("Введите натуральное число: "))
if number <= 0 or number % 1:
    print(f"Число не является натуральным")
else:
    odd_c, even_c = odd_even_digits_count(number)
    print(f"Количество чётных цифр в числе: {even_c} количество нечётных {odd_c}")
