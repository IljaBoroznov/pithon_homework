# 1. Создайте программу для игры с конфетами человек против человека.
# *' Условие задачи: На столе лежит 117 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

# a) Добавьте игру против бота


print('Введите имя игрока')
player1 = input()
player2 = 'BOT'
konf = 117
from random import randint
i = randint(1, 2)
temp = konf
prize1 = 0
prize2 = 0
while temp > 0:
    if i % 2 != 0:
        print(f'игрок {player1} введите число конфет')
        chois1 = int(input())
        if chois1 > 28:
            while chois1 > 28:
                print(f'{player1} число конфет не должно превышать 28, попробуйте еще раз')
                chois1 = int(input())
        else:
            temp = temp - chois1
            prize2 = prize2 + chois1
        i += 1
    else:
        print(f'игрок {player2} ввёл число конфет')
        chois2 = randint(1, 29)
        print(chois2)
        temp = temp - chois2
        prize1 = prize1 + chois2
        i += 1
if i % 2 == 0:
    print(f'Победил {player1} его приз {prize1} конфет')
else:
    print(f'Победил {player2} его приз {prize2} конфет')
