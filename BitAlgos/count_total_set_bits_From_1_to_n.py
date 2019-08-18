def count_set_bits(n):
    bit_Count = 0
    for i in range(1, n+1):
        bit_Count += count_bits_utils(i)
    return bit_Count


def count_bits_utils(x):
    if x <= 0:
        return 0
    return (0 if int(x % 2) == 0 else 1) + count_bits_utils(int(x / 2))


if __name__ == '__main__':
    n = 3
    print(count_set_bits(n))
