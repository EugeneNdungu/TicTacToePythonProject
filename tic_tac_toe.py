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