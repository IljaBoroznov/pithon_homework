print('Введите имя игрока')
player1 = input()
print('Введите имя 2 игрока')
player2 = input()

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end = ' ')
    print()
count = 0
while count < 9:
    if count % 2 != 0:
        print(f'{player1} введите номер позиции')
        pos1 = int(input())
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == pos1:
                    a[i][j] = 0
                print(a[i][j], end = ' ')
            print()
        b = 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[0][0] == 0 and a[0][1] == 0 and a[0][2] == 0:
                    b = 1 
                elif a[1][0] == 0 and a[1][1] == 0 and a[1][2] == 0:
                    b = 1   
                elif a[2][0] == 0 and a[2][1] == 0 and a[2][2] == 0:
                    b = 1    
                elif a[0][0] == 0 and a[1][0] == 0 and a[2][0] == 0:
                    b = 1   
                elif a[0][1] == 0 and a[1][1] == 0 and a[2][1] == 0:
                    b = 1    
                elif a[0][2] == 0 and a[1][2] == 0 and a[2][2] == 0:
                    b = 1    
                elif a[0][0] == 0 and a[1][1] == 0 and a[2][2] == 0:
                    b = 1   
                elif a[0][2] == 0 and a[1][1] == 0 and a[2][0] == 0:
                    b = 1
        if b == 1:
            print(f"победа {player1} ")
        count += 1
    else:
        print(f'{player2} введите номер позиции')
        pos2 = int(input())
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == pos2:
                    a[i][j] = 'x'
                print(a[i][j], end = ' ')
            print()
        c = 0
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[0][0] == 'x' and a[0][1] == 'x' and a[0][2] == 'x':
                    c = 1
                elif a[1][0] == 'x' and a[1][1] == 'x' and a[1][2] == 'x':
                    c = 1
                elif a[2][0] == 'x' and a[2][1] == 'x' and a[2][2] == 'x':
                    c = 1    
                elif a[0][0] == 'x' and a[1][0] == 'x' and a[2][0] == 'x':
                    c = 1    
                elif a[0][1] == 'x' and a[1][1] == 'x' and a[2][1] == 'x':
                    c = 1    
                elif a[0][2] == 'x' and a[1][2] == 'x' and a[2][2] == 'x':
                    c = 1    
                elif a[0][0] == 'x' and a[1][1] == 'x' and a[2][2] == 'x':
                    c = 1    
                elif a[0][2] == 'x' and a[1][1] == 'x' and a[2][0] == 'x':
                    c = 1
        if c == 1:
            print(f"победа {player2} ")     
        count += 1
    if count == 9 and c != 1 and b != 1:
        print('Ничья')




