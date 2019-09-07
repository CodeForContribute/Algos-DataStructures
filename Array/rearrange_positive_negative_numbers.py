#### Here all negative values are 1st arranged left side
## Then all positve elements are brough right side
def rearrange(arr, n):
    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    pos = i + 1
    neg = 0
    while neg < pos < n and arr[neg] < 0:
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg += 2


#############################################################################

# Python3 program to rearrange array
# in alternating positive & negative
# items with O(1) extra space

# Function to rearrange positive and
# negative integers in alternate fashion.
# The below solution does not maintain
# original order of elements
def rearrange_pos_neg(arr, n):
    i = 0
    j = n - 1
    while i < j:
        while arr[i] > 0:
            i += 1
        while arr[j] < 0:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if i == 0 or i == n:
        return 0
    k = 0
    while k < n and i < n:
        arr[k], arr[i] = arr[i], arr[k]
        i += 1
        k += 2


# Function to rearrange positive and
# negative integers in alternate fashion.
# The below solution does maintain
# original order of elements
def rightRotate(arr, n, outofPlace, index):
    temp = arr[index]
    for i in range(index, outofPlace, -1):
        arr[i] = arr[i - 1]
    arr[outofPlace] = temp
    return arr


def rearrange_place_maintained(arr, n):
    outofPlace = -1
    for index in range(n):
        if outofPlace >= 0:
            if ((arr[index] >= 0 and arr[outofPlace] < 0) or
                    (arr[index] < 0 and arr[outofPlace] >= 0)):
                arr = rightRotate(arr, n, outofPlace, index)
                if index - outofPlace > 2:
                    outofPlace += 2
                else:
                    outofPlace -= 1

        if outofPlace == -1:
            if (arr[index] >= 0 and index % 2 == 0) or (arr[index] < 0 and index % 2 == 1):
                outofPlace = index


def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


if __name__ == '__main__':
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    n = len(arr)
    # rearrange(arr, n)
    # rearrange_pos_neg(arr, n)
    rearrange_place_maintained(arr, n)
    printArray(arr, n)

