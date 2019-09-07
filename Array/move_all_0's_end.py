def moveZerosEnd(arrr, n):
    count = 0
    for i in range(n):
        if arrr[i] != 0:
            arrr[count] = arrr[i]
            count += 1
    while count < n:
        arrr[count] = 0
        count += 1

########## Maintaining Order ########
def moveZerosToEnd(arr, n):
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1

if __name__ == '__main__':
    arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    n = len(arr)
    # moveZerosEnd(arr, n)
    moveZerosToEnd(arr,n)
    for j in range(n):
        print(arr[j], end=" ")