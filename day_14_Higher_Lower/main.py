import random

from logo import logo, vs
from game_data import data


def pick_item(data: list) -> dict:
    """Randomly select an item from the list and remove it as an available option"""
    return random.choice(data)


def print_vs(item_1: dict, item_2: dict) -> None:
    """Print the vs card"""
    print(
        f"Compare A: {item_1['name']} a {item_1['description']} from {item_1['country']}"
    )
    print(vs)
    print(
        f"Compare B: {item_2['name']} a {item_2['description']} from {item_2['country']}"
    )


def get_valid_choice() -> str:
    guess: str = input("Who do you think has more followers? Type 'A' or 'B': ").upper()
    valid_responses: list = ["A", "B"]
    while guess not in valid_responses:
        guess: str = input("Invalid response. Please type 'A' or 'B': ").upper()
    return guess


def compare_followers(user_choice: dict, other_choice: dict) -> bool:
    """Compare the follower counts of the two items"""
    return user_choice["follower_count"] > other_choice["follower_count"]


def main():
    # print the logo
    print(logo)
    player_score: int = 0

    # make copy of the data to manipulate
    available_data: list = data.copy()

    # Randomly pick an account from the list of accounts
    item_2: dict = pick_item(data=available_data)
    available_data.remove(item_2)

    while True:
        item_1: dict = item_2
        item_2: dict = pick_item(data=available_data)
        available_data.remove(item_2)

        print_vs(item_1=item_1, item_2=item_2)
        guess: str = get_valid_choice()

        user_choice: dict = item_1 if guess == "A" else item_2
        other_choice: dict = item_2 if user_choice == item_1 else item_1

        # Compare the choice
        if compare_followers(user_choice=user_choice, other_choice=other_choice):
            print("Correct!")
            player_score += 1
            item_2 = user_choice
        else:
            print(f"Game over. Your score was {player_score}")
            break

        if not available_data:
            print("You've guessed all items correctly! You win!")
            break


if __name__ == "__main__":
    main()
