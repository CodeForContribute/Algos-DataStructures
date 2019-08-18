def find_max(arr, n, k):
    hash_map = dict()
    for i in range(n):
        x = arr[i]
        d = min(1+i, n-i)
        if x not in hash_map.keys():
            hash_map[x] = d
        else:
            hash_map[x] = min(d, hash_map[x])
    ans = 10 ** 9
    for i in range(n):
        x = arr[i]
        if x != k-x and k-x in hash_map.keys():
            ans = min(max(hash_map[x], hash_map[k-x]), ans)
    return ans


if __name__ == '__main__':
    arr1 = [3, 5, 8, 6, 7]
    n = len(arr1)
    print(find_max(arr1, n, 11))
