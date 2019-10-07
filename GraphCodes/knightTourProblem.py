n = 8


def isSafe(x, y, board):
    if 0 <= x < n and 0 <= y < n and board[x][y] == -1:
        return True
    return False


def printSolution(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def solveKT():
    board = [[-1 for i in range(n)] for i in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0
    pos = 1
    if not solveKTUtil(board, 0, 0, move_x, move_y, pos):
        print("No solution Exists")
    else:
        printSolution(board)


def solveKTUtil(board, current_x, current_y, move_x, move_y, pos):
    if pos == n ** 2:
        return True

    for i in range(8):
        new_current_x = current_x + move_x[i]
        new_current_y = current_y + move_y[i]
        if isSafe(new_current_x, new_current_y, board):
            board[new_current_x][new_current_y] = pos
            if solveKTUtil(board, new_current_x, new_current_y, move_x, move_y, pos + 1):
                return True
            board[new_current_x][new_current_y] = -1
    return False


if __name__ == "__main__":
    solveKT()
