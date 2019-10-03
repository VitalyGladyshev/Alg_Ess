# ДЗ к Уроку №2 Гладышев ВВ

"""
Задание №4

Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.
"""


def reverse_number(numb, el=1):
    ser_s = 0
    print(f"{el}")
    numb -= 1
    if numb > 0:
        ser_s = reverse_number(numb, el/-2)
    return ser_s + el


number = int(input("Введите количество элементов ряда: "))
if number <= 0:
    print(f"Число должно быть больше нуля")
else:
    ser_sum = reverse_number(number)
    print(f"Сумма элементов ряда: {ser_sum}")
