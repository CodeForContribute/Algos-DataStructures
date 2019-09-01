############# InComplete #####################

def CountPairs(arr1, arr2, m, n):
    NoOfY = [0]*5
    for i in range(n):
        if arr2[i] < 5:
            NoOfY[i] += 1
    arr2.sort()
    total_pairs = 0
    for i in range(m):
        total_pairs += count(arr1[i], arr2, n, NoOfY)
    print(total_pairs)


def count(x, arr2, n, NoOfY):
    ans = 0
    if x == 0:
        return 0
    if x == 1:
        return NoOfY[0]
    # index = list(filter(lambda i: i > x, arr2))[0]
    res = list(map(lambda i: i > x, arr2))[0]
    ans += n - res
    ans += NoOfY[0] + NoOfY[1]
    if x == 2:
        ans -= NoOfY[3] + NoOfY[4]
    if x == 3:
        ans += NoOfY[2]
    return ans


if __name__ == '__main__':
    arr1 = [2, 1, 6]
    arr2 = [1, 5]
    m = len(arr1)
    n = len(arr2)
    CountPairs(arr1, arr2, m, n)
