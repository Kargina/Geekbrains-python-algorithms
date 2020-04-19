# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

i = int(input('Введите количество строк в матрице: '))
j = int(input('Введите количество столбцов в матрице: '))

matrix = [[random.randint(1, 100) for _ in range(j)] for _ in range(i)]

print('Исходная матрица:')
for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()

elements = matrix[0]

for line in matrix:
    for pos, item in enumerate(line):
        if item < elements[pos]:
            elements[pos] = item

max_element = elements[0]

for item in elements:
    if item > max_element:
        max_element = item

print(f'Минимальные элементы столбцов: {elements}')
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_element}')