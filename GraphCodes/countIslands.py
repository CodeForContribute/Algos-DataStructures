# Time complexity: O(ROW x COL
class Graph:
    def __init__(self, row, col, graph):
        self.row = row
        self.col = col
        self.graph = graph

    def isSafe(self, i, j, visited):
        if 0 <= i < self.row and 0 <= j < self.col and self.graph[i][j] and not visited[i][j]:
            return True
        return False

    def DFS(self, i, j, visited):
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[i][j] = True
        for p in range(8):
            if self.isSafe(i + rowNbr[p], j + colNbr[p], visited):
                self.DFS(i + rowNbr[p], j + colNbr[p], visited)

    def CountIslands(self):
        visited = [[False] * self.row for i in range(self.col)]
        count = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.graph[i][j] and not visited[i][j]:
                    self.DFS(i, j, visited)
                    count += 1
        return count


if __name__ == '__main__':
    graph = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]

    row = len(graph)
    col = len(graph[0])

    g = Graph(row, col, graph)

    print("Number of islands is:")
    print(g.CountIslands())
