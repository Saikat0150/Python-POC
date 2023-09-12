import random


def guess_the_number():
    print("Welcome to the guessing game")
    print("Choose the number from 1 to 100")
    play_again = "yes"

    while play_again == "yes":
        secret_number = random.randint(1, 100)
        flag = False
        num_guesses = 0

        while num_guesses < 3:
            guess = int(input("Enter a number: "))
            num_guesses += 1
            if guess < secret_number:
                print(f"Too low.. Try again.. You have {3-num_guesses} more chance")
            elif guess > secret_number:
                print(f"Too high.. Try again.. You have {3-num_guesses} more chance")
            else:
                print("Congratulation!! You guesses the right number")
                flag = True
                break

        if not flag:
            print("Better luck next time")
        play_again = input("Do you want to play again? (yes/no): ").lower()


guess_the_number()
