from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSort(self):
        visited = [False] * self.v
        stack = []
        for i in self.graph:
            self.DFS(i, visited, stack)
        while len(stack):
            print((stack.pop()), end=" ")

    def DFS(self, node, visited, stack):
        visited[chr(node)] = True
        for neighbor in self.graph[node]:
            self.DFS(neighbor, visited, stack)
        stack.append(node)

    def printOrder(self, words, n):
        for i in range(n - 1):
            word1 = words[i]
            word2 = words[i + 1]
            j = 0
            while 0 <= j < min(len(word1), len(word2)):
                if word1[j] != word2[j]:
                    print(word1[j], word2[j])
                    self.addEdge(word1[j], word2[j])
                    # print(self.graph)
                    break
                j = j + 1
        self.topologicalSort()


if __name__ == '__main__':
    words = ["caa", "aaa", "aab"]
    g = Graph(3)
    g.printOrder(words, 3)
