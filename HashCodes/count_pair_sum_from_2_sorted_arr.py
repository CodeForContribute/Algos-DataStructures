def count_pairs(arr1, arr2, m, n, sum):
    count = 0
    for i in range(m):
        for j in range(n):
            if arr1[i] + arr2[j] == sum:
                count += 1
    print(count)


# Using Binary search
def is_present(arr, low, high, value):
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] == value:
            return True
        elif arr[mid] > value:
            low = mid + 1
        else:
            high = mid - 1
    return False


def count_pairs_using_binary_search(arr1, arr2, m, n, sum):
    count = 1
    for i in range(m):
        value = sum - arr1[i]
        if is_present(arr2, 0, n - 1, value):
            count += 1
    print(count)


# Using Hashing
def count_pairs_sum_using_hashing(arr1, arr2, m, n, sum):
    hash_map = dict()
    count = 0
    for i in range(m):
        if arr1[i] in hash_map.keys():
            hash_map[arr1[i]] += 1
        else:
            hash_map[arr1[i]] = 1

    for j in range(n):
        if sum - arr2[j] in hash_map.keys():
            count += 1
    print(count)


# More Efficient
def CountPairs(arr1, arr2, m, n, sum):
    l = 0
    r = n - 1
    count = 0
    while l < m and r >= 0:
        if arr1[l] + arr2[r] == sum:
            l += 1
            r -= 1
            count += 1
        elif arr1[l] + arr2[r] < sum:
            l += 1
        elif arr1[l] + arr2[r] > sum:
            r -= 1
    print(count)


if __name__ == '__main__':
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 3, 5, 8]
    m = len(arr1)
    n = len(arr2)
    x = 10
    count_pairs(arr1, arr2, m, n, x)
    count_pairs_using_binary_search(arr1, arr2, m, n, x)
    count_pairs_sum_using_hashing(arr1, arr2, m, n, x)
    CountPairs(arr1, arr2, m, n, x)
