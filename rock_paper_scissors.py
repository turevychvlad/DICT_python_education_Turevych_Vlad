import random

# читаємо ім'я користувача
name = input("Enter your name: ")
print(f"Hello, {name}")

# читаємо рейтинг з rating.txt
score = 0
try:
    with open("rating.txt", "r") as file:
        for line in file:
            if line.startswith(name):
                score = int(line.split()[1])
                break
except FileNotFoundError:
    pass

# читаємо опції гри (розширений список або стандартний)
user_input = input()
if user_input:
    options = user_input.strip().split(',')
else:
    options = ["rock", "paper", "scissors"]

print("Okay, let's start")

def get_losing_options(choice, options):
    # обчислюємо, хто програє обраному варіанту
    index = options.index(choice)
    rotated = options[index+1:] + options[:index]
    half = len(rotated) // 2
    return rotated[:half]  # ці варіанти перемагають обране

while True:
    user_choice = input()

    if user_choice == "!exit":
        print("Bye!")
        break
    elif user_choice == "!rating":
        print(f"Your rating: {score}")
    elif user_choice in options:
        computer_choice = random.choice(options)
        if user_choice == computer_choice:
            print(f"There is a draw ({computer_choice})")
            score += 50
        elif computer_choice in get_losing_options(user_choice, options):
            print(f"Sorry, but the computer chose {computer_choice}")
        else:
            print(f"Well done. The computer chose {computer_choice} and failed")
            score += 100
    else:
        print("Invalid input")
