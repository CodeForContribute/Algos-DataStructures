class HashMap:
    def __init__(self):
        self.s = set()

    def is_sub_array(self, arr1, arr2, m, n):
        for i in range(m):
            self.s.add(arr1[i])
        for j in range(n):
            if arr2[j] not in self.s:
                return 0

        return 1


if __name__ == '__main__':
    hash_map = HashMap()
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]
    m = len(arr1)
    n = len(arr2)
    if hash_map.is_sub_array(arr1, arr2, m, n):
        print("arr2 is subarray of arr1")
    else:
        print("arr2 is not subarray of arr1")
