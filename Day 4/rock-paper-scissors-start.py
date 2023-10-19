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

#Write your code below this line 👇

import random

choices = [rock, paper, scissors]

while True:
    user_input = int(
        input('''
Choose an Option.
Type 0 for Rock, 1 for Paper, or 2 for Scissors
Type 3 to quit the game
'''))

    if user_input == 3:
        break  # Exit the loop to end the game
    elif user_input not in [0, 1, 2]:
        print('Invalid Input. Try again.')
        continue  # Skip the rest of the loop and start over

    computer_choice = random.randint(0, 2)

    if user_input == computer_choice:
        result = 'Tie'
    elif (user_input == 0 and computer_choice == 2) or (user_input == 1 and computer_choice == 0) or (user_input == 2 and computer_choice == 1):
        result = 'You Win'
    else:
        result = 'Computer Wins'

    print(f'\nYou chose:\n{choices[user_input]}\n')
    print(f'Computer chose:\n{choices[computer_choice]}\n')
    print(result)

print('Thanks for playing!')
