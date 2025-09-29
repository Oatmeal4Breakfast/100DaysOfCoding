import random

from logo import logo, vs
from game_data import data


def pick_item(data: list) -> dict:
    """Randomly select an item from the list and remove it as an available option"""
    item: dict = random.choice(data)
    data.remove(item)
    return item


def print_vs(item_1: dict, item_2: dict) -> None:
    """Print the vs card"""
    print(
        f"Compare A: {item_1['name']} a {item_1['description']} from {item_1['country']}"
    )
    print(vs)
    print(
        f"Compare B: {item_2['name']} a {item_2['description']} from {item_2['country']}"
    )


def validate_response(response: str) -> str:
    valid_responses: list = ["A", "B"]
    guess: str = response
    while response.upper() not in valid_responses:
        guess: str = input("Invalid response. Please type 'A' or 'B': ")
    return guess


def compare_followers(user_choice: dict, other_choice: dict) -> bool:
    """Compare the follower counts of the two items"""
    if user_choice["follower_count"] > other_choice["follower_count"]:
        return True
    else:
        return False


def main():
    # print the logo
    print(logo)

    player_score: int = 0
    # Initiate the choice
    user_choice: dict = {}
    other_choice: dict = {}

    # Randomly pick an account from the list of accounts
    item_1: dict = pick_item(data=data)
    item_2: dict = pick_item(data=data)

    print_vs(item_1=item_1, item_2=item_2)

    # Asking the user to take a guess
    guess: str = input("Who do you think has more followers? Type 'A' or 'B': ")
    validate_response(response=guess)

    if guess == "A":
        user_choice = item_1
        other_choice = item_2
    elif guess == "B":
        user_choice = item_2
        other_choice = item_1

    print(f"You chose: {user_choice['follower_count']}")
    print(f"The other choise was: {other_choice['follower_count']}")
    # Compare the choice
    if compare_followers(user_choice=user_choice, other_choice=other_choice):
        print("Correct!")
        player_score += 1
        other_choice = pick_item(data=data)
    else:
        print(f"Game over. Your score was {player_score}")


if __name__ == "__main__":
    main()
