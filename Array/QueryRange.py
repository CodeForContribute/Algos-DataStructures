def QueryType1(torotate,times, n ):
    torotate[0] = (torotate[0] - times)%n

def QueryType2(torotate, times, n):
    torotate[0] = (torotate[0] + times)%n

def QueryType3(torotate, l, r, presum, n):
    l = (l+torotate[0] +n)%n
    r = (r+torotate[0]+n)%n
    if l<=r:
        print(presum[r+1] - presum[l], end=" ")
    else:
        print(presum[n] + presum[r+1]- presum[l],end=" ")


def wrapper(arr, n):
    presum = [0]*(n+1)
    presum[0] = 0
    for i in range(1, n+1):
        presum[i] = presum[i-1] + arr[i-1]

    torotate = [0]
    # QueryType1(torotate, 3, n)
    QueryType2(torotate,3, n )
    QueryType3(torotate,0, 2, presum, n)

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    n = len(arr)
    wrapper(arr, n)


