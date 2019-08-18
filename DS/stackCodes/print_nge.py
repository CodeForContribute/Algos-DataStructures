def print_gne(arr, n):
    s = list()
    arr1 = [0 for i in range(n)]
    # print(arr1[i] for i in range(n))
    for i in range(n - 1, -1, -1):
        while len(s) > 0 and s[-1] <= arr[i]:
            s.pop()
        if len(s) == 0:
            arr1[-i] = -1
        else:
            arr[i] = s[-1]
        s.append(arr[i])

        for i in range(n):
            print(arr[i], "-->", arr1[i])


if __name__ == '__main__':
    arr = [11, 13, 21, 3]
    n = len(arr)
    print_gne(arr, n)
