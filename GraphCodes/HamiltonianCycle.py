class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for _ in range(self.v)] for _ in range(self.v)]

    def isSafe(self, v, pos, path):
        # Here pos indicates the last visited vertex in path array
        # So for a safe path there should be an edge between the last visited vertex and current vertex
        if self.graph[path[pos - 1]][v] == 0:
            return False
        for vertex in path:
            if vertex == v:
                return False
        return True

    def hamCycle(self, s):
        """
        https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/
        :param s: source node
        :return: path for Ham Cycle if any or return False
        """
        path = [-1 for i in range(self.v)]
        path[0] = s
        if self.hamCycleUtil(path, 1):
            for i in path:
                print(i, end=" ")
            return True
        else:
            print("No Hamoltonian Cycle exists in the graph")
            return False

    def hamCycleUtil(self, path, pos):
        # if pos becomes equal to the number of vertices then check for the last seen vertex connects to the first vertex of the graph
        if pos == self.v:
            if self.graph[path[pos - 1]][0] == 1:
                return True
            else:
                return False
        for v in range(0, self.v):
            if self.isSafe(v, pos, path):
                path[pos] = v
                if self.hamCycleUtil(path, pos + 1):
                    return True
                path[pos] = -1
        return False


if __name__ == '__main__':
    # Driver Code 

    ''' Let us create the following graph 
          (0)--(1)--(2) 
           |   / \   | 
           |  /   \  | 
           | /     \ | 
          (3)-------(4)    '''
    g1 = Graph(5)
    g1.graph = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
                [0, 1, 0, 0, 1, ], [1, 1, 0, 0, 1],
                [0, 1, 1, 1, 0], ]

    # Print the solution
    s = 0
    g1.hamCycle(s)
    print()
    ''' Let us create the following graph 
          (0)--(1)--(2) 
           |   / \   | 
           |  /   \  | 
           | /     \ | 
          (3)       (4)    '''
    g2 = Graph(5)
    g2.graph = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
                [0, 1, 0, 0, 1, ], [1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0], ]

    # Print the solution 
    g2.hamCycle(s)
