def greet():
    print("                   ")
    print(" Приветсвую вас    ")
    print(" в игре            ")
    print(" крестики-нолики!  ")
    print("                   ")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")


field = [[' '] * 3 for i in range(3)]


def board():
    print()
    print("|XY | 0 | 1 | 2 | ")
    print("----------------- ")
    for i, row in enumerate(field):
        row_str = f"| {i} | { ' | '.join(row)} | "
        print(row_str)
        print("----------------- ")
    print()


def turn():
    while True:
        cords = input("  Ваш ход: ").split()

        if len(cords) != 2:
            print("Вы ввели больше двух координат! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите только числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Вы вышли из диапазона!")
            continue

        if field[x][y] != " ":
            print("Клетка уже занята!")
            continue
        return x, y


def win():
    win_cords = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cords:
        symbols = []
        for i in cord:
            symbols.append(field[i[0]][i[1]])
        if symbols == ["X", "X", "X"]:
            print("Победитель X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Победитель 0!!!")
            return True
    return False


greet()
count = 0
while True:
    count += 1
    board()
    if count % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = turn()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if count == 9:
        print("Ничья!")
        break