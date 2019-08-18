# Time Complexity : O(n ^ 2)


def count_inversions(arr, n):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                count += 1
    return count


# Method2: Using Divide & Conquer
def merge_sort(arr, n):
    temp_arr = [0] * n
    return _merge_sort(arr, temp_arr, 0, n - 1)


def _merge_sort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count = _merge_sort(arr, temp_arr, left, mid)
        print("inv_count from left sub array ==== %d" % inv_count)
        inv_count += _merge_sort(arr, temp_arr, mid + 1, right)
        print("inv_count from right sub array ==== %d" % inv_count)
        inv_count += merge(arr, temp_arr, left, mid, right)
        print("inv_count after merging ==== %d" % inv_count)
    return inv_count


def merge(arr, temp_arr, left, mid, right):
    i = left  # Starting index of left sub- array
    j = mid + 1  # Starting index of right sub -array
    k = left  # starting index of sorted sub array
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i)+1
            k += 1
            j += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    for loop_var in range(left, right+1):
        arr[loop_var] = temp_arr[loop_var]
    return inv_count


if __name__ == '__main__':
    arr = [2, 1, 4, 3, 5]
    n = len(arr)
    print(count_inversions(arr, n))
    print(merge_sort(arr, n))
