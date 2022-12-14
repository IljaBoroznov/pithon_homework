# Реализуйте алгоритм перемешивания списка.
print('Введите число N')
n = int(input())
lis = [i for i in range(0, n+1)] 
print(lis)
import random
sort_lis = sorted(lis, key = lambda x: random.random())
print(sort_lis)