# 5. В массиве найти максимальный отрицательный элемент. 
# Вывести на экран его значение и позицию в массиве.

import random

list_len = int(input('Введите длину массива: '))
rand_list = [random.randint(-100, 100) for _ in range(list_len)]
print(f'Исходный массив:\n{rand_list}')

max_negative = 0
max_neg_pos = -1

for pos, item in enumerate(rand_list):
    if max_negative == 0 and item < 0:
        max_negative = item
        max_neg_pos = pos
    if item < 0 and item > max_negative:
        max_negative = item
        max_neg_pos = pos

print(f"Максимальный отрицательный элемент '{max_negative}', индекс - {max_neg_pos}")
