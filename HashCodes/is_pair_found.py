def print_pairs(arr, n, k):
    is_pair_found = False
    for i in range(n):
        for j in range(n):
            if i != j and arr[i] % arr[j] == k:
                print((arr[i], arr[j]), end=" ")
                is_pair_found = True

    return is_pair_found


# Using Hashing Technique:
def print_pairs_using_hashing(arr, n, k):
    hash_map = dict()
    for i in range(n):
        hash_map[arr[i]] = True

    is_pair_found = False

    for i in range(n):
        if hash_map[k] and k < arr[i]:
            print((k, arr[i]), end=" ")
            is_pair_found = True

        if arr[i] >= k:
            v = find_divisors(arr[i] - k)
            for j in range(len(v)):
                if arr[i] % v[j] == k and arr[i] != v[j] and hash_map[v[j]]:
                    print((arr[i], v[j]), end=" ")
                    is_pair_found = True

    return is_pair_found


def find_divisors(n):
    v = list()
    import math
    for i in range(1, math.floor(n ** 0.5) + 1):
        if n % i == 0:
            if n / i == i:
                v.append(i)
            else:
                v.append(i)
                v.append(n // i)
    return v


if __name__ == '__main__':
    arr = [2, 3, 5, 4, 7]
    n = len(arr)
    k = 3
    (print_pairs(arr, n, k))
    print("\n")
    print(print_pairs_using_hashing(arr, n, k))
