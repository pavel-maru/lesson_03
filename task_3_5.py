
# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран
# его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный
# отрицательный». Это два абсолютно разных значения.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

# array = [-86, 85, -40, -54, -16, -94, -63, -26, 11, 2]

max_ = MIN_ITEM
count = 0

for item in array:
    if item < 0:
        count += 1
        if item > max_:
            max_ = item

if count > 0:
    print(f'{max_=}')
else:
    print('В данном массиве нет отрицательных чисел.')
