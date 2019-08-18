def prime_freq_greater_than_k(arr, n, k):
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    for entry in hash_map:
        value = hash_map[entry]
        if is_prime(value) and value >= k:
            print(entry, end=" ")


def is_prime(n):
    if n > 2 and not n % 2 or n == 1:
        return False
    for i in range(3, int(n**0.5 + 1), 2):
        if not n % i:
            return False
    return True


if __name__ == '__main__':
    arr = [11, 11, 11, 23, 11, 37,
           37, 51, 51, 51, 51, 51]
    n = len(arr)
    k = 2
    prime_freq_greater_than_k(arr, n, k)
