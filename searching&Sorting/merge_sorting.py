"""
Time Complexity in all the cases (worst,average, best ) - O(nlog(n))
Auxiliary Space - O(n)
Algorithmic Paradigm - Divide & Conquer
Sorting in Place : No
Stable: Yes
Application:
   1. Can be used in Sorting linked list in O(n(log(n))
       as merge sort required space O(1) for merging linked list so efficient.
"""
def MergeSort(arr):
    if len(arr)> 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        MergeSort(L)
        MergeSort(R)
        i = j = k =0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print ("Given array is", end="\n")
    print_list(arr)
    MergeSort(arr)
    print("Sorted array is: ", end="\n")
    print_list(arr)