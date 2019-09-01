########## Efficient Approach ######
## Time Complexity : O(n) ############
def maxSum(arr, n):
    sum_arr = 0
    for i in range(n):
        sum_arr += arr[i]
    curr_val = 0
    for i in range(n):
        curr_val += i * arr[i]
    res = curr_val
    for i in range(1, n):
        next_val = (curr_val - (sum_arr - arr[i - 1]) + ((n - 1) * arr[i-1]))
        curr_val = next_val
        res = max(res, next_val)
    return res

########## Second Approach #########
def maxSumPivot(arr, n):
    sum = 0
    pivot = findPivot(arr, n)
    diff = n-1-pivot
    for i in range(n):
        sum += ((i+diff)%n)*arr[i]
    return sum

def findPivot(arr, n):
    for i in range(n):
        if arr[i] > arr[(i+1)%n]:
            return i

if __name__ == '__main__':
    arr = [8, 3, 1, 2]
    n = len(arr)
    print(maxSum(arr, n))
