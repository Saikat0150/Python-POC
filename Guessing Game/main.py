import random


def choose_word(file):
    with open(file, "r") as f:
        words = f.read().splitlines()
    return random.choice(words)


def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    print(displayed_word)
    return displayed_word.strip()


def word_guessing_game():
    print("Welcome to the Word Guessing Game")
    file = 'data.txt'
    word = choose_word(file)
    attempts = len(word)
    guessed_letters = []
    print(f"\nYou have total {attempts} attempts")
    while attempts > 0:
        print("\nWord: ", display_word(word, guessed_letters))
        guess = input("Enter you guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter..")
            continue

        if guess in guessed_letters:
            print("You already guesses that letter..")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"\nThe letter is not in the word.. You have {attempts} attempts left.")

        if all(letter in guessed_letters for letter in word):
            print(f"\nYou won the game...")
            break

    else:
        print(f"You have run out of attempts. The word was '{word}'")

    play_again = input("\n Play again< (yes/no): ").lower()
    if play_again == "yes":
        word_guessing_game()
    else:
        print("\nThank you for playing the game..")


if __name__ == "__main__":
    word_guessing_game()
    