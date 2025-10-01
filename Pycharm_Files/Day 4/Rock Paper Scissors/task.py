import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices: list = [rock, paper, scissors]

user_choice: int = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
random_index: int = random.randint(0, len(choices))
computer_choice = choices[random_index-1]

print(choices[user_choice])
print(f"Computer chose:\n{computer_choice}")

if user_choice not in range(len(choices)):
    print("Invalid input. Please choose a number between 0 and 2")
elif user_choice == random_index:
    print("Draw")
elif user_choice == 0 and random_index == 2:
    print("You win")
elif user_choice == 2 and random_index == 0:
    print("You lose")
elif user_choice > random_index:
    print("You win")
else:
    print("You lose.")


