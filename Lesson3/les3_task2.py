# 2. Во втором массиве сохранить индексы четных элементов первого массива. 
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, 
# второй массив надо заполнить значениями 0, 3, 4, 5 
# (помните, что индексация начинается с нуля), 
# т. к. именно в этих позициях первого массива стоят четные числа.

import random

list_len = int(input('Введите длину массива: '))
random_list = [random.randint(-100, 100) for _ in range(list_len)]
print(f'Исходный массив:\n{random_list}')

indexes_even_num = []

for i, item in enumerate(random_list):
    if item % 2 == 0:
        indexes_even_num.append(i)

if len(indexes_even_num) == 0:
    print('Четных элементов в массиве нет')
else:
    print(f'Список индексов четных элементов массива:\n{indexes_even_num}')