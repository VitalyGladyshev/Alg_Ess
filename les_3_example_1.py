# 1. Удаление списка во время его итерирования

list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3, 4]
list_4 = [1, 2, 3, 4]

for i, item in enumerate(list_1):
    del item

print(list_1)

for i, item in enumerate(list_2):
    list_2.remove(item)

print(list_2)

for i, item in enumerate(list_3):
    list_3.pop(i)

print(list_3)

for i, item in enumerate(list_4[:]):
    list_4.remove(item)

print(list_4)

# 2. Крестики-нолики, где Х побеждает с первой попытки

row = [''] * 3
board = [row] * 3
print(board)
board[0][0] = 'X'
print(board)
board = [[''] * 3 for _ in range(3)]
print(board)
board[0][0] = 'X'
print(board)

# 3. Теже операнды, но другая история

a = [1, 2, 3, 4]
b = a
a = a + [5, 6, 7]
print(a, b)

a = [1, 2, 3, 4]
b = a
a += [5, 6, 7]
print(a, b)

# 4. Игла в стоге сена

t = {'one', 'two'}
for i in t:
    print(i)

t = {'one'}
for i in t:
    print(i)

t = {'one', }
for i in t:
    print(i)

# 5. Сохранить только уникальные значения

lst = [1, 5, 6, 1, 6, 2, 4, 5, 1, 6, 5]
lst = list(set(lst))
print(lst)

# 6. Ключ словаря - изменяемый объект

set_x = {1, 2, 3}
lst_x = {4, 5, 6}
# dict_x = {set_x: lst_x}
# dict_x = {lst_x: set_x}
dict_x = {frozenset(set_x): lst_x}
dict_y = {tuple(lst_x): set_x}

print(dict_x)
print(dict_y)
