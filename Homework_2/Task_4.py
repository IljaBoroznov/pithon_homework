# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, 
# вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2

print('Введите число N')
n = int(input())
lis = [i for i in range(1, n*2+2)] #создание списка от 1 до N
a = - n
for i in range(n*2+1):
    lis[i] = a
    a += 1
print(lis)
print('Введите номер позиции')
first = int(input())
print('Введите номер позиции')
second = int(input())
print(f'произведение равно {lis[first] * lis[second]}')
