# Задайте список из вещественных чисел. 
# Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 6, 10.01]
print(list)

for i in range(len(list)):
   list[i] = round(list[i] % int(list[i]), 3)
print(list)
a = list.count(0)
for i in range(a):
    list.remove(0)# удаление нуля
print(max(list)-min(list))