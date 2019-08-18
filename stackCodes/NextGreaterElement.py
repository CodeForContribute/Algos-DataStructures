def print_next_greater_element(arr):
    for i in range(0, len(arr)):
        next = -1
        for j in range(i + 1, len(arr), 1):
            if arr[j] > arr[i]:
                next = arr[j]
                break
        print(str(arr[i]) + "-- " + str(next))


if __name__ == '__main__':
    arr = [11, 12, 23, 4, 5, -1]
    print(print_next_greater_element(arr))
