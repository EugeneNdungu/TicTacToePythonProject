"""
The program is a tic tac toe game that allows to players to play the game
"""
# Initialize a list to store the values
board = [
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3']
]
# Define a function to display the board
def displayBoard():
    for row in board:
        print(row[0],'|',row[1],'|',row[2])
        if row == board[2]:
            continue
        print('-'*9)

displayBoard()  
for i in range(3):
    player1 = str(input('Player 1. Do you want to be X or O?\n'))
    player1 = player1.upper()
    if player1 == 'X' or player1 == 'O':
        break
    else:
        if i == 2:
            print("Sorry. Out of trys. Better luck next time")
            break
        print('Invalid input! Try again')

game_ended = False

# Check for winner
def checkWin():
    global game_ended
    if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        print("Player",board[2][0], "has won")
        game_ended = True
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        print("Player",board[1][0], "has won")
        game_ended = True
    elif board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        print("Player",board[0][0], "has won")
        game_ended = True
    elif board[2][0] == board[1][0] and board[2][0] == board[0][0]:
        print("Player",board[2][0], "has won")
        game_ended = True
    elif board[2][1] == board[1][1] and board[2][1] == board[0][1]:
        print("Player",board[2][1], "has won")
        game_ended = True
    elif board[2][2] == board[1][2] and board[2][2] == board[0][2]:
        print("Player",board[2][2], "has won")
        game_ended = True
    elif board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        print("Player",board[2][0], "has won")
        game_ended = True
    elif board[2][2] == board[1][1] and board[2][2] == board[0][0]:
        print("Player",board[2][2], "has won")   
        game_ended = True

while(not game_ended):
    pstn = int(input('Player, select position: '))
    if pstn == 1:
        if board[2][0] == 'X' or board[2][0] == 'O':
            print("Sorry, position already occupied, please choose another position")
            continue
        else:
            board[2][0] = player1
        displayBoard()
        checkWin()
    elif pstn == 2:
        if board[2][1] == 'X' or board[2][1] == 'O':
            print("Sorry, position already occupied, please choose another position")
            continue
        else:
            board[2][1] = player1
        displayBoard()
        checkWin()
    elif pstn == 3:
        if board[2][2] == 'X' or board[2][2] == 'O':
            print("Sorry, position already occupied, please choose another position")
            continue
        else:
            board[2][2] = player1
        displayBoard()
        checkWin()
    elif pstn == 4:
        if board[1][0] == 'X' or board[1][0] == 'O':
            print("Sorry, position already occupied, please choose another position")
            continue
        else:
            board[1][0] = player1
        displayBoard()
        checkWin()
    elif pstn == 5:
        if board[1][1] == 'X' or board[1][1] == 'O':
            print("Sorry, position already occupied, please choose another position")
            continue
        else:
            board[1][1] = player1
        displayBoard()
        checkWin()
    elif pstn == 6:
        if board[1][2] == 'X' or board[1][2] == 'O':
            print("Sorry, position already occupied, please choose another position")
            continue
        else:
            board[1][2] = player1
        displayBoard()
        checkWin()
    elif pstn == 7:
        if board[0][0] == 'X' or board[0][0] == 'O':
            print("Sorry, position already occupied, please choose another position")
            continue
        else:
            board[0][0] = player1
        displayBoard()
        checkWin()
    elif pstn == 8:
        if board[0][1] == 'X' or board[0][1] == 'O':
            print("Sorry, position already occupied, please choose another position")
            continue
        else:
            board[0][1] = player1
        displayBoard()
        checkWin()
    elif pstn == 9:
        if board[0][2] == 'X' or board[0][2] == 'O':
            print("Sorry, position already occupied, please choose another position")
            continue
        else:
            board[0][2] = player1
        displayBoard()
        checkWin()
    else:
        print("Invalid input! Please try again")
        continue
    if player1 == 'X':
        player1 = 'O'
    else:
        player1 = 'X'
    