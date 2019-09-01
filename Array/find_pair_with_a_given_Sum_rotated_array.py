def findPair_using_sorting(arr, n, data):
    arr.sort()
    low = 0
    high = n - 1
    while low < high:
        if arr[low] + arr[high] == data:
            print(arr[low], arr[high])
            break
        elif arr[low] + arr[high] < data:
            low += 1
        else:
            high -= 1
    return False


def findPairs_using_Hashing(arr, n, data):
    hash_map = set()
    for i in range(n):
        temp = data - arr[i]
        if temp in hash_map:
            print(arr[i], temp)
        hash_map.add(arr[i])


def findPairsRotatedArray(arr, n, data):
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            break
    low_element_index = (i + 1) % n
    high_element_index = i

    while low_element_index != high_element_index:
        if arr[low_element_index] + arr[high_element_index] == data:
            print(arr[low_element_index], arr[high_element_index])
            return
        if arr[low_element_index] + arr[high_element_index] < data:
            low_element_index = (low_element_index + 1) % n
        else:
            high_element_index = (high_element_index - 1 + n) % n
    return False


def findAllpairs(arr, n, sum):
    for i in range(n):
        if arr[i] > arr[i+1]:
            break
    l = (i+1)%n
    r = i
    count = 0
    while l != r:
        if arr[l] + arr[r] == sum:
            count+=1
            if l == (n+r-1)%n:
                return count
            l = (l+1)%n
            r = (n+r-1)%n
        elif arr[l] + arr[r] > sum:
            r = (n+r-1)%n
        else:
            l = (l+1)%n
    return count

if __name__ == '__main__':
    A = [11, 15, 6, 7, 9, 10]
    n = len(A)
    # findPair_using_sorting(A, n, 19)
    # print("\n")
    # findPairs_using_Hashing(A, n, 19)
    # print("\n")
    # findPairsRotatedArray(A, n, 19)
    print(findAllpairs(A, n, 16))