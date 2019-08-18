def first_non_repeating(arr, n):
    for i in range(n):
        j = 0
        while j < n:
            if i != j and arr[i] == arr[j]:
                break
            j += 1
        if j == n:
            return arr[i]
    return -1


# Method 2: Using Hashing
def first_non_repeating_ele(arr, n ):
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    for i in range(n):
        if arr[i] in hash_map.keys() and hash_map[arr[i]] == 1:
            print(arr[i], end=" ")
            break


if __name__ == '__main__':
    arr = [9, 4, 9, 6, 7, 4]
    n = len(arr)
    print(first_non_repeating(arr, n))
    first_non_repeating_ele(arr, n)
