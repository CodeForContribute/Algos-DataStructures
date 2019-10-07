def subset_sum(sequence, sum_value):
    rows = len(sequence) + 1
    cols = sum_value + 1
    T = [[False for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        T[row][0] = True

    for i in range(1, rows):
        for j in range(1, cols):
            if j >= sequence[i - 1]:
                T[i][j] = T[i - 1][j] or T[i - 1][j - sequence[i - 1]]
            else:
                T[i][j] = T[i - 1][j]
    return T[rows - 1][cols - 1]


if __name__ == '__main__':
    sequence = [2, 3, 7, 8]
    print(subset_sum(sequence, 29))
