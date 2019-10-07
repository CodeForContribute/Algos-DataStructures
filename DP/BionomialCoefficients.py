######### Recursive Solution ###############################
def bionomialCoefficients(n, k):
    # Base condition
    if k == 0 or k == n:
        return 1
    return bionomialCoefficients(n - 1, k - 1) + bionomialCoefficients(n - 1, k)


########## As recrsive approach calculates the same exp more than 1 time so the Dp solution approach will save computations #####
########### Time Complexity : O(n*k) ##############################################################################
########### Space Complexity:O(n*k) ##############################################################################

def bionomialCoefficientsDP(n, k):
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j] + C[i - 1][j - 1]
    return C[n][k]


########### Space Optimised Solution ######################################
def spaceOptimisedBionomialCoefficientsDP(n, k):
    C = [[0 for i in range(k + 1)]]


if __name__ == '__main__':
    n = 4
    k = 2
    import time

    a = time.time()
    print(bionomialCoefficients(n, k))
    print(time.time() - a)
    b = time.time()
    print(bionomialCoefficientsDP(n, k))
    print(time.time() - b)
