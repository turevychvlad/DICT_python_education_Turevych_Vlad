import random

print("HANGMAN")

words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)

guess = input("Guess the word: > ")

if guess.lower() == secret_word:
    print("You survived!")
else:
    print("You lost!")
