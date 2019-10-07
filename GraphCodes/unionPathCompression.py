from collections import defaultdict


class subSet:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


###### Time Complexity:O(log(n)) ##########################################################################
class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def findParent(self, subsets, node):
        if subsets[node].parent != node:
            subsets[node].parent = self.findParent(subsets, subsets[node].parent)
        return subsets[node].parent

    def union(self, subsets, node1, node2):
        if subsets[node1].rank > subsets[node2].rank:
            subsets[node2].parent = node1
        elif subsets[node2].rank > subsets[node1].rank:
            subsets[node1].parent = node2
        else:
            subsets[node2].parent = node1
            subsets[node1].rank += 1

    def isCycle(self):
        subSets = []
        for i in range(self.v):
            subSets.append(subSet(i, 0))
        for u in self.graph:
            u_rep = self.findParent(subSets, u)
            for v in self.graph[u]:
                v_rep = self.findParent(subSets, v)
                if u_rep == v_rep:
                    return True
                else:
                    self.union(subSets, u_rep, v_rep)


if __name__ == '__main__':
    g = Graph(3)

    # add edge 0-1
    g.addEdge(0, 1)

    # add edge 1-2
    g.addEdge(1, 2)

    # add edge 0-2
    g.addEdge(0, 2)

    if g.isCycle():
        print('Graph contains cycle')
    else:
        print('Graph does not contain cycle')
