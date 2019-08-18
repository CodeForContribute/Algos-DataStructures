def all_permutations_a_row_in_a_matrix(mat, m, n, row):
    hash_map = dict()
    for i in range(n):
        if mat[row][i] in hash_map.keys():
            hash_map[mat[row][i]] += 1
        else:
            hash_map[mat[row][i]] = 1
    permuted_rows = list()
    for i in range(m):
        if i != row:
            permuted_rows.append(i)
    for i in range(m):
        for j in range(n):
            if mat[i][j] not in hash_map.keys():
                if i in permuted_rows:
                    permuted_rows.remove(i)

    for i in range(len(permuted_rows)):
        print(permuted_rows[i], end=" ")


if __name__ == '__main__':
    m = 4
    n = 4
    r = 3
    mat = [[3, 1, 4, 2],
           [1, 6, 9, 3],
           [1, 2, 3, 4],
           [4, 3, 2, 1]]
    all_permutations_a_row_in_a_matrix(mat, m, n, r)
