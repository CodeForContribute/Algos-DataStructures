"""
Time Complexity : O(n)
"""


def min_delete_operations(arr, n):
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    max_count = -1
    for i in hash_map:
        if hash_map[i] > max_count:
            max_count = hash_map[i]
    return n - max_count


if __name__ == '__main__':
    arr1 = [1, 1, 1, 1, 1]
    m = len(arr1)
    print(min_delete_operations(arr1, m))
