"""
Time Complexity: O(n2) as there are two nested loops.

Auxiliary Space: O(1)
  1.  The good thing about selection sort is it never makes more than O(n) swaps and can be useful when memory write is
     a costly operation.
  2.Stability : The default implementation is not stable. However it can be made stable. Please see stable selection sort
   for details.
  3. In Place : Yes, it does not require extra space.
"""


def selection_sorting(arr, n):
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    for i in range(n):
        print(arr[i], end=" ")


if __name__ == '__main__':
    A = [64, 25, 12, 22, 11]
    n = len(A)
    selection_sorting(A, n)
