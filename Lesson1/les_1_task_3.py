# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.

import random

type = input('Введите тип числа\nint - целое число\nfloat - вещественное число\nchar - символ\n')

if type == 'int':
    begin = int(input('Введите первое число: '))
    end = int(input('Введите последнее число: '))
    print(f'Случайное число между {begin} и {end}: {random.randint(begin, end)}')

elif type == 'float':
    begin = float(input('Введите первое число: '))
    end = float(input('Введите последнее число: '))
    print(f'Случайное число между {begin} и {end}: {random.uniform(begin, end)}')

elif type == 'char':
    begin = input('Введите первый символ: ')
    end = input('Введите последний символ: ')
    print(f'Случайный символ между {begin} и {end}: {chr(random.randint(ord(begin), ord(end)))}')

