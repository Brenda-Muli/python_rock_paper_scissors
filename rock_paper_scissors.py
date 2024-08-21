#import of random module to generate random choices for the computer
import random

#use of int to convert the input to an integer
user_choice= int(input('Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors.'))

#generating a random integer between 0-2
computer_choice = random.randint(0,2)

#print computer and user choice
print('Computer Chose:')
print(computer_choice)
print('You Chose:')
print(user_choice)

#if else statements to determine who wins or loses
if user_choice >=3 or user_choice <0:
    print('Enter a valid number:')
elif computer_choice == user_choice:
    print('It is a draw')
elif user_choice == 0 and computer_choice == 2:
    print('You win!')
elif computer_choice == 0 and user_choice == 2:
    print('You loose')
elif user_choice > computer_choice:
    print('You win!')
else:
    print('You lose')
