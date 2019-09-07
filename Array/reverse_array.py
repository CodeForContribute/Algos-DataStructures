def reverse_array(arr,start,end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def reverse_array_using_recursion(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    return reverse_array_using_recursion(arr, start+1, end-1)

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6]
    print(A)
    # reverse_array(A, 0, 5)
    reverse_array_using_recursion(A,0,len(A)-1)
    print("Reversed list is")
    print(A)
