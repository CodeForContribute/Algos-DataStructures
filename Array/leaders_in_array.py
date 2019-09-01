############# Time Complexity : O(n^2) #######################
def leaders_in_array(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                break
        if j == len(arr)-1:
            print(arr[i], end=" ")

############# Time Complexity : O(n) #######################
def leaders_in_array_scan_from_right(arr, n):
    output = []
    max_from_right = arr[n-1]
    # print(max_from_right, end=" ")
    output.append(max_from_right)
    for i in range(n-2,0,-1):
        if max_from_right < arr[i]:
            # print(arr[i], end=" ")
            output.append(arr[i])
            max_from_right = arr[i]
    for i in output[::-1]:
        print(i, end=" ")



if __name__ == '__main__':
    arr = [16, 17,4,3,5,2]
    n = len(arr)
    leaders_in_array(arr)
    print("\n")
    leaders_in_array_scan_from_right(arr, n)

