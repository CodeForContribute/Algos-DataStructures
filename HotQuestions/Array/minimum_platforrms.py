# Time Complexity:O(N*log(n))
def min_platforms(arv, dept, n):
    arv.sort()
    dept.sort()
    plat_needed = 1
    result = 1
    i = 1
    j = 0
    while i < n and j < n:
        if arv[i] < dept[j]:
            plat_needed += 1
            i += 1
            if plat_needed > result:
                result = plat_needed
        else:
            plat_needed -= 1
            j += 1
    return result


if __name__ == '__main__':
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    n = len(arr)
    print(min_platforms(arr, dep, n))
