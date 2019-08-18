import sys


def smallest_element_repeated_k_times(arr, n, k):
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    res = sys.maxsize
    res1 = sys.maxsize
    # Technique 1
    for key, value in hash_map.items():
        if value == k:
            res = min(res, key)
    return res if res != res1 else -1
    # Technique 2
    # min_value_list = list()
    # for entry in hash_map:
    #     value = hash_map[entry]
    #     if value == k:
    #         min_value_list.append(entry)
    # print(min(min_value_list))


if __name__ == '__main__':
    arr = [11, 11, 11, 23, 11, 37,
           37, 51, 51, 51, 51]
    n = len(arr)
    k = 4
    print(smallest_element_repeated_k_times(arr, n, k))
