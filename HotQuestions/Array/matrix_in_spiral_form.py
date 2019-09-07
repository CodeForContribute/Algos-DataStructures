def spiralForm(arr, m,n):
    k = 0
    l = 0
    """
    k -> starting row index
    m -> ending row index
    l -> starting column index
    n -> ending column index
    i->iterator
    Time Complexity : O(m*n)
    """
    while k < m and l < n:
        for i in range(l, n):
            print(arr[k][i],end=" ")
        k += 1
        for j in range(k,m):
            print(arr[j][n-1], end=" ")
        n -= 1
        if k < m:
            for j in range(n-1, l-1, -1):
                print(arr[m-1][j], end=" ")
            m -= 1
        if l < n:
            for i in range(m-1, k-1, -1):
                print(arr[i][l], end=" ")
            l += 1

################ Recursive Approach #########################3
# def printMatrixSpiralForm(arr,i,j,m,n):
#     if i >= m and j >= n:
#         return
#     for p in range(i, n):
#         print(arr[i][p], end=" ")
#
#     for p in range(i+1,m):
#         print(arr[p][n-1] ,end=" ")
#
#     if m-1 != i:
#         for p in range(n-2,j-1, -1):
#             print(arr[m-1][p], end=" ")
#
#     if n-1 != j:
#         for p in range(m-2, i, -1):
#             print(arr[p][j] ,end=" ")
#
#     printMatrixSpiralForm(arr, i+1, j+1, m-1, n-1)


if __name__ == '__main__':
    a = [[1, 2, 3, 4, 5, 6],
         [7, 8, 9, 10, 11, 12],
         [13, 14, 15, 16, 17, 18]]
    m = 3
    n = 6
    spiralForm(a, m, n)
    print("\n")
    printMatrixSpiralForm(a, 0, 0, m, n)
