### Space Efficient ##############
def Equilibrium(arr, n):
    leftSum = 0
    rightSum = 0
    for i in range(1, n):
        rightSum += arr[i]
    i, j = 0, 1
    while j < n:
        rightSum -= arr[j]
        leftSum += arr[i]
        if leftSum == rightSum:
            return arr[i + 1]
        i += 1
        j += 1


if __name__ == '__main__':
    arr = [2, 3, 4, 1, 4, 5]
    n = len(arr)
    print(Equilibrium(arr, n))

