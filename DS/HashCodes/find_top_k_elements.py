from sys import maxsize


def top_k_elements(arr, n, k):
    # List of size k + 1 to store elements
    top = [0 for i in range(k + 1)]
    # Dictionary to keep track of frequency
    hash_map = {i: 0 for i in range(k + 1)}
    for m in range(len(arr)):
        if arr[m] in hash_map.keys():
            hash_map[arr[m]] += 1
        else:
            hash_map[arr[m]] = 1
        top[k] = arr[m]
        i = top.index(arr[m])
        # i = k
        i -= 1
        while i >= 0:
            if hash_map[top[i]] < hash_map[top[i + 1]]:
                top[i], top[i + 1] = top[i + 1], top[i]
            elif hash_map[top[i]] == hash_map[top[i + 1]] and top[i] > top[i + 1]:
                top[i], top[i + 1] = top[i + 1], top[i]
            else:
                break
            i -= 1
        i = 0
        while i < k and top[i] != 0:
            print(top[i], end=" "),
            i += 1


if __name__ == '__main__':
    k = 4
    arr = [5, 2, 1, 3, 2]
    n = len(arr)
    top_k_elements(arr, n, k)
