import random


def bin_search(array, value):
    left = 0
    right = len(array) - 1
    pos = len(array) // 2

    while array[pos] != value and left <= right:

        if value > array[pos]:
            left = pos + 1
        else:
            right = pos - 1

        pos = (left + right) // 2

    return -1 if left > right else pos + 1


a = [random.randint(0, 1000) for _ in range(100)]
a.sort()
print(a)

num = int(input("Какой элемент найти: "))
print(bin_search(a, num))
