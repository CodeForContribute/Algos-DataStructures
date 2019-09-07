def rearrange(arr, n):
    s = set()
    for i in range(n):
        s.add(arr[i])
    for i in range(n):
        if i in s:
            arr[i] = i
        else:
            arr[i] = -1

###### Method2 ##########
def fix(arr, n):
    for i in range(n):
        if arr[i] >= 0 and arr[i] != i:
            ele = arr[arr[i]]
            arr[arr[i]] = arr[i]
            arr[i] = ele

if __name__ == '__main__':
    arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
    n = len(arr)
    # rearrange(arr, n)
    fix(arr, n)
    for i in range(n):
        print(arr[i], end=" ")