from collections import defaultdict


def min_operations(arr, n):
    hash_map = defaultdict(lambda: 0)
    for i in range(0, n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    max_count = 0
    for item in hash_map:
        if hash_map[item] > max_count:
            max_count = hash_map[item]

    return n - max_count


if __name__ == '__main__':
    arr1 = [1, 1, 1, 1, 1]
    m = len(arr1)
    print(min_operations(arr1, m))
