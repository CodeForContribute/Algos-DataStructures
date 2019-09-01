def next_gap(gap):
    if gap <= 1:
        return 0
    return (gap//2)+(gap%2)

def merge(arr1, arr2, n,m):
    gap = (n+m)
    gap = next_gap(gap)
    while gap > 0:
        i = 0
        while i+gap < n:
            if arr1[i] > arr1[i+gap]:
                arr1[i], arr1[i+gap] = arr1[i+gap], arr1[i]
            i+=1
        j = gap-n if gap>n else 0
        while i<n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i +=1
            j += 1
        if j < m:
            while j+gap < m:
                if arr2[j] > arr2[j+gap]:
                    arr2[j], arr2[j+gap] = arr2[j+gap], arr2[j]
                j += 1
        gap = next_gap(gap)

if __name__ == '__main__':
    a1 = [10, 27, 38, 43, 82]
    a2 = [3, 9]
    n = len(a1)
    m = len(a2)
    for i in range(n):
        print(a1[i], end=" ")
    print("\n")
    for j in range(m):
        print(a2[j], end=" ")
    print("\n")
    merge(a1, a2,n,m)
    for i in range(n):
        print(a1[i], end=" ")
    for j in range(m):
        print(a2[j], end=" ")