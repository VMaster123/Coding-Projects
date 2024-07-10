# Major Help from https://www.youtube.com/watch?v=trKjYdBASyQ&ab_channel=TheCodingTrain
import math
noRestart = True 
gameRunning = True
def gameBeginning():
    global turn_counter
    global gameRunning
    global board
    global player_choice

    
    turn_counter = 0
    gameRunning = True

    board=[['     ' for _ in range(3)] for _ in range(3)]

    player_choice = 0

    
    print("Wellcome,lets play tic-tac-toe")
    print("------------------------")


def printBoard(board):
    for row in board:
        print("|".join(row))
        print("-----|-----|-----")






def gameWin(board, symbol):
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)):
            return True
    
    for i in range(3):
        if all(board[j][i] == symbol for j in range(3)):
            return True
    
    if all(board[i][i] == symbol for i in range(3)):
        return True
    
    elif all(board[i][2 - i] == symbol for i in range(3)):
        return True
    
    return False

def player_turn(): 
    global noRestart
    global turn_counter
    global gameRunning
    if(gameRunning):
        flag = 1
        while(flag == 1):
            try:
                player_choice = int(input("Place Block Where: "))
                row = math.floor((player_choice-1)/3)
                column = (player_choice % 3 + 2) % 3
                    
                if(board[row][column] != '     '):
                    print("Try Again, space already there")
                    flag = 1

                elif( player_choice < 1 or player_choice > 9 ) :
                    print("Only pick num from 1 to 9")
                    flag = 1
                else:
                    flag = 0

            except ValueError:
                print("Try again, not valid input ")

        symbol = '  X  '
        board[row][column] = symbol

        turn_counter += 1

        gameWinner(symbol)

            

def gameWinner(symbol):
    global turn_counter
    global gameRunning

    

    if gameWin(board, symbol):
        print(f"{symbol} Wins!")
        gameRunning = False
        printBoard(board)

    elif(turn_counter == 9):
        print("Tie !")
        gameRunning = False
        printBoard(board)
    elif(turn_counter % 2 == 0):
        printBoard(board)
            





def ai_turn():
    global gameRunning
    global turn_counter

    symbol =  '  O  '
    if(gameRunning):
        best_score = -100000000 
        bestmove = None
        for i in range(3):
            for j in range(3):

                if board[i][j] == '     ' :
                    board[i][j] = symbol
                    score = minimax(board,0,False)
                    board[i][j] = '     '

                    if(score > best_score) :
                        best_score = score
                        bestmove = [i,j]

        if bestmove is not None:
            board[bestmove[0]][bestmove[1]] = symbol

            turn_counter += 1
            
            gameWinner(symbol)
            
    



def minimax(board, depth, isMaximizing):


    if gameWin(board, '  X  ') :
        return -1000
    elif gameWin(board, '  O  ') : 
        return  1000
    elif depth == 9:
         return 0


    if(isMaximizing):
        best_score =  -100000000 
        symbol =  '  X  '

    
    else:
        best_score =  100000000 
        symbol =  '  O  '
    for i in range(3):
        for j in range(3):

            if board[i][j] == '     ' :
                board[i][j] = symbol
                score = minimax(board,depth + 1, True)
                board[i][j] = '     '

                if isMaximizing:
                    best_score = max(score, best_score)
                else:
                    best_score = min(score, best_score)


    return best_score




while(noRestart):
    gameBeginning()

    while(gameRunning):     
        player_turn()
        ai_turn()

    
    flag_2 = True

    while flag_2:
        again = input("Play again? ")
        if again.lower().strip() == "yes" :
            gameRunning = True
            flag_2 = False

        elif again.lower().strip() == "no":
            noRestart = False
            flag_2 = False

        else:
            print("Not a good answer")










