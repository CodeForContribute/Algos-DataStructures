def rearrangeArray(arr,n):
    max_index = n-1
    min_index = 0
    max_element = arr[n-1]+1
    for i in range(n):
        if i%2 == 0:
            arr[i] += (arr[max_index]%max_element)*max_element
            max_index -= 1
        else:
            arr[i] += (arr[min_index]%max_element)*max_element
            min_index += 1
    for i in range(n):
        arr[i] = arr[i]//max_element

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(arr)
    rearrangeArray(arr, n)
    for i in range(n):
        print(arr[i], end=" ")