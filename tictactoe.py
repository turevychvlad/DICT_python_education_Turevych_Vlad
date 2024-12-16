def print_field(field):
    # Функція для друку ігрового поля
    print("---------")
    for row in field:
        print(f"| {' '.join(row)} |")
    print("---------")

def check_winner(field):
    # Перевірка можливих виграшних комбінацій
    lines = [
        field[0], field[1], field[2],  # горизонтальні
        [field[i][0] for i in range(3)], [field[i][1] for i in range(3)], [field[i][2] for i in range(3)],  # вертикальні
        [field[i][i] for i in range(3)],  # діагональ зліва направо
        [field[i][2 - i] for i in range(3)],  # діагональ справа наліво
    ]
    if ["X"] * 3 in lines:
        return "X wins"
    if ["O"] * 3 in lines:
        return "O wins"
    # Перевірка стану "неможливо"
    count_x = sum(row.count("X") for row in field)
    count_o = sum(row.count("O") for row in field)
    if abs(count_x - count_o) > 1:
        return "Impossible"
    if any("_" in row for row in field):
        return "Game not finished"
    return "Draw"

def is_valid_input(coordinates, field):
    # Перевірка введених координат
    if len(coordinates) != 2 or not coordinates[0].isdigit() or not coordinates[1].isdigit():
        print("You should enter numbers!")
        return False

    x, y = map(int, coordinates)
    if not (1 <= x <= 3 and 1 <= y <= 3):
        print("Coordinates should be from 1 to 3!")
        return False

    if field[x - 1][y - 1] != "_":
        print("This cell is occupied! Choose another one!")
        return False

    return True

def tic_tac_toe():
    # Основна функція гри "Хрестики-нулики"
    field = [['_'] * 3 for _ in range(3)]  # Створення порожнього поля
    print_field(field)
    turn = "X"

    while True:
        # Введення координат
        coordinates = input("Enter the coordinates: ").split()
        if not is_valid_input(coordinates, field):
            continue

        x, y = map(int, coordinates)
        field[x - 1][y - 1] = turn
        print_field(field)

        result = check_winner(field)
        if result in ["X wins", "O wins", "Draw", "Impossible"]:
            print(result)
            break

        turn = "O" if turn == "X" else "X"

tic_tac_toe()
