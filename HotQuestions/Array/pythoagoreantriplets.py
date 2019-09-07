def isTriplet(arr, n):
    for i in range(n):
        arr[i] = arr[i] * arr[i]
    arr.sort()
    for i in range(n - 1, 1 ,- 1):
        j = 0
        k = i - 1
        while j < k:
            if arr[j] + arr[k] == arr[i]:
                return True
            else:
                if arr[j] + arr[k] < arr[i]:
                    j = j + 1
                else:
                    k = k - 1
    return False


if __name__ == '__main__':
    ar = [3, 1, 4, 6, 5]
    ar_size = len(ar)
    print(isTriplet(arr=ar, n=ar_size))
