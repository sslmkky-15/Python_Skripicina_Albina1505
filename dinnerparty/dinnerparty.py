import random

print("Hello! Let's split the bill together.")

while True:
    print("First, tell me how many friends are joining (including you):")
    try:
        num_friends = int(input('> '))
        if num_friends <= 0:
            print("No one is joining for the party.")
          
            exit() 
        break
    except ValueError:
        print("Invalid input. Please enter a whole number (e.g., 5).")

print("Please, enter the name of every friend, one by one:")

friends = {}
i = 0
while i < num_friends:
    name = input('> ')
    friends[name] = 0
    i += 1

print("Now enter the total amount of the bill:")

while True:
    try:
        total_amount = float(input('> '))
        if total_amount <= 0:
            print("Please, enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value (e.g., 100.50).")

print('Do you want to use the "Who is lucky?" feature? (Yes/No)')
answer = input().strip().capitalize() # Додано очистку тексту (напр. "yes " -> "Yes")

if answer == "Yes":
    lucky_one = random.choice(list(friends.keys()))
    print(f"{lucky_one} is the lucky one!")

    if num_friends > 1:
        split_amount = round(total_amount / (num_friends - 1), 2)
    else:
        split_amount = 0 # Якщо ти один, то "lucky" означає безкоштовно? :)

    for friend in friends:
        if friend == lucky_one:
            friends[friend] = 0
        else:
            friends[friend] = split_amount
else:
    print("No one is going to be lucky.")
    split_amount = round(total_amount / num_friends, 2)
    for friend in friends:
        friends[friend] = split_amount

print("\nHere is the final split:")
print(friends)
print("Thank you for using the bill splitter. Have a nice day!")
