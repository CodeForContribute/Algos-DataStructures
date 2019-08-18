def groupElements(arr, n):
    visited = [False] * n
    for i in range(n):
        visited[i] = False
    for i in range(0, n):
        if visited[i] is False:
            print(arr[i], end=" ")
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    print(arr[i], end=" ")
                    visited[j] = True


def group_multiple_array_elements(arr, n):
    hash_map = dict()
    for i in range(0, len(arr)):
        hash_map[arr[i]] = hash_map.get(arr[i], 0) + 1
        # get() takes 2 params - key to be searched and default value if key is not present
    for i in range(0, len(arr)):
        count = hash_map.get(arr[i], None)
        if count is not None:
            for j in range(0, count):
                print(arr[i], end=" ")
            del hash_map[arr[i]]


if __name__ == '__main__':
    arr1 = [5, 3, 5, 1, 3, 3]
    arr2 = [4, 6, 9, 2, 3, 4, 9, 6, 10, 4]
    groupElements(arr1, len(arr1))
    print("\n")
    groupElements(arr2, len(arr2))
    print("\nBy Using Hashing")
    group_multiple_array_elements(arr1, len(arr1))
    print("\n")
    group_multiple_array_elements(arr2, len(arr2))
