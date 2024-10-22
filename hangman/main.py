import random

print("HANGMAN")

words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)
guessed_word = ['-' for _ in range(len(secret_word))]

attempts = 8
guessed_letters = set()

while attempts > 0:
    print(f"{''.join(guessed_word)}")
    letter = input("Input a letter: > ").lower() 
    
    if len(letter) != 1:
        print("Please input a single letter.")
        continue
    
    if not letter.isalpha():
        print("Please enter a lowercase English letter.")
        continue
    
    if letter in guessed_letters: 
        print("You’ve already guessed the letter.")
        continue
    
    guessed_letters.add(letter)
    
    if letter in secret_word:
        for i, char in enumerate(secret_word):
            if char == letter:
                guessed_word[i] = letter
    else:
        attempts -= 1
        print(f"That letter doesn't appear in the word. Attempts left: {attempts}")
    
    if '-' not in guessed_word:
        print(f"You survived! The word was: {secret_word}")
        break

if '-' in guessed_word:
    print(f"You lost! The word was: {secret_word}")
