# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 

import random
print('Введите размер списка')
size = int(input())
print('Минимальное значение элемента')
a = int(input())
print('Максимальное значение элемента')
b = int(input())
list = [random.randint(a,b) for i in range(size)]
print(list)

#list = [2, 3, 5, 6, 7] 

if len(list) % 2 == 0:
    newlist = []
    for i in range(int(len(list)/2)):
        res = list[i] * list[len(list) - 1 - i]
        newlist.append(res)
    print(newlist)
else:
    newlist = []
    for i in range(int(len(list)/2)):
        res = list[i] * list[len(list) - 1 - i]
        newlist.append(res)
    resmidle = list[int(len(list)/2)] ** 2
    newlist.append(resmidle)
    print(newlist) 
