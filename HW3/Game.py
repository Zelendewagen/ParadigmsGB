import os

matrix = [[' '] * 3,
          [' '] * 3,
          [' '] * 3]
moveset = ['11', '12', '13',
           '21', '22', '23',
           '31', '32', '33']


def matrix_print():
    os.system('cls')
    print("-" * 10)
    print(f"{matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]}")
    print("-" * 10)
    print(f"{matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]}")
    print("-" * 10)
    print(f"{matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]}")


def player_move(name):
    while True:
        move = input(f"Ходит {name}: ")
        if move not in moveset:
            print("Данное поля занято или не существует. Введите номер строки и столбца")
        else:
            moveset.remove(move)
            matrix[int(move[0]) - 1][int(move[1]) - 1] = name[-11:-1]
            matrix_print()
            break


def check_win():
    if matrix[0][0] == matrix[0][1] and matrix[0][0] != ' ':
        if matrix[0][1] == matrix[0][2]:
            return True
    if matrix[1][0] == matrix[1][1] and matrix[1][0] != ' ':
        if matrix[1][1] == matrix[1][2]:
            return True
    if matrix[2][0] == matrix[2][1] and matrix[2][0] != ' ':
        if matrix[2][1] == matrix[2][2]:
            return True
    if matrix[0][0] == matrix[1][0] and matrix[0][0] != ' ':
        if matrix[1][0] == matrix[2][0]:
            return True
    if matrix[0][1] == matrix[1][1] and matrix[0][1] != ' ':
        if matrix[1][1] == matrix[2][1]:
            return True
    if matrix[0][2] == matrix[1][2] and matrix[0][2] != ' ':
        if matrix[1][2] == matrix[2][2]:
            return True
    if matrix[0][0] == matrix[1][1] and matrix[1][1] != ' ':
        if matrix[1][1] == matrix[2][2]:
            return True
    if matrix[0][2] == matrix[1][1] and matrix[1][1] != ' ':
        if matrix[1][1] == matrix[2][0]:
            return True


def game_x0():
    player1 = input('Введите имя первого игрока: ') + '(\033[33mX\033[0m)'
    player2 = input('Введите имя второго игрока: ') + '(\033[32m0\033[0m)'
    n = 0
    matrix_print()
    while n != 9:
        n += 1
        player_move(player1)
        if check_win():
            matrix_print()
            print(f"{player1} Победил !")
            break
        player_move(player2)
        n += 1
        if check_win():
            matrix_print()
            print(f"{player2} Победил !")
            break
    print('НИЧЬЯ !')
