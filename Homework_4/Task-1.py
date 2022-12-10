print('Ведите порядок знаков числа Пи после запятой')
n = int(input())
import math
print(round(math.pi, n))

def format_by_mask(num: float, number: float) -> float:
    """форматирует число по заданной маске"""
    number = str(number)
    number = len(number[number.find('.')+1::]) # find ищет точку и считает сколько знаков после точки
    return float(f'{math.pi:0.{number}f}') # f'a:0.3f' 

d = input('Ведите точность в формате "0.00001": ')
print(format_by_mask(math.pi, d))