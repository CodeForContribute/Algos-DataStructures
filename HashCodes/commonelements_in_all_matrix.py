def print_common_elements(mat, m, n):
    hash_map = dict()
    Set = set()
    for i in range(n):
        hash_map[mat[0][i]] = 1

    for i in range(1, m):
        for j in range(n):
            if mat[i][j] in hash_map.keys() and hash_map[mat[i][j]] == i:
                hash_map[mat[i][j]] = i + 1
                
    for i in range(m):
        for j in range(n):
            if mat[i][j] in hash_map.keys() and hash_map[mat[i][j]] == m:
                if mat[i][j] not in Set:
                    Set.add(mat[i][j])
    for i in range(len(Set)):
        print(Set.pop(), end=" ")


if __name__ == '__main__':
    mat = [[1, 2, 1, 5, 8],
           [3, 7, 8, 5, 1],
           [8, 7, 7, 3, 1],
           [8, 1, 2, 7, 9]]

    print_common_elements(mat, 4, 5)
