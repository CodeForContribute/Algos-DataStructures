def find_symmetric_pairs(arr, row):
    hm = dict()
    for i in range(row):
        first = arr[i][0]
        sec = arr[i][1]
        if sec in hm.keys():
            if hm[sec] == first:
                print(str([sec, first]) + "-->" + str([first, sec]))

        else:
            hm[first] = sec


if __name__ == '__main__':
    arr = [[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]]
    # for i in range(len(arr)):
    #     print(arr[i])
    find_symmetric_pairs(arr, len(arr))
