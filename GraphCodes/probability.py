def isSafe(m, n, row, col):
    if 0 <= row < m and 0 <= col < n:
        return True
    return False


def CalculateProbability(m, n, row, col, N):
    if not isSafe(m, n, row, col):
        return 0.0
    if N == 0:
        return 1.0
    prob = 0.0
    prob += CalculateProbability(m, n, row - 1, col, N - 1) * 0.25
    prob += CalculateProbability(m, n, row, col + 1, N - 1) * 0.25
    prob += CalculateProbability(m, n, row + 1, col, N - 1) * 0.25
    prob += CalculateProbability(m, n, row, col - 1, N - 1) * 0.25
    return prob


if __name__ == '__main__':
    # matrix size
    m = 5
    n = 5

    i = 1
    j = 1

    # Number of steps
    N = 2

    print("Probability is")
    print(CalculateProbability(m, n, i, j, N))
