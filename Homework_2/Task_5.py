# Реализуйте алгоритм перемешивания списка.
print('Введите число N')
n = int(input())
lis = [i for i in range(1, n*2+2)] #создание списка от 1 до N
a = - n
for i in range(n*2+1):
    lis[i] = a
    a += 1
print(lis)
for i in lis:
    temp = lis[i]
    lis[i] = lis[i+1]
    lis[i+1] = temp
print(lis)