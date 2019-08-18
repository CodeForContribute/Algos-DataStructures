def sum_non_repeating(arr, n):
    hash_map = set()
    for i in range(len(arr)):
        if arr[i] not in hash_map:
            hash_map.add(arr[i])
    sum = 0
    for i in range(len(hash_map)):
        sum += hash_map.pop()
    print(sum)


if __name__ == '__main__':
    arr = [1, 2, 3, 1, 1, 4, 5, 6]
    n = len(arr)
    sum_non_repeating(arr, n)
