def missing_number(arr, n):
    total = n*(n+1)//2
    return total-sum(arr)

########## Xor Methods ########
def getMissingInt(arr, n):
    x1 = arr[0]
    x2 = 1
    for i in range(1, n):
        x1 = x1^arr[i]
    for i in range(2, n+2):
        x2 = x2^i
    return x2^x1


if __name__ == '__main__':
    a = [1, 2, 4, 5, 6]
    n = len(a)
    miss = getMissingInt(a, n)
    miss1 = getMissingInt(a, n)

    print(miss, miss1)