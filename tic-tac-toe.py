def main() :
    current_player = next_player(" ")
    board = make_board()
    
    win_status = game_is_won(board)

    while not (game_is_won(board) or game_is_draw(board)) :
        show_board(board)
        make_move(current_player, board)
        current_player = next_player(current_player)

    show_board(board)
    print("GGs, feel free to now brag about winning to your opponent!")


def make_board() :
    board = []
    for space in range(16) :
        board.append(space + 1)
    
    return board

def show_board(board) :
    print(f"\n{board[0]}|{board[1]}|{board[2]}|{board[3]}")
    print(f"{board[4]}|{board[5]}|{board[6]}|{board[7]}")
    print(f"{board[8]}|{board[9]}|{board[10]}|{board[11]}")
    print(f"{board[12]}|{board[13]}|{board[14]}|{board[15]}\n")

def game_is_draw(board) :
    for space in range(16) :
        if board[space] != "o" and board[space] != "x" :
            return False
    return True

def game_is_won(space) :
    return (space[0] == space[1] == space[2] == space[3] or space[4] == space[5] == space[6] == space[7] or space[8] == space[9] == space[10] == space[11] or space[12] == space[13] == space[14] == space[15] or space[0] == space[4] == space[8] == space[12] or space[1] == space[5] == space[9] == space[13] or space[2] == space[6] == space[10] == space[14] or space[3] == space[7] == space[11] == space[15] or space[0] == space[5] == space[10] == space[15] or space[3] == space[6] == space[9] == space[12])

def make_move(player, board) :
    space = int(input(f"{player}'s turn to choose a space (1-16)"))
    board[space - 1] = player

def next_player(current_player) :
    if current_player == " " or current_player == "o" :
        return "x"
    
    elif current_player == "x" :
        return "o"


if __name__ == "__main__":
    main()