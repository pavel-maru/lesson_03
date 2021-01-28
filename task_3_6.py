
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = MAX_ITEM
max_ = MIN_ITEM
i_min = 0
i_max = 0
sum_ = 0

for i in range(SIZE):
    if array[i] < min_:
        min_ = array[i]
        i_min = i
    if array[i] > max_:
        max_ = array[i]
        i_max = i

if i_min > i_max:
    i_max, i_min = i_min, i_max

print(f'{min_=}, {max_=}')
print(array[(i_min + 1):i_max])
for item in array[(i_min + 1):i_max]:
    sum_ += item

print(f'{sum_=}')
