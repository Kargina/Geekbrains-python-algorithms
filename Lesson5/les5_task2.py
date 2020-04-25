# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. 
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Нельзя пользоваться функциями hex() и/или int() для преобразования систем счисления.
# Использовать модуль collections

from collections import deque
from functools import reduce

def number_is_hex(num):
    list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    for i in num:
        if i not in list_of_numbers:
            print(f"Число {''.join(num)} не шестнадцатиричное. Выход.")
            exit()

def sum_hex(num_1, num_2):

    list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

    num_1 = num_1[::-1]
    num_2 = num_2[::-1]
    
    if len(num_1) < len(num_2):
        max_len = len(num_2)
        num_1.extend(['0'] * (max_len - len(num_1)))
    elif len(num_2) < len(num_1):
        max_len = len(num_1)
        num_2.extend(['0'] * (max_len - len(num_2)))
    else:
        max_len = len(num_1)

    result = deque()
    add_one = 0

    for i in range(max_len):
        digit1 = num_1[i]
        digit2 = num_2[i]
        summa = list_of_numbers.index(digit1) + list_of_numbers.index(digit2) + add_one
        result.appendleft(summa % 16)
        add_one = summa // 16

    if add_one != 0:
        result.appendleft(add_one)

    for id, item in enumerate(result):
        result[id] = list_of_numbers[item]

    return list(result)

def product_hex(num_1, num_2):

    list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    num_1 = num_1[::-1]
    num_2 = num_2[::-1]
    result = []
    nulls = 0

    for i in num_1:

        carry = 0
        intermediate_result = deque()

        for j in num_2:
            product = list_of_numbers.index(i) * list_of_numbers.index(j) + carry
            intermediate_result.appendleft(product % 16)
            carry = product // 16

        if carry != 0:
            intermediate_result.appendleft(carry)
        for _ in range(nulls):
            intermediate_result.append(0)
        nulls += 1

        for id, item in enumerate(intermediate_result):
            intermediate_result[id] = list_of_numbers[item]
        result.append(intermediate_result)

    for id, item in enumerate(result):
        result[id] = list(item)
    result = reduce(sum_hex, result)
            
    return result

def main():

    number_1 = list(input("Введите первое число: ").upper())
    number_2 = list(input("Введите второе число: ").upper())

    number_is_hex(number_1)
    number_is_hex(number_2)

    summa = sum_hex(number_1, number_2)
    product = product_hex(number_1, number_2)

    print(f"Сумма чисел - {''.join(summa)}")
    print(f"Произведение чисел - {''.join(product)}")

if __name__ == "__main__":

    main()
