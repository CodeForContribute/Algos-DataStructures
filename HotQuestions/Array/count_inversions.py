def merge_sort(arr, n):
    temp_arr = [0]*n
    return _merge_sort(arr, temp_arr, 0, n-1)

def _merge_sort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right)//2
        inv_count = _merge_sort(arr, temp_arr, left, mid)
        inv_count += _merge_sort(arr, temp_arr, mid+1, right)
        inv_count += merge(arr ,temp_arr, left, mid, right)
    return inv_count

def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid+1
    k = left
    inv_count = 0
    while i<= mid and j<=right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k+=1
            i+=1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i+1)
            k+=1
            j+=1
    while i<= mid:
        temp_arr[k] = arr[i]
        i+=1
        k+=1
    while j<= right:
        temp_arr[k] = arr[j]
        j+=1
        k+=1
    for temp in range(left, right+1):
        arr[temp] = temp_arr[temp]
    return inv_count

if __name__ == '__main__':
    arr = [1, 20, 6, 4, 5]
    n = len(arr)
    result = merge_sort(arr, n)
    print(result)