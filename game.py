import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        user_guess = input("Please enter your guess (between 1 and 100): ")
        attempts += 1

        try:
            user_guess = int(user_guess)
            if user_guess < 1 or user_guess > 100:
                print("Your guess is out of bounds. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")