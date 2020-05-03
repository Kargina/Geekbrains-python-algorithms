# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# Для проверки использовалась программа нахождения простого числа с помощью алгоритма «Решето Эратосфена» и без него

import math
import sys

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

    for val in locals().values():
        show_size(val)

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

    for val in locals().values():
        show_size(val)

    return(primes[-1])

def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level+1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level+1)
        
    return sys.getsizeof(x)

def main():

    print(sys.version, sys.platform)

    print(f"\n{'*' * 10} Check function \"prime_sieve\" {'*' * 10}\n")
    prime_sieve(10)
    print(f"\n{'*' * 10} Check function \"prime\" {'*' * 10}\n")
    prime(10)

if __name__ == "__main__":
    main()   
