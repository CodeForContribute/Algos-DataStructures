def first_element_k_times_in_array(arr, k):
    hash_map = dict()
    for i in range(0, len(arr)):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1

    for i in range(0, len(arr)):
        if hash_map[arr[i]] == k:
            return arr[i]

    return -1


if __name__ == '__main__':
    arr1 = [1, 7, 4, 3, 4, 8, 7]
    print(first_element_k_times_in_array(arr1, 2))
