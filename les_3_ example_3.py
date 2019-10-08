import random

array = [random.randint(-100, 100) for _ in range(1000)]
print(array)

arr_below = []
arr_large = []

for item in array:

    if item > 0:
        arr_large.append(item)
    elif item < 0:
        arr_below.append(item)

print(arr_below)
print(arr_large)

# Второй вариант. Он хуже, т.к. два обхода массива
arr_below1 = [item for item in array if item < 0]
arr_large1 = [item for item in array if item > 0]

print(arr_below1)
print(arr_large1)
