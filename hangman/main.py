print("HANGMAN")

secret_word = 'python'
guess = input("Guess the word: > ")

if guess.lower() == secret_word:
    print("You survived!")
else:
    print("You lost!")
