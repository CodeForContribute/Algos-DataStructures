"""
Problem Statement
=================
Find a subsequence in given array in which the subsequence's elements are in sorted order, lowest to highest, and in
which the subsequence is as long as possible.
Video
-----
* https://youtu.be/CE2b_-XfVDk
Solution
--------
Dynamic Programming is used to solve this question. DP equation is.::
        if(arr[i] > arr[j]) { T[i] = max(T[i], T[j] + 1) }
* Time complexity is O(n^2).
* Space complexity is O(n)
Reference
---------
* http://en.wikipedia.org/wiki/Longest_increasing_subsequence
* http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
"""


def longest_increasing_subsequence(sequence):
    sequence_length = len(sequence)

    T = [1 for _ in range(sequence_length)]
    solution_indices = [i for i in range(sequence_length)]

    for index_i in range(1, sequence_length):
        for index_j in range(0, index_i):
            if (sequence[index_i] > sequence[index_j]) and (T[index_i] < T[index_j] + 1):
                T[index_i] = T[index_j] + 1
                solution_indices[index_i] = index_j

    # find the index of the max number in T
    max_value = max(T)
    max_index = T.index(max_value)

    # Print solution using linked values in solution_indices

    next_index = max_index

    while True:
        print(sequence[next_index], end=" ")
        old_index = next_index
        next_index = solution_indices[next_index]
        if next_index == old_index:
            break

    return T[max_index]


if __name__ == '__main__':
    sequence = [23, 10, 22, 5, 33, 8, 9, 21, 50, 41, 60, 80, 99, 22, 23, 24, 25, 26, 27]
    # assert 10 == longest_increaing_subsequence(sequence)
    a = longest_increasing_subsequence(sequence)
    print(a)
