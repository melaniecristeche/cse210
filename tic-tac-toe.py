def main():
    lets_play = player_turn("")
    create_board = board()
    while not (you_win(create_board) or draw(create_board)):
        display(create_board)
        player_move(lets_play, create_board)
        lets_play = player_turn(lets_play)
    display(create_board)
    print("\nGood game!! You are amazing!. Thanks for playing!")

def board():
    board = []
    for space in range(9):
        board.append(space + 1)
    return board

def display(board):
    print("\n %s | %s | %s" %(board[0], board[1], board[2]))
    print('---+---+---')
    print(" %s | %s | %s" %(board[3], board[4], board[5]))
    print('---+---+---')
    print(" %s | %s | %s" %(board[6], board[7], board[8]))

def you_win(board):
    return (board[0] == board[1]== board[2] or 
            board[3] == board[4] == board[5] or 
            board[6] == board[7] == board[8] or 
            board[0] == board[3] == board[6] or 
            board[1] == board[4] == board[7] or 
            board[2] == board[5] == board[8] or 
            board[2] == board[4] == board[6] or 
            board[0] == board[4] == board[8])

def draw(board):
    for space in range(9):
        if board[space] != "x" and board[space] != "o":
            return False
    return True 


def player_move(player, board):
    space = int(input(f"\n{player}'s turn to choose a space (1-9): "))
    board[space - 1] = player

def player_turn(turn):
    if turn == "" or turn == "o":
        return "x"
    elif turn == "x":
        return "o"

if __name__ == "__main__":
    main()
