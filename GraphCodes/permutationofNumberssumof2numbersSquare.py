def isSafe(graph, v, path, pos, ):
    if graph[path[pos - 1]][v] == 0:
        return False
    for i in range(pos):
        if path[i] == v:
            return False
    return True


def HamPath(n):
    """
    https://www.geeksforgeeks.org/permutation-numbers-sum-two-consecutive-numbers-perfect-square/
    :param n:
    :return:
    """
    if n == 1:
        return 'No Solution'
    arr = []
    # Form an array which contains the perfect square and sum of all pair of combinations of 2
    # numbers are less than the last element of this array
    for i in range(1, int((2 * (n - 1)) ** 0.5) + 1):
        arr.append(i ** 2)
    # initialise an adjacency matrix
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # Forming a adjacency matrix where value is 1 if a pair's sum forms a perfect square
    for i in range(1, n + 1):
        for element in arr:
            if 0 < element - i <= n and 2 ** i != element:
                graph[i][element - i] = 1
                graph[element - i][i] = 1

    # Find the Hamalotonian Cycle/path return False if there is not any path found
    for j in range(1, n + 1):
        path = [-1 for _ in range(n + 1)]
        path[1] = j
        if formPath(graph, path, 2):
            return path[1:]
    return "No solution"


def formPath(graph, path, pos):
    n = len(graph) - 1
    if pos == n + 1:
        return True
    for v in range(1, n + 1):
        if isSafe(graph, v, path, pos):
            path[pos] = v
            if formPath(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False


if __name__ == '__main__':
    print(17, '->', HamPath(17))
    print(20, '->', HamPath(20))
    # print(25, '->', HamPath(25))
