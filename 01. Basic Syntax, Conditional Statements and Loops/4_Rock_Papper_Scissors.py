import random

# ASCII Art

rock = r'''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''

paper = r'''
       _
   _  / |
  / \ | | /\
   \ \| |/ /
    \ Y | /___
  .-.) '. `__/
 (.-.   / /
     | ' |
     |___|
    [_____]
    |     |
'''

scissors = r'''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/

'''
rockPaperScissors = [rock, paper, scissors]

print(r''' 
            WELCOME TO THE ROCK PAPER SCISSORS
             __ _  __ _ _ __ ___   ___  ___ 
             / _` |/ _` | '_ ` _ \ / _ \/ __|
            | (_| | (_| | | | | | |  __/\__ \
             \__, |\__,_|_| |_| |_|\___||___/
              __/ |                          
             |___/   

''')



computerChoice = random.randint(0, 2)
userChoice = int(input('What do you chose? Type 0 for ROCK, 1 for PAPER, or 2 for SCISSORS\n'))


computerScore = 0
userScore = 0
playAgain = False

if userChoice >= 3:
    print('''Invaild number! you LOSE!''')
    computerScore += 1
else:
    print(rockPaperScissors[userChoice])
    print("Computer Chose: ")
    print(rockPaperScissors[computerChoice])
    if userChoice == computerChoice:  # Tie
        print('It is a TIE!')

    #user chooses rock:
    elif userChoice == 0 and computerChoice == 1:  # lose
        print("You LOSE!")
        computerScore += 1

    elif userChoice == 0 and computerChoice == 2:  # win
        print('You WIN!')
        userScore += 1

    #user chooses paper:
    elif userChoice == 1 and computerChoice == 0:  # win
        print('You WIN!')
        userScore += 1

    elif userChoice == 1 and computerChoice == 2:  # lose
        print("You LOSE!")
        computerScore += 1

    elif userChoice == 2 and computerChoice == 0:  # lose
        print("You LOSE!")
        computerScore +=1

    elif userChoice == 2 and computerChoice == 1:  # win
        print('You WIN!')
        userScore +=1



print('Your Score: ' + str(userScore))
print("Computer's score " + str(computerScore))
