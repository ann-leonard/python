import random
moves = ['rock','paper','scissors']
playerMove = input("Please choose 'rock', 'paper', or 'scissors': ")

compMove = random.choice(moves)
print(f'The computer chose {compMove}.')
if compMove == playerMove:
    print("It's a tie")
elif compMove == 'rock' and playerMove == 'paper' or compMove == 'paper' and playerMove == 'scissors' or compMove == 'scissors' and playerMove == 'rock':
    print("you win!")
else:
    print("You lose!")
