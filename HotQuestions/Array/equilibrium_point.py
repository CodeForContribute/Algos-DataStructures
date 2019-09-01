## Using 2 loops ##########3
def equilibrium(arr, n):
    leftsum = 0
    rightsum = 0
    for i in range(n):
        leftsum = 0
        for j in range(i):
            leftsum += arr[j]