import random

board = [' ' for x in range (10)]

def letter_insert(letter, pos):
    board[pos] = letter

def empty_space(pos):
    return board[pos] == ' '
def board_print(board):
    print("    |    |")
    print(" " + board[1] + "  |  " + board[2] + " | " + board[3])
    print("    |    |")
    print("---------------")
    print("    |    |")
    print(" " + board[4] + "  |  " + board[5] + " | " + board[6])
    print("    |    |")
    print("---------------")
    print("    |    |")
    print(" " + board[7] + "  |  " + board[8] + " | " + board[9])

def winner(boards, lenght):
    return ((boards[7] == lenght and boards[8] == lenght and boards[9] == lenght) or
    (boards[4] == lenght and boards[5] == lenght and boards[6] == lenght) or
    (boards[1] == lenght and boards[2] == lenght and boards[3] == lenght) or 
    (boards[1] == lenght and boards[4] == lenght and boards[7] == lenght) or
    (boards[2] == lenght and boards[5] == lenght and boards[8] == lenght) or
    (boards[3] == lenght and boards[6] == lenght and boards[6] == lenght) or
    (boards[1] == lenght and boards[5] == lenght and boards[9] == lenght) or
    (boards[3] == lenght and boards[5] == lenght and boards[7] == lenght))
def move_player():
    run = True
    while run:
        move_next = input("input for X (1-9): ")
        try:
            move_next = int(move_next)
            if move_next > 0 and move_next <10:
                if empty_space(move_next):
                    run = False
                    letter_insert("X", move_next)
                else:
                    print("this space is occupied")
            else:
                print("please type a number within the range")
        except:
            print("type a number please")
def move_ai():
    moves_possible = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    for let in ["O", "x"]:
        for i in moves_possible:
            boardCopy = board[:]
            boardCopy[i] = let
            if winner(boardCopy, let):
                move = i
                return move
            
    cornersOpen = []
    for i in moves_possible:
        if i in[1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = random_select(cornersOpen)
        return move
    
    if 5 in moves_possible:
        move = 5
        return move
    
    edgesopen = []
    for i in moves_possible:
        if i in[1,3,7,9]:
            edgesopen.apped(i)

    if len(edgesopen) > 0:
        move = random_select(cornersOpen)
        
    return move
def random_select(li):
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def board_full(board):
    if board.count(" ") > 1:
        return False
    else:
        return True
def main():
    print("welcome to tic tac toe")
    board_print(board)

    while not(board_full(board)):
        if not(winner(board, "O")):
            move_player()
            board_print(board)
        else:
            print("O Wins")
            break
        if not(winner(board, "X")):
            move = move_ai()
            if move == 0:
                print("tie game")
            else:
                letter_insert("O", move)
                print("Opponent place an O in position", move, ":")
                board_print(board)
        else:
            print("X wins")
            break
    if board_full(board):
        print("TIE")
main()