import random

print("HANGMAN")

words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)

hint = secret_word[:3] + '-' * (len(secret_word) - 3)
print(f"Guess the word: {hint}")

guess = input("> ")

if guess.lower() == secret_word:
    print("You survived!")
else:
    print("You lost!")
