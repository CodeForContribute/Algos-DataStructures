def non_overlapping_sum(arr, arr2, n):
    hash_map = dict()
    for i in range(len(arr)):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    for i in range(len(arr2)):
        if arr2[i] in hash_map.keys():
            hash_map[arr2[i]] += 1
        else:
            hash_map[arr2[i]] = 1

    sum = 0
    for i in range(n):
        if hash_map[arr[i]] == 1:
            sum += arr[i]
        if hash_map[arr2[i]] == 1:
            sum += arr2[i]

    return sum


if __name__ == '__main__':
    arr1 = [1, 5, 3, 8]
    arr2 = [5, 1, 8, 4]
    n = len(arr1)
    print(non_overlapping_sum(arr1, arr2, n))
