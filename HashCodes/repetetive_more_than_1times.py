from math import sqrt


def find_repeating_number(arr, n):
    sqt = sqrt(n)
    block_size = n // sqt + 1
    count = [0 for i in range(block_size)]
    for i in range(0, n+1, 1):
        pass
