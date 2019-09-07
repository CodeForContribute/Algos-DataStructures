def preProcess(arr, n):
    temp = [None] * (2 * n)
    for i in range(n):
        temp[i] = temp[i + n] = arr[i]

    return temp


def leftRotate(arr, n, k, temp):
    start = k % n
    for i in range(start, start + n):
        print(temp[i], end=" ")
    print(" ")


def space_optimised_rotation(arr, n, k):
    for i in range(k, k + n):
        print(arr[i % n], end=" ")


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    n = len(arr)
    temp = preProcess(arr, n)
    # k = 2
    # leftRotate(arr, n, k, temp)
    #
    # k = 3
    # leftRotate(arr, n, k, temp)
    #
    # k = 4
    # leftRotate(arr, n, k, temp)

    k = 4
    space_optimised_rotation(arr, n, k)
