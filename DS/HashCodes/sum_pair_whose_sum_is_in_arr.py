def sum_pair_whose_sum_is_in_arr(arr, n):
    found = False
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] in arr:
                print((arr[i], arr[j]), end=" ")
                found = True
    if found is False:
        print("Not Found:")
        # for k in range(n):
        #     if arr[i] + arr[j] == arr[k]:
        #         print((arr[i], arr[j]), end=" ")
        #         found = True


def sum_pair_whose_sum_is_in_arr_in_hash(arr, n):
    found = False
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] in hash_map.keys():
                print((arr[i], arr[j]), end=" ")
                found = True
    if found is False:
        print("Not Found:")


if __name__ == '__main__':
    arr = [10, 4, 8, 13, 5]
    n = len(arr)
    sum_pair_whose_sum_is_in_arr(arr, n)
    print("\n")
    sum_pair_whose_sum_is_in_arr_in_hash(arr, n)
