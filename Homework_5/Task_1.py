print('Введите имя 1 игрока')
player1 = input()
print('Введите имя 2 игрока')
player2 = input()
konf = 117
from random import randint
i = randint(1, 2)
temp = konf
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
        print(temp)
        i += 1
    else:
        print(f'игрок {player2} введите число конфет')
        chois2 = int(input())
        if chois2 > 28:
            while chois2 > 28:
                print(f'{player2} число конфет не должно превышать 28, попробуйте еще раз')
                chois2 = int(input())
        else:
            temp = temp - chois2
        print(temp)
        i += 1
if i % 2 == 0:
    print(f'Победил {player2} ')
else:
    print(f'Победил {player1} ')
