# ДЗ к Уроку №2 Гладышев ВВ

"""
Задание №1

Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся
пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит
неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
"""

while True:
    number_1 = float(input("Введите первое число: "))
    number_2 = float(input("Введите второе число: "))
    while True:
        operation = input("Введите знак операции: ")
        if operation == '0':
            exit()
        elif operation == '+':
            print(f"{number_1} {operation} {number_2} = {number_1 + number_2}")
            break
        elif operation == '-':
            print(f"{number_1} {operation} {number_2} = {number_1 - number_2}")
            break
        elif operation == '*':
            print(f"{number_1} {operation} {number_2} = {number_1 * number_2}")
            break
        elif operation == '/':
            if number_2 != 0:
                print(f"{number_1} {operation} {number_2} = {number_1 / number_2}")
                break
            else:
                print(f"Деление на ноль не поддерживается. Повторите ввод")
                break
        else:
            print(f"Данная операция не интерпретирована. Повторите ввод")
