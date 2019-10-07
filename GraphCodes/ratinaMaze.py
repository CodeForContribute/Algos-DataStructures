N = 4


def printSolution(solution):
    for i in solution:
        for j in i:
            print(j, end=" ")
        print(" ")


def isSafe(x, y, maze):
    if N > x >= 0 and N > y >= 0 and maze[x][y] == 1:
        return True
    return False


def solveRatInaMaze(maze):
    solution = [[0 for i in range(4)] for _ in range(4)]
    if solveRatInaMazeUtil(maze, 0, 0, solution) is False:
        print("No solution exists")
        return False
    else:
        printSolution(solution)
        return True


def solveRatInaMazeUtil(maze, x, y, solution):
    # Base Condition
    if x == N - 1 and y == N - 1:
        solution[x][y] = 1
        return True
    # iteration to check weather a given position is safe or not
    if isSafe(x, y, maze):
        solution[x][y] = 1
        if solveRatInaMazeUtil(maze, x + 1, y, solution):
            return True
        if solveRatInaMazeUtil(maze, x, y + 1, solution):
            return True
        # remove the position which doesn't lead to the solution
        solution[x][y] = 0
        return False


if __name__ == '__main__':
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]

    solveRatInaMaze(maze)
