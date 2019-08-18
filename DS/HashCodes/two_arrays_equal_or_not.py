def are_equal(arr1, arr2, n, m):
    if n != m:
        return False
    hash_map = dict()
    for i in range(n):
        if arr1[i] in hash_map.keys():
            hash_map[arr1[i]] += 1
        else:
            hash_map[arr1[i]] = 1

    for i in range(m):
        if not arr2[i] in hash_map.keys():
            return False
        if hash_map[arr2[i]] == 0:
            return False
        hash_map[arr2[i]] -= 1

    return True


if __name__ == '__main__':
    arr1 = [3, 5, 2, 5, 2]
    arr2 = [2, 3, 5, 5, 2]
    n = len(arr1)
    m = len(arr2)
    print(are_equal(arr1, arr2, n, m))
