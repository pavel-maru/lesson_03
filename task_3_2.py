
# 2. Во втором массиве сохранить индексы чётных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо
# заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят чётные числа.

import random

SIZE = 10_000
MIN_ITEM = 0
MAX_ITEM = 1_000_000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

arr_index = []

for i in range(SIZE):
    if array[i] % 2 == 0:
        arr_index.append(i)

print(arr_index)
