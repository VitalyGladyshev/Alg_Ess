# ДЗ к Уроку №1 Гладышев ВВ

"""
Задание №5

Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

letter = ord(input("Введите букву алфавита: "))

if letter in range(65, 90+1):
    num = letter - 64
elif letter in range(97, 122+1):
    num = letter - 96

# Не определяем букву ё(Ё)
elif letter in range(1072, 1103+1):
    num = letter - 1071
elif letter in range(1040, 1071+1):
    num = letter - 1039
else:
    print("Неизвестный символ")
    exit()
print(f"Номер в алфавите: {num}")
