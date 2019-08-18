def distinct_element_common_to_all_matrix(mat, m, n):
    hash_map = dict()
    for i in range(m):
        for j in range(n):
            if mat[i][j] in hash_map.keys():
                hash_map[mat[i][j]] += 1
            else:
                hash_map[mat[i][j]] = 1
    list1 = list()
    for key, value in enumerate(hash_map):
        if hash_map[value] >= m:
            list1.append(value)
        list1.sort()
    for i in range(len(list1)):
        print(list1[i], end=" ")


if __name__ == '__main__':
    mat = [[12, 1, 14, 3, 16],
           [14, 2, 1, 3, 35],
           [14, 1, 14, 3, 11],
           [14, 25, 3, 2, 1],
           [1, 18, 3, 21, 14]]
    m = 5
    n = 5
    distinct_element_common_to_all_matrix(mat, m, n)
