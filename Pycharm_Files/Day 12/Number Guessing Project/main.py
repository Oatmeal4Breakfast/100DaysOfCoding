import random
from art import logo


def validate_response(response: str) -> None:
    """ Validate the user response. """
    valid_responses: list = ['easy', 'hard']
    while True:
        if response.lower() not in valid_responses:
            response: str = input("Invalid Response! Type 'easy' or 'hard'")
        else:
            return


def check_guess(guess: int, number: int) -> bool:
    """ checks the guess against the number """
    if guess == number:
        print("You win!")
        return True
    elif guess > number:
        print("Too high.")
        return False
    else:
        print("Too low.")
        return False


def pick_number() -> int:
    """ pick a random number between 1 and 100"""
    return random.randint(a=1, b=100)


def main():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty: str = input("Choose a difficulty. Type 'easy' or 'hard': ")
    validate_response(difficulty)
    if difficulty == 'easy':
        lives: int = 10
    else:
        lives: int = 5

    print(f"You have {lives} lives to guess the number")
    number_to_guess: int = pick_number()

    guess: int = int(input("Make a guess: "))

    for life in range(lives -1):
        if check_guess(guess, number_to_guess):
            return
        else:
            lives -= 1
            print(f"You have {lives} attempt(s) remain to guess the number.")
            guess: int = int(input("Make a guess: "))

    print("You lose")





main()