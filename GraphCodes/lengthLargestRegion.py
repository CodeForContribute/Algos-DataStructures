# Time Complexity:O(m*n)

def largestRegion(M):
    global ROW, COL
    visited = [[0] * COL for i in range(ROW)]
    result = -999999999999
    for i in range(ROW):
        for j in range(COL):
            if M[i][j] and not visited[i][j]:
                count = [1]
                DFS(M, i, j, visited, count)
                result = max(result, count[0])

    return result


def isSafe(Matrix, row, col, visited):
    global ROW, COL
    return (0 <= row < ROW) and (0 <= col < COL) and (Matrix[row][col] and not visited[row][col])


def DFS(Matrix, row, col, visited, count):
    rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
    visited[row][col] = True
    for k in range(8):
        if isSafe(Matrix, row + rowNbr[k], col + colNbr[k], visited):
            count[0] += 1
            DFS(Matrix, row + rowNbr[k], col + colNbr[k], visited, count)


if __name__ == '__main__':
    ROW = 4
    COL = 5

    M = [[0, 0, 1, 1, 0],
         [1, 0, 1, 1, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1]]

    print(largestRegion(M))
