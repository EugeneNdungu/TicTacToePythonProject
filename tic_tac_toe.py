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
    if player1 == 'X':
        player2 = 'O'
        break
    elif player1 == 'O':
        player2 = 'X'
        break
    else:
        if i == 2:
            print("Sorry. Out of trys. Better luck next time")
            break
        print('Invalid input! Try again')

pstn = int(input('Player1, select position: '))
if pstn == 1:
    if board[2][0] == 'X' or board[2][0] == 'O':
        print("Sorry, position already occupied, please choose another position")
    else:
        board[2][0] = player1
    displayBoard()
