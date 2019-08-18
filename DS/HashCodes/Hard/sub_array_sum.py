def find_sub_array_sum(arr, n):
    c_array = [0 for i in range(n)]
    for i in range(n):
        c_array[i+1] = c_array[i] + arr[i]
    sub_arr_sum = []
