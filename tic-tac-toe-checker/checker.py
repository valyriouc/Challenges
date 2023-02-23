def is_solved(board):
    def check_state(board, number):
        return ((board[0][0] == number and board[0][1] == number and board[0][2] == number) or
        (board[1][0] == number and board[1][1] == number and board[1][2] == number) or
        (board[2][0] == number and board[2][1] == number and board[2][2] == number) or
        (board[0][0] == number and board[1][0] == number and board[2][0] == number) or
        (board[0][1] == number and board[1][1] == number and board[2][1] == number) or
        (board[0][2] == number and board[1][2] == number and board[2][2] == number) or
        (board[0][0] == number and board[1][1] == number and board[2][2] == number) or
        (board[2][0] == number and board[1][1] == number and board[0][2] == number))
    if (check_state(board, 1)):
        return 1
    elif (check_state(board, 2)):
        return 2
    elif(not check_state(board, 1) and not check_state(board, 2)):
        for y in range(0, 3):
            for x in range(0, 3):
                if (board[y][x] == 0):
                    return -1
    return 0
    
                