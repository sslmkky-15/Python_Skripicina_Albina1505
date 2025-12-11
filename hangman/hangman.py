import random

PROGRAMMING_LANGUAGES = ['swift', 'golang', 'rust', 'ruby', 'kotlin', 'python', 'java']

MAX_MISTAKES = 7

def pick_secret_word():

    return random.choice(PROGRAMMING_LANGUAGES)

def initialize_display_word(secret_word):

    word_length = len(secret_word)
    if word_length <= 3:

        return ['-'] * word_length

    initial_view = list(secret_word[:3]) + ['-'] * (word_length - 3)
    return initial_view


def show_current_progress(displayed_list):
    print(' '.join(displayed_list))


def uncover_letters(target_word, current_view, guess_char):

    newly_revealed = 0
    for idx, char in enumerate(target_word):

        if char == guess_char and current_view[idx] == '-':
            current_view[idx] = guess_char
            newly_revealed += 1
    return newly_revealed


def check_input_validity(user_input):

    if len(user_input) != 1:
        print("Enter only one letter!")
        return False
    if not user_input.islower() or not user_input.isalpha():
        print("Please enter a lowercase English letter (a-z).")
        return False
    return True

def start_new_round():

    secret_word = pick_secret_word()
    current_display = initialize_display_word(secret_word)

    if '-' not in current_display:
        print("\nYou have already guessed the word: ")
        show_current_progress(current_display)
        print("Incredible! You won from the first step!")
        return

    mistakes_count = 0
    used_letters = set()

    while True:
        print("\n" + "=" * 30)
        show_current_progress(current_display)
        print(f"Remaining attempts: {MAX_MISTAKES - mistakes_count}")
        print(f"Letters used: {', '.join(sorted(list(used_letters)))}")
        print("=" * 30)

        guess = input("Your letter: ").strip()

        if not check_input_validity(guess):
            continue

        if guess in used_letters:
            print("You have already named this letter. Try another one.")
            continue

        used_letters.add(guess)

        if guess not in secret_word:
            print(f"Unfortunately, the letter '{guess.upper()}' is missing from the word.")
            mistakes_count += 1
            if mistakes_count >= MAX_MISTAKES:
                print("\nAll attempts have been exhausted!")
                print(f"The word was: **{secret_word}**")
                return
            continue

        revealed_now = uncover_letters(secret_word, current_display, guess)

        if revealed_now == 0:

            print("This letter was already known.")
            continue

        if '-' not in current_display:
            print(f"\nCongratulations! You guessed the word! **{secret_word}**!")
            show_current_progress(current_display)
            print("You are saved!")
            return

def run_game_manager():

    print("HANGMAN")
    print("Try to guess the word before you run out of attempts!")

    while True:
        command = input('\nEnter "play" to start, "exit" to finish: ').strip().lower()
        if command == "play":
            start_new_round()
        elif command == "exit":
            print("Thanks for playing! See you later.")
            break
        else:
            print("Unknown command. Try 'play' or 'exit'.")
            continue

if __name__ == "__main__":
    run_game_manager()