
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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

for i in range(SIZE):
    if array[i] < min_:
        min_ = array[i]
        i_min = i
        # print(f'{min_=}, {i_min=}')
    if array[i] > max_:
        max_ = array[i]
        i_max = i
        # print(f'{max_=}, {i_max=}')

array[i_min] = max_
array[i_max] = min_
print(array)
