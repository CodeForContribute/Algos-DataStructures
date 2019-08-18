def first_repeating_element(arr, n):
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            return arr[i]
        else:
            hash_map[arr[i]] = i
    return -1


if __name__ == '__main__':
    arr = [10, 5, 3, 4, 3, 5, 6]
    n = len(arr)
    print(first_repeating_element(arr, n))
