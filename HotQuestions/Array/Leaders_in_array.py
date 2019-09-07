def printLeaders(arr, n):
    max_from_right = arr[n-1]
    print(max_from_right)
    for j in range(n-2, -1, -1):
        if max_from_right < arr[j]:
            print(arr[j])
            max_from_right = arr[j]


if __name__ == '__main__':
    arr = [18, 16, 17, 4, 3, 5, 2]
    n = len(arr)
    printLeaders(arr, n)