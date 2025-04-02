import random

# створюємо повний набір доміно (унікальні пари [i, j], де i <= j)
def generate_full_set():
    return [[i, j] for i in range(7) for j in range(i, 7)]

# ділимо набір на гравця, компа і резерв
def distribute_pieces():
    while True:
        pieces = generate_full_set()
        random.shuffle(pieces)
        stock = pieces[:14]
        player = pieces[14:21]
        computer = pieces[21:]
        
        all_doubles = [x for x in player + computer if x[0] == x[1]]
        if all_doubles:
            max_double = max(all_doubles)
            if max_double in player:
                player.remove(max_double)
                return stock, computer, player, [max_double], "computer"
            else:
                computer.remove(max_double)
                return stock, computer, player, [max_double], "player"

# перевірка завершення гри
def check_game_over(player, computer, snake):
    if not player:
        return "player"
    if not computer:
        return "computer"
    if snake[0][0] == snake[-1][1]:
        count = sum([x.count(snake[0][0]) for x in snake])
        if count >= 8:
            return "draw"
    return None

# показ змійки (обрізка, якщо довга)
def format_snake(snake):
    if len(snake) > 6:
        return "".join(str(s) for s in snake[:3]) + "..." + "".join(str(s) for s in snake[-3:])
    return "".join(str(s) for s in snake)

# інтерфейс гри
def print_interface(stock, computer, snake, player, status):
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}\n")
    print(format_snake(snake) + "\n")
    print("Your pieces:")
    for idx, piece in enumerate(player):
        print(f"{idx+1}:{piece}")
    print()
    if status == "player":
        print("Status: It's your turn to make a move. Enter your command.")
    elif status == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
    elif status == "player_win":
        print("Status: The game is over. You won!")
    elif status == "computer_win":
        print("Status: The game is over. The computer won!")
    elif status == "draw":
        print("Status: The game is over. It's a draw!")

# перевірка допустимості ходу
def is_legal_move(piece, snake, side):
    left = snake[0][0]
    right = snake[-1][1]
    if side == "left":
        return piece[1] == left or piece[0] == left
    else:
        return piece[0] == right or piece[1] == right

# застосування ходу
def apply_move(snake, piece, side):
    if side == "left":
        if piece[1] == snake[0][0]:
            snake.insert(0, piece)
        else:
            snake.insert(0, piece[::-1])
    else:
        if piece[0] == snake[-1][1]:
            snake.append(piece)
        else:
            snake.append(piece[::-1])

# логіка комп'ютера з урахуванням частот
def computer_move_logic(snake, computer, stock):
    counts = {i: 0 for i in range(7)}
    for piece in computer + snake:
        counts[piece[0]] += 1
        counts[piece[1]] += 1
    scored = sorted([(piece, counts[piece[0]] + counts[piece[1]]) for piece in computer], key=lambda x: -x[1])
    for piece, _ in scored:
        for side in ["left", "right"]:
            if is_legal_move(piece, snake, side):
                computer.remove(piece)
                apply_move(snake, piece, side)
                return
    if stock:
        computer.append(stock.pop(0))

# хід гравця з перевірками
def player_turn(snake, player, stock):
    while True:
        try:
            move = int(input())
            if abs(move) > len(player):
                raise ValueError
            if move == 0:
                if stock:
                    player.append(stock.pop(0))
                return
            piece = player[abs(move) - 1]
            side = "right" if move > 0 else "left"
            if is_legal_move(piece, snake, side):
                apply_move(snake, piece, side)
                player.pop(abs(move) - 1)
                return
            else:
                print("Illegal move. Please try again.")
        except:
            print("Invalid input. Please try again.")

# ігровий цикл
def play():
    stock, computer, player, snake, status = distribute_pieces()
    while True:
        print_interface(stock, computer, snake, player, status)
        result = check_game_over(player, computer, snake)
        if result:
            print_interface(stock, computer, snake, player, result + "_win" if result in ["player", "computer"] else "draw")
            break
        if status == "player":
            player_turn(snake, player, stock)
            status = "computer"
        else:
            input()
            computer_move_logic(snake, computer, stock)
            status = "player"

if __name__ == "__main__":
    play()
