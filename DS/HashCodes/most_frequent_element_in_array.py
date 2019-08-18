"""
Time Complexity : O(n * log(n))
                  log(n) - for Sorting
                  n - for traversing
"""


def most_frequent_in_array(arr, n):
    arr.sort()
    max_count = 1
    res = arr[0]
    curr_count = 1
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            curr_count += 1
        else:
            if curr_count > max_count:
                max_count = curr_count
                res = arr[i - 1]
            curr_count = 1
    if curr_count > max_count:
        max_count = curr_count
        res = arr[n - 1]
    return res


"""
This function is using hash function
Time Complexity: O(n)
"""


def most_frequent_using_hash(arr, n):
    if arr is None:
        return
    if len(arr) > n:
        return
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    max_count = 0
    res = -1
    for i in hash_map:
        if max_count < hash_map[i]:
            res = i
            max_count = hash_map[i]

    return res


if __name__ == '__main__':
    arr1 = [12, 2, 2, 56, 3, 8, 9, 9, 9, 9, 9]
    m = len(arr1)
    print(most_frequent_in_array(arr1, m))
    print(most_frequent_using_hash(arr1, m))
