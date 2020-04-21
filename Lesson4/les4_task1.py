# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

# Для анализа использовалось следующее задание:
# В одномерном массиве найти сумму элементов, 
# находящихся между минимальным и максимальным элементами. 
# Сами минимальный и максимальный элементы в сумму не включать.

import random
import functools
import cProfile
import timeit

rand_list_short = [4,45,6,8,3,1,6,8,5,3,23,6,8,5,3]
rand_list_medium = [10, 100] + [3] * 100 + [1, 10]
rand_list_long = [10, 100] + [3] * 100000000 + [1, 10]

# Суммирование в цикле
def func_1(rand_list):
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

    return summa

# Суммирование рекурсией
def func_2(rand_list):

    def listsum(numList):
        if len(numList) == 1:
            return numList[0]
        else:
            return numList[0] + listsum(numList[1:])
    
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

    if min_num_index < max_num_index:
        new_list = rand_list[min_num_index+1:max_num_index]
    else:
        new_list = rand_list[max_num_index+1:min_num_index]

    return listsum(new_list)

# Суммирование с использованием стандартных функций
def func_3(rand_list):
    min_num_index = rand_list.index(min(rand_list))
    max_num_index = rand_list.index(max(rand_list))
    if min_num_index < max_num_index:
        new_list = rand_list[min_num_index+1:max_num_index]
    else:
        new_list = rand_list[max_num_index+1:min_num_index]
    return sum(new_list)



# cProfile.run('func_1(rand_list_short)')
#           4 function calls in 0.000 seconds
#           1    0.000    0.000    0.000    0.000 les4_task1.py:26(func_1)
# cProfile.run('func_1(rand_list_medium)')
#           4 function calls in 0.000 seconds
#           1    0.000    0.000    0.000    0.000 les4_task1.py:26(func_1)
# cProfile.run('func_1(rand_list_long)')
#           4 function calls in 29.001 seconds
#           1   29.001   29.001   29.001   29.001 les4_task1_.py:24(func_1)

# cProfile.run('func_2(rand_list_short)')
#           10 function calls (8 primitive calls) in 0.000 seconds
#           1    0.000    0.000    0.000    0.000 les4_task1.py:62(func_2)
#           3/1    0.000    0.000    0.000    0.000 les4_task1.py:64(listsum)
# cProfile.run('func_2(rand_list_medium)')
#           204 function calls (105 primitive calls) in 0.000 seconds
#           1    0.000    0.000    0.000    0.000 les4_task1.py:62(func_2)
#           100/1    0.000    0.000    0.000    0.000 les4_task1.py:64(listsum)
# cProfile.run('func_2(rand_list_long)')
#           RecursionError: maximum recursion depth exceeded in comparison

# cProfile.run('func_3(rand_list_short)')
#           9 function calls in 0.000 seconds
#           1    0.000    0.000    0.000    0.000 les4_task1.py:91(func_3)
# cProfile.run('func_3(rand_list_medium)')
#           9 function calls in 0.001 seconds
# cProfile.run('func_3(rand_list_long)')
#           9 function calls in 14.950 seconds
#           1    2.093    2.093   14.615   14.615 les4_task1_.py:78(func_3)
#           1    0.001    0.001   14.950   14.950 {built-in method builtins.exec}
#           1    3.106    3.106    3.106    3.106 {built-in method builtins.max}
#           1    4.172    4.172    4.172    4.172 {built-in method builtins.min}
#           1    2.660    2.660    2.660    2.660 {built-in method builtins.sum}
#           1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#           2    2.584    1.292    2.584    1.292 {method 'index' of 'list' objects}


# python -m timeit -n 1000 -s "import les4_task1" "les4_task1.func_1([4,45,6,8,3,1,6,8,5,3,23,6,8,5,3])"
# 1000 loops, best of 3: 3.93 usec per loop
# python -m timeit -n 1000 -s "import les4_task1" "les4_task1.func_2([4,45,6,8,3,1,6,8,5,3,23,6,8,5,3])"
# 1000 loops, best of 3: 6.15 usec per loop
# python -m timeit -n 1000 -s "import les4_task1" "les4_task1.func_3([4,45,6,8,3,1,6,8,5,3,23,6,8,5,3])"
# 1000 loops, best of 3: 4.07 usec per loop

# python -m timeit -n 100 -s "import les4_task1" "les4_task1.func_1([10, 100] + [3] * 100 + [1, 10])" 
# 100 loops, best of 3: 22.3 usec per loop
# python -m timeit -n 100 -s "import les4_task1" "les4_task1.func_2([10, 100] + [3] * 100 + [1, 10])"
# 100 loops, best of 3: 102 usec per loop
# python -m timeit -n 100 -s "import les4_task1" "les4_task1.func_3([10, 100] + [3] * 100 + [1, 10])"
# 100 loops, best of 3: 14.2 usec per loop

# python -m timeit -n 100 -s "import les4_task1" "les4_task1.func_1([10, 100] + [3] * 10000 + [1, 10])"
# 100 loops, best of 3: 1.95 msec per loop
# python -m timeit -n 100 -s "import les4_task1" "les4_task1.func_3([10, 100] + [3] * 10000 + [1, 10])"
# 100 loops, best of 3: 1.27 msec per loop

# Выводы
# Нахождение суммы массива рекурсией самый медленный способ из тестировавшихся
# Также при использовании рекурсивных функций достигается порог стандартной максимальной глубины рекурсии при работе с большими списками
# Использование циклов в данной задаче существенно повышает скорость выполнения
# Однако если использовать стандартную функцию суммы и нахождения минимального и максимального значения в массиве, 
# то скорость выполнения будет примерно в два раза выше, чем при использовании цикла.
