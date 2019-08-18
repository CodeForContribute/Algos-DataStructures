def multiply(arr1, arr2, arr3, n):
    for i in range(n):
        for j in range(n):
            arr3[i][j] = 0
            for k in range(n):
                arr3[i][j] += arr1[i][k] * arr2[k][j]

    return arr3


if __name__ == '__main__':
    arr1 = [[1, 2],
            [2, 3]]
    arr2 = [[4, 5],
            [5, 6]]
    arr3 = [[0 for i in range(2)],
            [0 for j in range(2)]]
    n = 2
    print(multiply(arr1, arr2, arr3, n))
