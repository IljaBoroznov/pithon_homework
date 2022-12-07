#Задайте последовательность чисел. 
# Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
lis = [randint(-5, 5) for i in range(20)]

new_list = []
for i in lis:
    if i not in new_list:
        new_list.append(i)

print(lis)
print(new_list)

# lis = list(set(lis))
# print(lis)