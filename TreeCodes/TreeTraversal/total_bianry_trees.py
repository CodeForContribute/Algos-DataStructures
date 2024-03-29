def count_trees(n):
    BT = [0]*(n+1)
    BT[0] = BT[1] = 1
    for i in range(2, n+1):
        for j in range(i):
            BT[i] += BT[j] * BT[i-j-1]
    return BT[n]

if __name__ == '__main__':
    n = 5
    print(count_trees(n))