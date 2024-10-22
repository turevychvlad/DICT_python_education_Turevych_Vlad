import random

num_friends = int(input("Enter the number of friends joining (including you): "))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    friends = {}
    for _ in range(num_friends):
        name = input("Enter the name of a friend (including you): ")
        friends[name] = 0

    total_amount = float(input("Enter the total amount: "))
    split_amount = round(total_amount / num_friends, 2)

    for name in friends:
        friends[name] = split_amount

    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ').strip()

    if lucky_choice == "Yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")

        new_split_amount = round(total_amount / (num_friends - 1), 2)
        
        for name in friends:
            if name != lucky_one:
                friends[name] = new_split_amount
            else:
                friends[name] = 0
    else:
        print("No one is going to be lucky")

    print(friends)
