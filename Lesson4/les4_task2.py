# 2. Написать два алгоритма нахождения i-го по счёту простого числа. 
# Функция нахождения простого числа должна принимать на вход натуральное 
# и возвращать соответствующее простое число. 
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import math
import cProfile

# Функция для нахождения верхней границы отрезка,
# в котором находится i-ое простое число
def upper_bound(prime_index):

    num_of_primes = 0
    upper_bound = 2
    while num_of_primes <= prime_index:
        num_of_primes = upper_bound / math.log(upper_bound)
        upper_bound += 1
    return upper_bound

# Алгоритм для нахождения простого числа с помощью алгоритма «Решето Эратосфена»
def prime_sieve(n):

    primes = []
    max_num = upper_bound(n)+1
    nums = [i for i in range(0,max_num)]
    nums[1] = 0
    for i in nums:
        if i > 1:
            primes.append(i)
            if i > 1:
                for j in range(i + i, len(nums), i):
                    nums[j] = 0
    return primes[n-1]

# Алгоритм для нахождения простого числа без использования решета Эратосфена
def prime(num):

    primes = []
    def isprime(n):
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        return d * d > n
    i = 2
    while len(primes) < num:
        if isprime(i):
            primes.append(i)
        i += 1
    return(primes[-1])

index = int(input("Введите номер простого числа: "))
print("Алгоритм для нахождения простого числа с помощью алгоритма «Решето Эратосфена»")
print(f"{index}-ое простое число - {prime_sieve(index)}")
print("Алгоритм для нахождения простого числа без использования «Решета Эратосфена»")
print(f"{index}-ое простое число - {prime(index)}")