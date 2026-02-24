import random


def get_initial_pencils():
    while True:

        input_data = input("How many pencils would you like to use:\n> ")
        if not input_data.isnumeric():
            print("The number of pencils should be numeric")
            continue
        n = int(input_data)
        if n <= 0:
            print("The number of pencils should be positive")
            continue
        return n


def get_first_player(name1, name2):
    while True:

        first = input(f"Who will be the first ({name1}, {name2}):\n> ")
        if first not in [name1, name2]:
            print(f"Choose between '{name1}' and '{name2}'")
            continue
        return first


def main():
    global take
    name1, name2 = "John", "Jack"

    n_pencils = get_initial_pencils()
    current_player = get_first_player(name1, name2)


    while n_pencils > 0:
        print("|" * n_pencils)
        print(f"{current_player}'s turn!")

        if current_player == name2:

            if n_pencils == 1:
                take = 1
            elif n_pencils % 4 == 0:
                take = 3
            elif n_pencils % 4 == 3:
                take = 2
            elif n_pencils % 4 == 2:
                take = 1
            else:
                take = random.randint(1, 3)
            print(take)
        else:

            while True:
                take_input = input("> ")
                if take_input not in ['1', '2', '3']:
                    print("Possible values: '1', '2' or '3'")
                    continue
                take = int(take_input)
                if take > n_pencils:
                    print("Too many pencils were taken")
                    continue
                break

        if n_pencils <= 0:
            winner = name1 if current_player == name2 else name2
            print(f"{winner} won!")
            break


        current_player = name2 if current_player == name1 else name1


if __name__ == "__main__":
    main()