import math


def ConstructSegementTree(arr, n):
    if n < 0:
        return
    if len(arr) == 0:
        return
    height_segment = math.ceil(math.log(n, 2))
    max_size_st = int(2 * math.pow(2, height_segment) - 1)
    stree_array = [None] * max_size_st
    constructStUtil(arr, 0, n - 1, stree_array, 0)
    return stree_array


def constructStUtil(arr, start, end, segmenttree_array, index):
    if start == end:
        segmenttree_array[index] = arr[start]
        return arr[start]
    mid = getMid(start, end)
    segmenttree_array[index] = constructStUtil(arr, start, mid, segmenttree_array, index * 2 + 1) + \
                               constructStUtil(arr, mid + 1,
                                               end,
                                               segmenttree_array,
                                               index * 2 + 2)
    return segmenttree_array[index]


def getMid(start, end):
    return start + (end - start) // 2


############# Methods to return sum in given range ###############################################
def getSumUtil(st, start, end, qs, qe, index):
    if qs <= start and qe >= end:
        return st[index]
    if end < qs or start > qe:
        return 0
    mid = getMid(start, end)
    return getSumUtil(st, start, mid, qs, qe, 2 * index + 1) + getSumUtil(st, mid + 1, end, qs, qe, 2 * index + 2)


def getSum(st, n, qs, qe):
    if qs < 0 or qe > n - 1 or qs > qe:
        print("Invlaid Queries")
        return -1
    return getSumUtil(st, 0, n - 1, qs, qe, 0)


############## Update the value in a given range ###################################################################

def getUpdateValue(arr, st, n, index, new_val):
    if index < 0 or index > n - 1:
        print("Invalid input")
        return -1
    diff = new_val - arr[index]
    arr[index] = new_val
    updateValueUtil(st, 0, n - 1, index, diff, 0)


def updateValueUtil(st, start, end, index_updated, diff, start_index):
    if index_updated < start or index_updated > end:
        return
    st[start_index] = st[start_index] + diff
    if end != start:
        mid = getMid(start, end)
        updateValueUtil(st, start, mid, index_updated, diff, 2 * start_index + 1)
        updateValueUtil(st, mid + 1, end, index_updated, diff, 2 * start_index + 2)


#####################################################################################################################
if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 11]
    n = len(arr)
    st = ConstructSegementTree(arr, n)
    print("Sum of values in array from index 1 to 3")
    print(getSum(st, n, 1, 3))
    getUpdateValue(arr, st, n, 1, 10)
    print("Sum of values in array from index 1 to 3 after updating the value")
    print(getSum(st, n, 1, 3))
