def main() :
    current_player = next_player(" ")
    board = make_board()
    
    win_status = game_is_won(board)

    while win_status == "n/a" :
        show_board(board)
        make_move(current_player, board)

    if win_status == "x" :
        show_board(board)
        print("Good game! Player x won!")

    elif win_status == "o" :
        show_board(board)
        print("Good game! Player o won!")

def make_board() :
    board = []
    for space in range(16) :
        board.append(space + 1)
    
    return board

def show_board(board) :
    print(f"\n0{board[0]}|0{board[1]}|0{board[2]}|0{board[3]}")
    print("--+--+--+--")
    print(f"0{board[4]}|0{board[5]}|0{board[6]}|0{board[7]}")
    print("--+--+--+--")
    print(f"0{board[8]}|{board[9]}|{board[10]}|{board[11]}")
    print("--+--+--+--")
    print(f"{board[12]}|{board[13]}|{board[14]}|{board[15]}\n")

def game_is_draw(board) :
    for space in range(16) :
        if board[space] != "o" and board[space] != "x" :
            return False
    return True

def game_is_won(space) :
    if space[0] == space[1] == space[2] == space[3] == "x" or space[4] == space[5] == space[6] == space[7] == "x" or space[8] == space[9] == space[10] == space[11] == "x" or space[12] == space[13] == space[14] == space[15] == "x" or space[0] == space[4] == space[8] == space[12] == "x" or space[1] == space[5] == space[9] == space[13] == "x" or space[2] == space[6] == space[10] == space[14] == "x" or space[3] == space[7] == space[11] == space[15] == "x" or space[0] == space[5] == space[10] == space[15] == "x" or space[3] == space[6] == space[9] == space[12] == "x" :
        return "x"

    elif space[0] == space[1] == space[2] == space[3] == "o" or space[4] == space[5] == space[6] == space[7] == "o" or space[8] == space[9] == space[10] == space[11] == "o" or space[12] == space[13] == space[14] == space[15] == "o" or space[0] == space[4] == space[8] == space[12] == "o" or space[1] == space[5] == space[9] == space[13] == "o" or space[2] == space[6] == space[10] == space[14] == "o" or space[3] == space[7] == space[11] == space[15] == "o" or space[0] == space[5] == space[10] == space[15] == "o" or space[3] == space[6] == space[9] == space[12] == "o" :
        return "o"

    else :
        return "n/a"

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