"""
Time Complexity of this program using hashing is:O(n)
"""


def print_pairs(arr, n, sum):
    s = set()
    for i in range(n):
        if sum - arr[i] in s:
            return arr[i], sum - arr[i]
        else:
            s.add(arr[i])


if __name__ == '__main__':
    arr1 = [12, 2, 56, 3, 8, 9]
    m = len(arr1)
    print(print_pairs(arr1, m, 14))
