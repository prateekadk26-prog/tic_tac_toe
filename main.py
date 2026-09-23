import winsound

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    
   
   
def check_result(board):
    if(board[0] == board[1] == board[2] and board[0] != " " ):
        return True
    elif (board[3] == board[4] == board[5] and board[3] !=" " ):
        return True
    elif (board[6] == board[7] == board[8] and board[6] !=" " ):
        return True   
    elif (board[0] == board[3] == board[6] and board[0] !=" "):
        return True
    elif (board[1] == board[4] == board[7] and board[1] !=" "):
        return True
    elif (board[2] == board[5] == board[8] and board[2] !=" "):
        return True
    elif (board[0] == board[4] == board[8] and board[0] !=" "):
        return True   
    elif (board[2] == board[4] == board[6] and board[2] !=" "):
        return True
    else:
        return False

def check(board,position1, position2):
    if board[position1] == board[position2] or board[position2] == board[position1]:
        print("Invalid position")  

def make_move(board,player1,position):
    position = position-1
    if board[position] != " ":
        print("Position is already taken")
        return False
    else:
        board[position] = player1

        return True

def enter1(player1,board):
    while True:
        try:
            position1 = int(input("Enter a position for player X (1 to 9 ): "))
        except ValueError:
            print("please enter a number")
            continue

        if(position1 <= 0 or position1 >=10):
            print("Invalid position")
            # return False
            continue
        if make_move(board, player1, position1):
            print_board(board)            
            break

def enter2(player2, board):
    while True:
        try:
            position2 = int(input("Enter a position for player(O)(1 to 9 ): "))
        except ValueError:
            print("please enter a number")
            continue

        if(position2 <= 0 or position2 >=10):
            print("Invalid position")
            continue
        if make_move(board, player2, position2):
            print_board(board)

            print("\n \n \n")
            break

def reset_board():
    return [" "," "," ",
        " "," "," ",
        " "," "," "]



board = [" "," "," ",
        " "," "," ",
        " "," "," "]


player1="X"
player2 = "O"
while True:
    enter1(player1,board)
    winner = check_result(board)
    if winner:
        print(f"Player {player1} won the game")
        winsound.Beep(1000, 400)
        board = reset_board()
        print_board(board)
        continue
    enter2(player2, board)
    winner = check_result(board)
    if winner:
        print(f"Player {player2} won the game")
        winsound.Beep(1000, 400)
        board = reset_board()
        print_board(board)
        continue