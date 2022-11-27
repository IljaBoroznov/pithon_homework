# Напишите программу, 
# которая принимает на вход вещественное число 
# и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

print('введите число')
number = input()
res = list(number)
print(res)
result = [int(num) for num in filter(lambda num: num.isnumeric(), res)] # фильтрует из списка только интовые значения
print(result)
sum = 0
for i in range(len(result)):
    sum = sum + result[i]
print(sum)
