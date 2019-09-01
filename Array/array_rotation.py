def left_rotate_by_one(arr, n):
    temp = arr[0]
    for i in range(1, n):
        arr[i-1] = arr[i]
    arr[n-1] = temp

def left_rotate_by_d_elements(arr, n, d):
    for i in range(d):
        left_rotate_by_one(arr, n)

#############Juggling Algorithm#################
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def left_rotation_juggling(arr, n , d):
    g_c_d = gcd(n,d)
    for i in range(g_c_d):
        temp = arr[i]
        j = i
        while True:
            k = j+d
            if k >= n:
                k = k-n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


def print_array(arr,n):
    for j in range(n):
        print(arr[j] ,end=" ")


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)
    print_array(arr, n)
    print("\n")
    # left_rotate_by_d_elements(arr, n, 2)
    # print_array(arr,n)
    # print("\n")
    left_rotation_juggling(arr, n, 3)
    print_array(arr, n)



