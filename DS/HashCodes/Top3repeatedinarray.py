from sys import maxsize


def top3repeated_in_array(arr, n):
    if n < 3:
        print("Invalid Input")
        return

    hash_map = dict()
    for i in range(len(arr)):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    first = second = third = -maxsize
    
    Set = set()
    for i in range(len(arr)):
        Set.add(arr[i])

    while len(Set) > 0:
        a = Set.pop()
        if hash_map[a] > first:
            third = second
            second = first
            first = a
        elif hash_map[a] > second:
            third = second
            second = a
        elif hash_map[a] > third:
            third = a

    print(first, second, third, end=" ")


if __name__ == '__main__':
    arr1 = [3, 4, 2, 3, 16, 3, 15,
            16, 15, 15, 16, 2, 3]
    n = len(arr1)
    top3repeated_in_array(arr1, n)
