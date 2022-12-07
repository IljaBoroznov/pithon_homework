# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 
 
from random import randint
lis = [randint(0, 100) for i in range(3)]
print(lis)
a = lis[0]
b = lis[1]
c = lis[2]
data = open('kef.txt', 'w')
data.write(f'{a} * x**3 + {b} * x**2 + {c}* = 0')
data.close()
