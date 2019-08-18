# Using Two loops so time Complexity is: O(n^2)


def get_sum_pairs(arr, n, k):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                count += 1
    return count


# Using Hashing Time Complexity is: O(n)
def count_sum_pairs_using_hash(arr, n, k):
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    count = 0
    for i in range(n):
        if k - arr[i] in hash_map.keys():
            count += 1
        elif k - arr[i] == arr[i]:
            count -= 1

    return count // 2
    # Technique 2
    # hash_map = list()
    # hash_map = [0] * 1000
    # for i in range(n):
    #     hash_map[arr[i]] += 1
    # twice_count = 0
    # for i in range(n):
    #     twice_count += hash_map[k - arr[i]]
    #     if k - arr[i] == arr[i]:
    #         twice_count -= 1
    # return twice_count // 2


if __name__ == '__main__':
    arr = [1, 5, 7, -1, 5]
    n = len(arr)
    sum = 0
    print("Count of pairs is", get_sum_pairs(arr, n, sum))
    print("Count of pairs is", count_sum_pairs_using_hash(arr, n, sum))
