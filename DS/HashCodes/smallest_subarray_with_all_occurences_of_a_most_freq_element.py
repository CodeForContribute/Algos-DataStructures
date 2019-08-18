"""
  Time Complexity: O(n)
"""


def first_occurrences_number(arr, number):
    p1 = None
    for position in range(len(arr)):
        if arr[position] == number:
            p1 = position
            break
    return p1


def smallest_sub_array_most_freq_element(arr, n):
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1
    # Calculating Max count
    max_count = 0
    for i in range(n):
        if hash_map[arr[i]] > max_count:
            max_count = hash_map[arr[i]]

    # Finding the numbers having same max counts
    number_with_max_count = set()
    for i in range(n):
        if hash_map[arr[i]] == max_count:
            number_with_max_count.add(arr[i])

    # Finding the first occurrence of the number having max position which will yield  min sub array
    for i in range(len(number_with_max_count)):
        p2 = -1
        p = first_occurrences_number(arr, number_with_max_count.pop())
        if p > p2:
            p2 = p

    occurrences = []
    a = None
    for position in range(n):
        if hash_map[arr[position]] == max_count:
            if len(occurrences) == 0 and position == p2:
                a = position
                occurrences.append(position)
            elif len(occurrences) != 0 and position > a and arr[position] == arr[p2]:
                a = position
                occurrences.append(position)

    # Printing all the occurrences for the min_sub array
    for position in range(occurrences[0], occurrences[len(occurrences) - 1] + 1, 1):
        print(arr[position], end=" ")


if __name__ == '__main__':
    arr1 = [4, 1, 2, 2, 1, 3, 3]
    arr2 = [1, 2, 2, 4, 3, 3, 1, 4, 5, 6, 7, 3, 2]
    n = len(arr1)
    n2 = len(arr2)
    smallest_sub_array_most_freq_element(arr1, n)
    print("\n")
    smallest_sub_array_most_freq_element(arr2, n2)
