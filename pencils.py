import random

def get_initial_pencils():
    while True:
        try:
            pencils = int(input("How many pencils would you like to use: "))
            if pencils <= 0:
                # кількість олівців повинна бути позитивною
                print("The number of pencils should be positive")
            else:
                return pencils
        except ValueError:
            # кількість олівців повинна бути числом
            print("The number of pencils should be numeric")

def get_first_player(player1, player2):
    while True:
        first = input(f"Who will be the first ({player1}, {player2}): ")
        if first == player1 or first == player2:
            return first
        else:
            # оберіть між двома іменами
            print(f"Choose between '{player1}' and '{player2}'")

def bot_move(pencils):
    # стратегія бота
    if pencils % 4 == 0:
        return 3
    elif pencils % 4 == 3:
        return 2
    elif pencils % 4 == 2:
        return 1
    else:
        return random.randint(1, min(3, pencils))

def player_move(pencils):
    while True:
        try:
            move = int(input("How many pencils to take: "))
            if move < 1 or move > 3:
                # значення може бути лише 1, 2 або 3
                print("Possible values: '1', '2' or '3'")
            elif move > pencils:
                # взято забагато олівців
                print("Too many pencils were taken")
            else:
                return move
        except ValueError:
            # значення має бути числом
            print("Possible values: '1', '2' or '3'")

def main():
    print("Welcome to the Pencil Game!")
    pencils = get_initial_pencils()
    player1 = "John"
    player2 = "Jack (bot)"
    current_player = get_first_player(player1, player2)

    while pencils > 0:
        print("|" * pencils)
        print(f"{current_player}'s turn!")
        
        if current_player == player1:
            move = player_move(pencils)
        else:
            move = bot_move(pencils)
            print(move)
        
        pencils -= move
        if pencils == 0:
            # визначення переможця
            print(f"{current_player} lost!")
            break

        current_player = player2 if current_player == player1 else player1

if __name__ == "__main__":
    main()
