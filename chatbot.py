# Этап 1
print("Hello! My name is NoviceBot.")
print("I was created in 2024.")

# Этап 2
print("Please, remind me your name.")
your_name = input("> ")
print(f"What a great name you have, {your_name}!")

# Этап 3
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input("> "))
remainder5 = int(input("> "))
remainder7 = int(input("> "))
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")

# Этап 4
print("Now I will prove to you that I can count to any number you want.")
number = int(input("> "))
for i in range(number + 1):
    print(f"{i} !")
print("Completed, have a nice day!")

# Этап 5
print("Let's test your programming knowledge.")

while True:
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    answer = int(input("> "))
    
    if answer == 2:
        print("Congratulations, have a nice day!")
        break
    else:
        print("Please, try again.")
