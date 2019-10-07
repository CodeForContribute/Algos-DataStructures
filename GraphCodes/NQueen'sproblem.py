global N
N = 4


def printSolution(solution):
    for i in solution:
        for j in i:
            print(j, end=" ")
        print(" ")


def isSafe(chessBoard, row, col):
    for _ in range(col):
        # check for row on left side
        if chessBoard[row][_] == 1:
            return False
        # check for upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if chessBoard[i][j] == 1:
                return False
        # check for lower diagonal on left side
        for i, j in zip(range(row, N, -1), range(col, -1, -1)):
            if chessBoard[i][j] == 1:
                return False
    return True


def solveNQueenProblem(chessboard, col):
    if not solveNQueenProblemUtil(chessboard, col):
        print("No solution exists")
        return False
    else:
        printSolution(chessboard)
        return True


def solveNQueenProblemUtil(chessboard, col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(chessboard, i, col):
            chessboard[i][col] = 1
            if solveNQueenProblemUtil(chessboard, col + 1):
                return True
            chessboard[i][col] = 0
    return False


# Optimised Solution
# col = [0]*30
# N= 4
# def printSolution(board):
#     for i in range(N):
#         for j in range(N):
#             print(board[i][j],end=" ")
#         print(" ")
#
# def solveNQueen(board, col):
#     if not solveNQueenUtil(board, col):
#         print("Solution does not exist")
#         return False
#     else:
#         printSolution(board)
#         return True
#
# def solveNQueenUtil(board,col):
#     if col >= N:
#         return True
#     for i in range(N):
#         if board[i-col]


if __name__ == '__main__':
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    solveNQueenProblem(board, 0)
