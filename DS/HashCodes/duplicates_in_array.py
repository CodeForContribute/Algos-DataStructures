"""
Time Complexity is O(n)
Space Complexity is: O(1)
"""


def print_duplicates(arr):
    freq = dict()
    for element in arr:
        # try:
        #     freq[element] += 1
        # except:
        #     freq[element] = 1
        if element in freq.keys():
            freq[element] += 1
        else:
            freq[element] = 1

    for item in freq:
        if freq[item] > 1:
            print(item, end=" ")
    print("\n")


if __name__ == '__main__':
    arr1 = [12, 11, 40, 12, 5, 6, 5, 12, 11]
    n = len(arr1)
    print_duplicates(arr1)
