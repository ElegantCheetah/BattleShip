
#* Zain Kergaye
#* Mr. Webster
#* Programming 2

#? Hours wasted: 2.0

#ToDO:
#! 1. Create a class that makes an array 
#! 2. Get user input for the array
#! 3. Check if number is 1 or 0 
#! 5. give user feedback
#! 6. If number is 3 then say that they already hit that spot
#! 7. end game when they hit everything

from random import randint

def menu():
    print('------------------------')
    print('|Welcome to BattleShip!|')
    print('|                      |')
    print('|1. Play BattleShip    |')
    print('|2. View scores        |')
    print('|3. How to play        |')
    print('|4. Exit game          |')
    print('------------------------')

def howToPlay():
    #enter playing instructions here
    print('----------------------------------------------------------')
    print('|This is BattleShip, you are at a command console sending|')
    print("|missiles to an area on the playing field, enter a number|")
    print("|to select a specific row and then a specific columb     |")
    print('----------------------------------------------------------')
    input('Press any key to continue')

board = []




def print_board(board):
    print('\n')
    print("Battle Field")
    print('')
    for row in board:
        print('------------------')
        print (" | ".join(row))
    print('------------------')


def random_row(board):
    return randint(0,len(board) - 1)

def random_col(board):
    return randint(0,len(board[0]) - 1)

scores = open('Scores')

loop = 0
while (loop != 1):

    menu()
    menuInput = int(input('Enter selection 1-3: '))
    if(menuInput == 4):
        break
    
    if(menuInput == 3):
        howToPlay()

    if (menuInput == 2):
        
        BSscores = scores.read()
        print(BSscores)


    if(menuInput == 1):
        guessNum = 0
        board.clear()
        for x in range(5):
            board.append(["0"] * 5)
        
        ship_row = random_row(board)
        ship_col = random_col(board)

        gamedone = 1
        while gamedone == 1:
            print_board(board)
            print('------------------')
            guess_row = int(input("|Guess row: "))
            guess_col = int(input("|Guess col: "))
            print('------------------')

            if (guess_row == ship_row & guess_col == ship_col):
                guessNum = guessNum + 1
                print('----------------------------------------')
                print("|You win!                              |")
                print('|You sunk the battleship in ', guessNum, ' guesses|')
                print('----------------------------------------')
                input('Press any key to continue')
                #!scores.write('Best num:')
                #!scores.write(guessNum)
                break

            else:
                guessNum = guessNum + 1
                if(guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                    print('-------------------------')
                    print("|That's not in the board|")
                    print('-------------------------')
                elif(board[guess_row][guess_col] == 'X'):
                    print('-------------')
                    print('|Already hit|')
                    print('-------------')
                else:
                    print('------')
                    print('|miss|')
                    print('------')
                    board[guess_row][guess_col] = 'X'

    if(menuInput >= 4):
        print('-------------------------------')
        print('|Wrong answer please try again|')
        print('-------------------------------')
scores.close()