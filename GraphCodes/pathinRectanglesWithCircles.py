import math


def isPossible(m, n, k, r, X, Y):
    rect = [[0] * n for i in range(m)]

    # Now using Pythagorean theorem find if a
    # cell touches or within any circle or not.
    for i in range(m):
        for j in range(n):
            for p in range(k):
                if (math.sqrt((pow((X[p] - 1 - i), 2) +
                               pow((Y[p] - 1 - j), 2))) <= r):
                    rect[i][j] = -1

    # If the starting cell comes within
    # any circle return false.
    if rect[0][0] == -1:
        return False
    q = []
    rect[0][0] = 1
    q.append([0, 0])
    while len(q):
        arr = q.pop(0)
        elex = arr[0]
        eley = arr[1]

        if ((elex > 0) and (eley > 0) and
                (rect[elex - 1][eley - 1] == 0)):
            rect[elex - 1][eley - 1] = 1
            v = [elex - 1, eley - 1]
            q.append(v)

            # check top cell  
        if ((elex > 0) and
                (rect[elex - 1][eley] == 0)):
            rect[elex - 1][eley] = 1
            v = [elex - 1, eley]
            q.append(v)

            # check top-right cell  
        if ((elex > 0) and (eley < n - 1) and
                (rect[elex - 1][eley + 1] == 0)):
            rect[elex - 1][eley + 1] = 1
            v = [elex - 1, eley + 1]
            q.append(v)

            # check left cell  
        if ((eley > 0) and
                (rect[elex][eley - 1] == 0)):
            rect[elex][eley - 1] = 1
            v = [elex, eley - 1]
            q.append(v)

            # check right cell  
        if ((eley > n - 1) and
                (rect[elex][eley + 1] == 0)):
            rect[elex][eley + 1] = 1
            v = [elex, eley + 1]
            q.append(v)

            # check bottom-left cell  
        if ((elex < m - 1) and (eley > 0) and
                (rect[elex + 1][eley - 1] == 0)):
            rect[elex + 1][eley - 1] = 1
            v = [elex + 1, eley - 1]
            q.append(v)

            # check bottom cell  
        if ((elex < m - 1) and
                (rect[elex + 1][eley] == 0)):
            rect[elex + 1][eley] = 1
            v = [elex + 1, eley]
            q.append(v)

            # check bottom-right cell  
        if ((elex < m - 1) and (eley < n - 1) and
                (rect[elex + 1][eley + 1] == 0)):
            rect[elex + 1][eley + 1] = 1
            v = [elex + 1, eley + 1]
            q.append(v)

            # Now if the end cell (i.e. bottom right cell)  
            # is 1(reachable) then we will send true.  
    return rect[m - 1][n - 1] == 1


if __name__ == '__main__':

    # Test case 1
    m1 = 5
    n1 = 5
    k1 = 2
    r1 = 1
    X1 = [1, 3]
    Y1 = [3, 3]
    if isPossible(m1, n1, k1, r1, X1, Y1):
        print("Possible")
    else:
        print("Not Possible")

    m2 = 5
    n2 = 5
    k2 = 2
    r2 = 1
    X2 = [1, 1]
    Y2 = [2, 3]
    if isPossible(m2, n2, k2, r2, X2, Y2):
        print("Possible")
    else:
        print("Not Possible")
