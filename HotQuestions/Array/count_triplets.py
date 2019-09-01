def findTriplets(arr, n):
    arr.sort()
    i = n-1
    while i >= 0:
        j = 0
        k = i-1
        while j < k:
            if arr[i] == arr[j]+arr[k]:
                print("numbers are:", arr[i], arr[j],arr[k],end=" ")
                return
            elif arr[i] > arr[j] + arr[k]:
                j+=1
            else:
                k -= 1
        i -= 1
    print("No triplets found!")

if __name__ == '__main__':
    arr = [5, 32, 1, 7, 10, 50, 19, 21, 2]
    n = len(arr)
    findTriplets(arr, n)