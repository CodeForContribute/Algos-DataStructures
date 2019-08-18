def pair_with_given_product(arr, n, k):
    for i in range(n):
        for j in range(i + 1, n, 1):
            if arr[i] * arr[j] == k:
                return True
    return False


def pair_with_given_product2(arr, n, k):
    for i in arr:
        for j in arr:
            if i != j and i * j == k:
                return True
    return False


# Method3 Using Hashing
def is_product(arr, n, x):
    if n < 2:
        return False
    s = set()
    for i in range(n):
        if arr[i] == 0:
            if x == 0:
                return True
            else:
                continue
        if x % arr[i] == 0:
            if x // arr[i] in s:
                return True
            s.add(arr[i])


if __name__ == '__main__':
    arr1 = [10, 20, 9, 40, 10]
    n = len(arr1)
    # a = pair_with_given_product(arr1, n, 90)
    # a = pair_with_given_product2(arr1, n, 100)
    a = is_product(arr1, n, 90)
    if a is True:
        print("Yes")
    else:
        print("False")
