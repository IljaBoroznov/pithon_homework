# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, 
# вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2

print('Введите число N')
n = int(input())
lis = [i for i in range(0, n)] 
from random import randint
for i in lis:
    lis[i] = randint(-n, n)
def multi_pos_in_list(list, a, b):
    return list[a] * list[b]
print(lis)
print('Введите номер позиции')
a = int(input())
print('Введите номер позиции')
b = int(input())
print(multi_pos_in_list(lis, a, b))
