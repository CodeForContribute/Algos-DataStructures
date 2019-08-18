def pair_sum(mat, n, sum):
    for i in range(n):
        mat[i].sort()
    for i in range(n):
        for j in range(i + 1, n):
            left = 0
            right = n - 1
            while left < n and right >= 0:
                if mat[i][left] + mat[j][right] == sum:
                    print((mat[i][left], mat[j][right]), end=" ")
                    left += 1
                    right -= 1
                elif mat[i][left] + mat[j][right] < sum:
                    left += 1
                elif mat[i][left] + mat[j][right] > sum:
                    right -= 1


# Using Hashing
# Python Code for sum pairs in a matrix using hashing
def sum_pairs_using_hash(mat, n, sum):
    hash_map = dict()
    for i in range(n):
        for j in range(n):
            if mat[i][j] not in hash_map.keys():
                hash_map[mat[i][j]] = (i, j)
    for i in range(n):
        for j in range(i, n):
            if sum - mat[i][j] in hash_map.keys():
                a = hash_map[mat[i][j]]
                b = hash_map[sum - mat[i][j]]
                if a[0] < b[0]:
                    print((mat[i][j], sum - mat[i][j]), end=" ")


if __name__ == '__main__':
    mat = [[1, 3, 2, 4],
           [5, 8, 7, 6],
           [9, 10, 13, 11],
           [12, 0, 14, 15]]
    n = 4
    sum = 11
    pair_sum(mat, n, sum)
    print("\n")
    sum_pairs_using_hash(mat, n, sum)
