# Method1 : Using Sorting - Time Complexity is O(n(log*n))
def element_appears_once(arr, n):
    arr.sort()
    for i in range(n):
        print(arr[i], end="\n")
        for i in range(n):
            count = 1
            for j in range(3):
                if arr[j] == arr[j+1]:
                    count += 1
            if count % 3 != 0:
                print(arr[i], end="\n")
    # for i in range(0, n, 4):
    #     j = 0
    #     while j < 2:
    #         if arr[j] != arr[j+1]:
    #             return arr[j]
    #         j = j + 1


#  Method2 : Using Hashing -> Time Complexity is O(n) but require extra Space(o(n))
def element_appears_once_hashing(arr, n):
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    for i in range(n):
        if arr[i] in hash_map.keys() and hash_map.get(arr[i]) == 1:
            return arr[i]


# Method 3: Time Complexity O(n) but no extra space i.e, Space Complexity - O(1)
# def element_appears_once_using_bit_wise(arr, n):
#     ones = 0
#     twos = 0
#     for i in range(n):
#         twos = twos | (ones & arr[i])
#         print("twos====%d", twos)
#         ones = ones ^ arr[i]
#         print("ones===%d", ones)
#         common_bit_mask = ~(ones & twos)
#         print("common_bit_mask===%d", common_bit_mask)
#         ones &= common_bit_mask
#         print("ones===%d", ones)
#         twos &= common_bit_mask
#         print("twos====%d", twos)
#
#     return ones

def element_appears_once_using_bit_wise(arr, n):
    INT_SIZE = 32
    result = 0
    for i in range(INT_SIZE):
        sm = 0
        x = 1 << i
        for j in range(n):
            if arr[j] & x:
                sm += 1
        if sm % 3:
            result |= x
    return result


# Using Set in Python:
def element_appears_once_using_set(arr, n):
    return (3 * sum(set(arr)) - sum(arr)) // 2


if __name__ == '__main__':
    arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7]
    n = len(arr)
    (element_appears_once(arr, n))
    print(element_appears_once_hashing(arr, n))
    print(element_appears_once_using_bit_wise(arr, n))
    print(element_appears_once_using_set(arr, n))
