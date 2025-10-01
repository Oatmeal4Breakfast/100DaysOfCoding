import random
from art import logo

def deal_card(hand: list, deck: list) -> list:
    """ deals a card and adds it to the hand"""
    hand.append(random.choice(deck))
    return hand


def validate_response(player_input: str) -> None:
    while True:
        if player_input.lower() not in ["y","n"]:
            player_input: str = input("Invalid response. Pleaser enter 'y' or 'n': ")
        else:
            return


def start_hand(hand: list, deck: list) -> list:
    for i in range(2):
        hand.append(random.choice(deck))
    return hand


def check_for_ace(hand: list, score:int) -> int:
    if 11 in hand and sum(hand) < 21:
        index = hand.index(11)
        hand.pop(index)
        hand.append(1)
        score = sum(hand)
    else:
        score = sum(hand)
    return score


def main():
    print(logo)
    play:str = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    validate_response(play)

    while play == 'y':
        # initialize hands
        player_hand: list = []
        computer_hand: list = []

        # initialize the scores
        player_score: int = 0
        computer_score: int = 0

        # initialize the deck
        cards: list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        # deal the first two cards
        start_hand(player_hand, cards)
        start_hand(computer_hand, cards)

        player_score += sum(player_hand)
        computer_score += sum(computer_hand)
        print(f"You cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card {computer_hand[0]}")

        another_card: str = input("Type 'y' to get another card, type 'n' to pass: ")
        validate_response(another_card)
        while another_card == 'y':
            deal_card(hand=player_hand, deck=cards)
            deal_card(hand=computer_hand, deck=cards)
            check_for_ace(hand=player_hand, score=player_score)

            player_score = sum(player_hand)
            print(f"Your hand is {player_hand}, score is: {player_score}")
            print(f"Computer's first card {computer_hand[0]}")

            another_card: str = input("Type 'y' to get another card, type 'n' to pass: ")
            validate_response(another_card)

        while computer_score < 17:
            deal_card(hand=computer_hand, deck=cards)
            computer_score = sum(computer_hand)

        print(f"Your final hand is: {player_hand}, final score: {player_score}")
        print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

        if player_score <= 21 and player_score > computer_score:
            print("You win")
        elif player_score == computer_score:
            print("Draw")
        elif computer_score > 21:
            print("You win")
        else:
            print("You lose")

        play: str = input("Would you line to play again? 'y' or 'n'")
        validate_response(play)
        print("\n\n\n\n\n")
    #else:
    exit()


main()