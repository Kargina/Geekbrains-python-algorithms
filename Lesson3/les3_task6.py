# 6. В одномерном массиве найти сумму элементов, 
# находящихся между минимальным и максимальным элементами. 
# Сами минимальный и максимальный элементы в сумму не включать.

import random

list_len = int(input('Введите длину массива: '))
rand_list = [random.randint(1, 100) for _ in range(list_len)]
print(f'Исходный массив:\n{rand_list}')

min_number = rand_list[0]
max_number = rand_list[0]
min_num_index = 0
max_num_index = 0

for i, item in enumerate(rand_list):
    if item < min_number:
        min_number = item
        min_num_index = i
    if item > max_number:
        max_number = item
        max_num_index = i

summa = 0
if min_num_index < max_num_index:
    for i in rand_list[min_num_index+1:max_num_index]:
        summa += i
else:
    for i in rand_list[max_num_index+1:min_num_index]:
        summa += i

print(f'Минимальный элемент {min_number} находится на позиции {min_num_index}')
print(f'Максимальный элемент {max_number} находится на позиции {max_num_index}')
print(f'Сумма элементов между ними: {summa}')
