
# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
# каждому из чисел в диапазоне от 2 до 9.

MIN = 2
MAX = 99
MIN2 = 2
MAX2 = 9

# num2 = [2, 3, 4, 5, 6, 7, 8, 9]
for num2 in range(MIN2, MAX2 + 1):
    # print(num2)
    count = 0
    for num in range(MIN, MAX + 1):
        # print(num)
        if num % num2 == 0:
            count += 1
            # print(num, num2)

    print(f'В диапазоне от {MIN} до {MAX} на {num2} делится {count} чисел.')
