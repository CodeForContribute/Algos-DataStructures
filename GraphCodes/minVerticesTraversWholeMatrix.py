from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def dfs(self, n, m, visited, adj, N, M):
        visited[n][m] = True
        ##### Below neighbor
        if n + 1 < N and adj[n][m] >= adj[n + 1][m] and not visited[n + 1][m]:
            self.dfs(n + 1, m, visited, adj, N, M)
        ###### Right neighbor
        if m + 1 < M and adj[n][m] >= adj[n][m + 1] and not visited[n][m + 1]:
            self.dfs(n, m + 1, visited, adj, N, M)
        ###### above neighbor
        if n - 1 >= 0 and adj[n][m] >= adj[n - 1][m] and not visited[n - 1][m]:
            self.dfs(n - 1, m, visited, adj, N, M)
        ###### left neighbor
        if m - 1 >= 0 and adj[n][m] >= adj[n][m - 1] and not visited[n][m - 1]:
            self.dfs(n, m - 1, visited, adj, N, M)

    def printMinSource(self, adj, N, M):
        AllPairs = []
        for i in range(M):
            for j in range(N):
                AllPairs.append([adj[i][j], [i, j]])
        AllPairs.sort()
        AllPairs.reverse()
        visited = [[False for i in range(N)] for j in range(M)]
        for i in AllPairs:
            if not visited[i[1][0]][i[1][1]]:
                print(i[1][0], i[1][1])
                self.dfs(i[1][0], i[1][1], visited, adj, N, M)


if __name__ == '__main__':
    n = 3
    m = 3
    adj = [
        # [3, 3],
        # [1, 1]
        [1, 2, 3],
        [2, 3, 1],
        [1, 1, 1]
    ]
    g = Graph()
    g.printMinSource(adj, n, m)
