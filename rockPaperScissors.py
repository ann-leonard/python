import random

playerScore = 0
compScore = 0

def game():

    global compScore
    global playerScore

    moves = ['rock','paper','scissors']
    playerMove = input("Please choose 'rock', 'paper', or 'scissors': ")

    compMove = random.choice(moves)
    print(f'The computer chose {compMove}.')


    if compMove == playerMove:
        print("It's a tie- no points")
    elif compMove == 'rock' and playerMove == 'paper' or compMove == 'paper' and playerMove == 'scissors' or compMove == 'scissors' and playerMove == 'rock':
        print("you win!")
        playerScore +=1
    else:
        print("You lose!")
        compScore +=1

    print(f'You: {playerScore}')
    print(f'Computer: {compScore}')

while playerScore + compScore < 3:
    game()

if playerScore > compScore:
    print('You win!')
else:
    print('You lose :(')
