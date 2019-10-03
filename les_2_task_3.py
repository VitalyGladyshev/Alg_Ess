# ДЗ к Уроку №2 Гладышев ВВ

"""
Задание №3

Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843.
"""


def reverse_number(numb):
    rev_num = ""
    remainder = numb % 10
    numb //= 10
    if numb > 0:
        rev_num = reverse_number(numb)
    return str(remainder) + rev_num


number = int(input("Введите натуральное число: "))
if number <= 0:
    print(f"Число не является натуральным")
else:
    rev_number = reverse_number(number)
    print(f"Вы ввели число: {number} число с обратным порядком цифр {rev_number}")
