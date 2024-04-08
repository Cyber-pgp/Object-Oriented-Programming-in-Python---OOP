# making computer choose random
# importing modules


computers_choice = 'scissors'
users_choice = input('Do you want rock, paper or scissors?')

if computers_choice == users_choice:
    print('TIE')
elif users_choice == 'rock' and computers_choice == 'scissors':
    print('YOU WIN!')
elif users_choice == 'paper' and computers_choice == 'rock':
    print('YOU WIN!')
elif users_choice == 'scissors' and computers_choice == 'paper':
    print('YOU WIN!')
elif users_choice == 'paper' and computers_choice == 'scissors':
    print('YOU LOSE!')
elif users_choice == 'rock' and computers_choice == 'paper':
    print('YOU LOSE!')
elif users_choice == 'scissor' and computers_choice == 'rock':
    print('YOU LOSE!')
else:
    print('You win some and lose most!')


# but we want computer to choose it self then we need to rendomis this
# to make this randomise 

import random

computer_chioce = random.choice(['rock', 'paper', 'scissor'])

# ['rock', 'paper', 'scissor'] creatinng the list 
users_choice = input('Do you want rock, paper or scissors?')

print('Compter choice:', computer_choice)

if computers_choice == users_choice:
    print('TIE')
elif users_choice == 'rock' and computers_choice == 'scissors':
    print('YOU WIN!')
elif users_choice == 'paper' and computers_choice == 'rock':
    print('YOU WIN!')
elif users_choice == 'scissors' and computers_choice == 'paper':
    print('YOU WIN!')
elif users_choice == 'paper' and computers_choice == 'scissors':
    print('YOU LOSE!')
elif users_choice == 'rock' and computers_choice == 'paper':
    print('YOU LOSE!')
elif users_choice == 'scissor' and computers_choice == 'rock':
    print('YOU LOSE!')
else:
    print('You win some, you lose most!')
