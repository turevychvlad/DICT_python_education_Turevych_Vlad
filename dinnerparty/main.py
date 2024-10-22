num_friends = int(input("Enter the number of friends joining (including you): "))

if num_friends <= 0:
    print("No one is joining for the party")
else:
    friends = {}
    for _ in range(num_friends):
        name = input("Enter the name of a friend (including you): ")
        friends[name] = 0

    print(friends)
