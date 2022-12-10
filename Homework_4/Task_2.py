# 2'. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

print('Ведите натуральное число')
n = int(input())
def prime_factors(num):
    list = []
    if n % 2 == 0:
        list.append(2)
    if n % 3 == 0:
        list.append(3)
    if n % 5 == 0:
        list.append(5)
    else:
        list.append(n)
    return list

print(f'Список делителей числа {n} -> {prime_factors(n)}')


def dividers(a: int, uniq: bool = False):
    i = 2 
    dividers = []
    while a != 1:
        while a % i == 0:
            dividers.append(i)
            a //= i
        i += 1
    if uniq:
        return list(set(dividers))
    else:
        return dividers

print(f'Список натуральных делителей числа {n}: {dividers(n, True)}')
