def max_distance(arr, n):
    hash_map = dict()
    max_dist = 0
    for i in range(n):
        if arr[i] not in hash_map.keys():
            hash_map[arr[i]] = i
        else:
            max_dist = max(max_dist, i-hash_map[arr[i]])
    return max_dist


if __name__ == '__main__':
    arr1 = [12, 2, 2, 56, 3, 8, 9, 11, 10, 9, 8]
    m = len(arr1)
    print(max_distance(arr1, m))
