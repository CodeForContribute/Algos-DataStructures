def remove_min_number_elements(arr1, arr2, n, m):
    hash_map = dict()
    for i in range(n):
        if arr1[i] in hash_map.keys():
            hash_map[arr1[i]] += 1
        else:
            hash_map[arr1[i]] = 1
    count = 0
    visited = dict()
    for i in range(m):
        visited[arr2[i]] = False

    for i in range(m):
        if arr2[i] in hash_map.keys() and visited[arr2[i]] is False:
            count += 1
            visited[arr2[i]] = True
    return count


if __name__ == '__main__':
    a = [4, 2, 5, 6, 5, 5, 5, 5, 5]
    b = [4, 3, 5, 6, 4, 4]
    n = len(a)
    m = len(b)
    print(remove_min_number_elements(a, b, n, m))
