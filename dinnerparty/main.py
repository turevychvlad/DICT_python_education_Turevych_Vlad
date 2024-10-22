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

    print(friends) 
