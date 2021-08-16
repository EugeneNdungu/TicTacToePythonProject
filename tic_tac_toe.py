"""
The program is a tic tac toe game that allows to players to play the game
"""
# Initialize a dictionary to store the values
board = {'7':' ','8':' ','9':' ',
         '4':' ','5':' ','6':' ',
         '1':' ','2':' ','3':' '
        }
# Define a function to display the board
def displayBoard():
    print(board['7'] + '|' + board['8'] + '|' +board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' +board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' +board['3'])

displayBoard() 

def game():
    game_ended = False
    count = 0
    for i in range(3):
        player1 = str(input('Player 1. Do you want to be X or O?\n'))
        player1 = player1.upper()
        if player1 == 'X' or player1 == 'O':
            break
        else:
            if i == 2:
                print("Sorry. Out of trys. Better luck next time")
                game_ended = True
                break
            print('Invalid input! Try again')

    # Check for winner


    while(not game_ended):
        pstn = str(input('Player '  + player1 + ', select position: '))
        # Check to see if the position is filled
        if board[pstn] == ' ':
            board[pstn] = player1
            if player1 == 'X':
                player1 = 'O'
            else:
                player1 = 'X'
            count += 1
            displayBoard()
        elif board[pstn] == 'X' or board[pstn] == 'O':
            print('Sorry, that position has been filled. Please try again')
            continue

        if count >= 5:
            if board['1'] == board['2'] == board['3'] != ' ':
                print('Player', board['1'], 'has won the game.')
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                print('Player', board['4'], 'has won the game.')
                break
            elif board['7'] == board['8'] == board['9'] != ' ':
                print('Player', board['7'], 'has won the game.')
                break
            elif board['1'] == board['4'] == board['7'] != ' ':
                print('Player', board['1'], 'has won the game.')
                break
            elif board['2'] == board['5'] == board['8'] != ' ':
                print('Player', board['2'], 'has won the game.')
                break
            elif board['3'] == board['6'] == board['9'] != ' ':
                print('Player', board['3'], 'has won the game.')
                break
            elif board['1'] == board['5'] == board['9'] != ' ':
                print('Player', board['1'], 'has won the game.')
                break
            elif board['3'] == board['5'] == board['7'] != ' ':
                print('Player', board['3'], 'has won the game.')
                break
            elif count == 9:
                print('Game is a tie')
    #  Clear the board
    for key in board:
        board[key] = ' '
    # Ak if they want to play again
    play_again = str(input("Do you want to play again? \n"))
    play_again = play_again.upper()
    if play_again == 'Y':
        game()

if __name__ == "__main__":
    game()