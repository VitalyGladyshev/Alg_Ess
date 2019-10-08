import random

array = [random.randint(-100, 100) for _ in range(1000)]
print(array)

num = int(input("Введите число для вставки: "))
pos = int(input("На какую позицию вставить число: "))

# array.append(None)
# i = len(array) - 1
# while i > pos:
#    array[i], array[i - 1] = array[i - 1], array[i]
#    i -= 1

# или

# array.insert(pos, num)

# или

array_new = array[:pos] + [num] + array[pos:]

array[pos] = num
print(array)
