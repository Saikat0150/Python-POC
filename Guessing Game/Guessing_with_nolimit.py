import random


def guess_the_number():
    print("Welcome to Guess the Number!")
    play_again = "yes"

    while play_again == "yes":
        # Generate a random number between 1 and 100
        secret_number = random.randint(1, 100)
        num_guesses = 0

        while True:
            # Prompt the user for a guess
            guess = int(input("Enter your guess (between 1 and 100): "))

            # Increase the number of guesses
            num_guesses += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
                break

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()


guess_the_number()
