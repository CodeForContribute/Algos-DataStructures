def make_permutations(arr, n):
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    next_missing = 1
    for i in range(n):
        if hash_map[arr[i]] != 1 or arr[i] > n or arr[i] < 1:
            hash_map[arr[i]] -= 1
            while hash_map.get(next_missing):
                next_missing += 1
            arr[i] = next_missing
            hash_map[next_missing] = 1


if __name__ == '__main__':
    A = [2, 2, 3, 3]
    n = len(A)
    make_permutations(A, n)
    for i in range(n):
        print(A[i], end=" ")
