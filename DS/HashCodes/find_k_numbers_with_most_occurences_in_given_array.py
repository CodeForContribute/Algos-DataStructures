import heapq


def k_number_with_most_occurrences(arr, n, k):
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    a = [0] * (len(hash_map))
    j = 0
    for i in hash_map:
        a[j] = [i, hash_map[i]]
        j += 1
    a = sorted(a, key=lambda x: x[0], reverse=True)
    print("After sorting through the key:")
    for i in a:
        print(i, end=" ")
    a = sorted(a, key=lambda x: x[1], reverse=True)
    print("\n")
    print("After Sorting through the values:")
    for i in a:
        print(i, end=" ")
    print("\n")
    print("Retrieving the first k items from list:")
    for i in range(k):
        print(a[i][0], end=" ")


def k_number_with_most_occurrences_heapq(arr, n, k):
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    a = [0] * len(hash_map)
    j = 0
    for i in hash_map:
        a[j] = [i, hash_map[i]]
        j += 1
    heapq.heapify(a)
    a = (heapq.nlargest(k, a, key=lambda x: x[1]))
    a = sorted(a, key=lambda x: x[0], reverse=True)
    for i in a:
        print(i, end=" ")


if __name__ == '__main__':
    arr1 = [3, 1, 4, 4, 5, 2, 6, 1]
    n = len(arr1)
    k = 2
    k_number_with_most_occurrences_heapq(arr1, n, k)
