# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

list_len = int(input('Введите длину массива: '))
random_list = [random.randint(-100, 100) for _ in range(list_len)]
print(f'Исходный массив:\n{random_list}')

min_number = random_list[0]
max_number = random_list[0]
min_num_index = 0
max_num_index = 0

for i, item in enumerate(random_list):
    if item < min_number:
        min_number = item
        min_num_index = i
    if item > max_number:
        max_number = item
        max_num_index = i

random_list[min_num_index] = max_number
random_list[max_num_index] = min_number

print(f'Новый массив:\n{random_list}')