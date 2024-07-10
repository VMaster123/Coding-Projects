
import math
board=[['     ' for _ in range(3)] for _ in range(3)]
print(board)
player_choice = 0
def printBoard(board):
    for row in board:
        print("|".join(row))
        print("-----|-----|-----")

printBoard(board)


def gameWin(board,symbol,row,column):
    count_row = 0
    count_column = 0
    count_diagonal1 = 0
    count_diagonal2 = 0
    try:
        for i in range(3):
            if(board[row][i] == symbol):
                count_row += 1
            if(board[i][column] == symbol  ):
                count_column += 1
            if(board[i][i] == symbol ):
                count_diagonal1 += 1
            if(board[i][2-i] == symbol):
                count_diagonal2 += 1
        
        if(count_row == 3 or count_column == 3 or  count_diagonal1 == 3 or count_diagonal2 == 3):
            return True 
    except:
        pass

    return False


def player_turn():
    turn_counter = 0  
    gameRunning = True
    while gameRunning :
        
        try:
            player_choice = int(input("Place Block Where"))
            row = math.floor((player_choice-1)/3)
            column = (player_choice %3 + 2) %3

            if(board[row][column] != '     '):
                print("Try Again, space already there")
                continue

            elif( player_choice < 1 or player_choice > 9 ) :
                print("Only pick num from 1 to 9")
                continue

            elif(turn_counter % 2 == 0):
                symbol = '  X  '

            else:
                symbol = '  O  '
            
            board[row][column] = symbol
            turn_counter += 1
            printBoard(board)

            

            if gameWin(board, symbol, row, column):
                print(f"{symbol} Wins!")
                gameRunning = False
                  

            if turn_counter == 9: 
                print("It's a Tie!")
                gameRunning = False
                           

        except ValueError:
            print(player_choice)
            print(type(player_choice))
            print("Try again, not valid input ")



while(True):
    player_turn()
    break













