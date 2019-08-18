def check_duplicates_within_k(arr, n, k):
    Set = list()
    for i in range(n):
        if arr[i] in Set:
            return True
        Set.append(arr[i])
        if i >= k:
            Set.remove(arr[i - k])
    return False


if __name__ == '__main__':
    arr1 = [10, 5, 3, 4, 3, 5, 6]
    n = len(arr1)
    if check_duplicates_within_k(arr1, n, 3):
        print("Yes")
    else:
        print("No")
