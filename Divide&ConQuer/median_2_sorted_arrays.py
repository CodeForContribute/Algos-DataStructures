def get_median_2_sorted_array(arr1, arr2, n):
    i, j = 0, 0
    m1, m2 = -1, -1
    count = 0
    while count < n + 1:
        count += 1
        if i == n:
            m1 = m2
            m2 = arr2[0]
            break
        elif j == n:
            m1 = m2
            m2 = arr1[0]
            break
        elif arr1[i] < arr2[j]:
            m1 = m2
            m2 = arr1[i]
            i += 1
        else:
            m1 = m2
            m2 = arr2[j]
            j += 1
    return (m2 + m1) / 2


# Method2 : Algorithm:
#                     1. Calculate the medians m1 and m2 of the input arrays arr1[] and arr2[].
#                     2. If m1 == m2:return m1 or m2
#                     3.If m2 > m2: then median will be in two of sub arrays - a. arr1[0,.....n/2] and arr2[n/2....n-1].
#                     4. If m1 < m2: then median will be in two of sub arrays -a. arr1[n/2......n-1] and arr2[0.....n/2]
#                     5. Repeat the above process until the size of sub arrays becomes 2.
#                     6. If size of two sub arrays are 2 then return the median as
#                                                                        (max(arr1[0], arr2[0]) + min(arr[1], arr2[1])/2

def median(arr, n):
    if n == 0:
        return -1
    elif n % 2 == 0:
        return (arr[int(n / 2)] + arr[int(n / 2) + 1]) / 2
    else:
        return arr[int(n / 2)]


def get_median_divide_conquer(arr1, arr2, n):
    if n == 0:
        return -1
    elif n == 1:
        return (arr1[0] + arr2[0]) / 2
    elif n == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2
    else:
        m1 = median(arr1, n)
        m2 = median(arr2, n)
        if m1 > m2:
            if n % 2 == 0:
                return get_median_divide_conquer(arr1[:int(n / 2) + 1], arr2[:int(n / 2) - 1], int(n / 2) + 1)
            else:
                return get_median_divide_conquer(arr1[:int(n / 2) + 1], arr2[int(n / 2):], int(n / 2) + 1)
        else:
            if n % 2 == 0:
                return get_median_divide_conquer(arr1[int(n / 2 - 1):], arr2[:int(n / 2 + 1)], int(n / 2) + 1)
            else:
                return get_median_divide_conquer(arr1[int(n / 2):],
                                                 arr2[0:int(n / 2) + 1], int(n / 2) + 1)


if __name__ == '__main__':
    ar1 = [1, 12, 15, 26, 38]
    ar2 = [2, 13, 17, 30, 45]
    n1 = len(ar1)
    n2 = len(ar2)
    if n1 == n2:
        print("Median is ", get_median_divide_conquer(ar1, ar2, n1))
    else:
        print("Doesn't work for arrays of unequal size")
