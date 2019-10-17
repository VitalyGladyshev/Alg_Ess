from collections import deque
import random

array = [random.randint(-100, 100) for _ in range(10)]
print(array)

deq = deque()

for item in array:
    if item > 0:
        deq.append(item)
    else:
        deq.appendleft(item)

print(deq)

print('*' * 50)
with open('big_log.txt', 'r', encoding='utf-8') as f:
    last_ten = deque(f, 10)

print(last_ten)
