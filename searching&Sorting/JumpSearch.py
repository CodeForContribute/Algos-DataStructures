import math

"""
Time Complexity of Jump Search : O(sqrt(n)) or (n/m + m-1) which is min when m = sqrt(n)
Auxiliary Space : O(1)
Important Points:
     1. Works only sorted arrays.
     2.The optimal size of a block to be jumped is (√ n). This makes the time complexity of Jump Search O(√ n).
     3.The time complexity of Jump Search is between Linear Search ( ( O(n) ) and Binary Search ( O (Log n) ).
     4.Binary Search is better than Jump Search, but Jump search has an advantage that we traverse back only once 
      (Binary Search may require up to O(Log n) jumps, 
      consider a situation where the element to be searched is the smallest element or smaller than the smallest).
      So in a system where binary search is costly, we use Jump Search.
"""


def jump_search(arr, n, x):
    step = math.sqrt(n)
    prev = 0
    while arr[int(min(step, n)) - 1] < x:
        prev = int(step)
        step += int(math.sqrt(n))
        if int(prev) >= n:
            return -1
    while arr[int(prev)] < x:
        prev += 1
    if arr[int(prev)] == x:
        return int(prev)
    return -1


if __name__ == '__main__':
    arr = [0, 1, 1, 2, 3, 5, 8, 13, 21,
           34, 55, 89, 144, 233, 377, 610]
    x = 55
    n = len(arr)
    print(jump_search(arr, n, 55))
