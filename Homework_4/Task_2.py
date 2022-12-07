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

print(prime_factors(n))
