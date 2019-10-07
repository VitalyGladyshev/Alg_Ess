# ДЗ к Уроку №2 Гладышев ВВ

"""
Задание №6

В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ.
"""

import random

r_num = random.randint(0, 100)

for i in range(10):
    inp = int(input(f"Попытка {i+1}. Отгадайте число от 0 до 100: "))
    if r_num == inp:
        print(f"Вы угадали!!! :)))")
        break
    elif r_num > inp:
        print(f"Вы не угадали :( Загаданное число больше")
    else:
        print(f"Вы не угадали :( Загаданное число меньше")
print(f"Было загадано число {r_num}")