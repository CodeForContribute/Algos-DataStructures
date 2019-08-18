def find_repeating_number(arr, n):
    return sum(arr) - n * (n - 1) // 2


def find_rep_using_hash(arr, n):
    has_map = dict()
    for i in range(n):
        if arr[i] in has_map.keys():
            has_map[arr[i]] += 1
        else:
            has_map[arr[i]] = 1
    for i in range(len(arr)):
        print(has_map[arr[i]])
        if has_map[arr[i]] > 1:
            print(str(arr[i]) + "-->" + str(has_map[arr[i]]), end="\n")


if __name__ == '__main__':
    arr = [9, 8, 2, 6, 1, 8, 5, 3, 3, 4, 7]
    n = len(arr)
    # print(find_repeating_number(arr, n))
    find_rep_using_hash(arr, n)

