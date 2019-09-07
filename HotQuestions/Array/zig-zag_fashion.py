def zigZagFashion(arr, n):
    flag = True
    for i in range(n-1):
        if flag:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                if arr[i] < arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
        flag = bool(1-flag)
    print(arr)

if __name__ == '__main__':
    arr = [4, 3, 7, 8, 6, 2, 1]
    n = len(arr)
    zigZagFashion(arr, n)