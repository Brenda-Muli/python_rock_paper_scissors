#import of random module to generate random choices for the computer
import random

# Initializing scores and setting the number of rounds
user_score = 0
computer_score = 0
rounds = 3

#if else statement to determine points needed for a win
if rounds == 3:
    points_to_win = 2
else:
    points_to_win = 0

# mapping of numbers to their string values
choices = ['Rock', 'Paper', 'Scissors']

# A loop for when the user nor the computer has not yet reached the points to win
while user_score < points_to_win and computer_score < points_to_win:

# Getting user choice
    user_input = None
    while user_input not in [0, 1, 2]:
        user_input = int(input('Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: '))
        if user_input not in [0, 1, 2]:
            print('Invalid choice. Please enter 0, 1, or 2.')

# Getting computer choice
    computer_choice = random.randint(0, 2)
    print(f'Computer chose: {choices[computer_choice]}')
    print(f'You chose: {choices[user_input]}')

# Determining the winner of the round
    if user_input == computer_choice:
        print('It is a draw!')
    elif (user_input == 0 and computer_choice == 2) or \
         (user_input == 1 and computer_choice == 0) or \
         (user_input == 2 and computer_choice == 1):
        print('You win this round!')
        user_score += 1
    else:
        print('You lose this round!')
        computer_score += 1
    print(f'Score - Your score is: {user_score}, Computer score is: {computer_score}')

# Declaring the overall winner
if user_score > computer_score:
    print('Congratulations! You are the overall winner!')
else:
    print('The computer wins this time, Try again.')

print('Game Over')