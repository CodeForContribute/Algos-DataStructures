from bisect import bisect_left


# Method1: Using Sorting and binary Search : O(n*log(n) + high-low +1)
def printing_missing_elements(arr, n, low, high):
    arr.sort()
    ptr = bisect_left(arr, low)
    index = ptr
    x = low
    while index < n and x < high:
        if arr[index] != x:
            print(x, end=" ")
        else:
            index += 1
        x += 1
    while x <= high:
        print(x, end=" ")
        x += 1


# Method2 : Using Hashing O(n+(high-low+1)
def printing_missing_elements_using_hashing(arr, n ,low, high):
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    for i in range(low, high+1):
        if i not in hash_map.keys():
            print(i, end=" ")


if __name__ == '__main__':
    arr = [1, 3, 5, 4]
    n = len(arr)
    low = 1
    high = 10
    printing_missing_elements(arr, n, low, high)
    print("\n")
    printing_missing_elements_using_hashing(arr, n, low, high)
