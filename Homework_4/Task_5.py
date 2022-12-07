# 5'. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9 

data = open('file1.txt', 'w')
data.write('2 * x**2 + 4 * x + 5')
data.close()
data = open('file2.txt', 'w')
data.write('4 * x**2 + 1 * x + 4')
data.close()
with open("file1.txt", "r") as file:
    str1 = file.readline()

a = str1.split(' ')

res = list(a)
result = [int(num) for num in filter(lambda num: num.isnumeric(), res)]


with open("file2.txt", "r") as file:
    str2 = file.readline()
b = str2.split(' ')

res2 = list(b)
result2 = [int(num) for num in filter(lambda num: num.isnumeric(), res2)]

finish = []
for i in range(0, len(result2)):
    finish.append(result[i] + result2[i])  

a = finish[0]
b = finish[1]
c = finish[2]
data = open('result.txt', 'w')
data.write(f'{a} * x**2 + {b} * x + {c}')
data.close()
# моя винда 7 не подружилась с SymPy, поэтому подошел к решению максимально топорно, 
# надеюсь, что устраню ошибку и переделаю это задание нормально. Пока так...