import random


def get_level():
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        try:
            level = int(input("> "))
            if level in [1, 2]:
                return level
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")


def generate_task(level):
    if level == 1:

        a = random.randint(2, 9)
        b = random.randint(2, 9)
        op = random.choice(['+', '-', '*'])
        question = f"{a} {op} {b}"
        if op == '+':
            answer = a + b
        elif op == '-':
            answer = a - b
        else:
            answer = a * b
    else:

        a = random.randint(11, 29)
        question = f"{a}"
        answer = a ** 2
    return question, answer


def main():
    level = get_level()
    score = 0


    for _ in range(5):
        question, correct_answer = generate_task(level)
        while True:
            print(question)
            try:
                user_answer = int(input("> "))
                break
            except ValueError:

                print("Incorrect format.")

        if user_answer == correct_answer:
            print("Right!")
            score += 1
        else:
            print("Wrong!")


    print(f"Your mark is {score}/5.")

    # Запит на збереження результату
    print("Would you like to save your result to the file? Enter yes or no.")
    save_choice = input("> ").strip().lower()

    if save_choice in ['yes', 'y']:
        print("What is your name?")
        name = input("> ")

        level_description = "simple operations with numbers 2-9" if level == 1 else "integral squares of 11-29"


        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(f"{name}: {score}/5 in level {level} ({level_description}).\n")

        print('The results are saved in "results.txt".')


if __name__ == "__main__":
    main()