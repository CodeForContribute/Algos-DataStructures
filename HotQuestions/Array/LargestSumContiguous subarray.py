#########Kadane's Algorithm #############
import sys
def maxSubarraySum(arr, n):
    max_so_far = -sys.maxsize-1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range(n):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
    print(max_so_far, start, end, end=" ")

if __name__ == '__main__':
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    maxSubarraySum(a, len(a))