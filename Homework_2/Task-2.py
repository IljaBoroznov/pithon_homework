#  Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Введите число N')
n = int(input())
lis = [i for i in range(1,n+1)] #создание списка от 1 до N
a = 1
res = 1
for a in range(n):
    res = res * lis[a]
    lis[a] = res
print(lis)
