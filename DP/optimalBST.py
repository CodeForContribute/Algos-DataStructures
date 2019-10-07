"""
Problem Statement
=================
Given a sorted array keys[0.. n-1] of search keys and an array freq[0.. n-1] of frequency counts, where freq[i] is the
number of searches to keys[i]. Construct a binary search tree of all keys such that the total cost of all the searches
is as small as possible.
Video
-----
* https://youtu.be/hgA4xxlVvfQ
Analysis
--------
* Recursive: Exponential O(n^n)
* Dynamic Programming: O(n^3)
Reference
---------
* http://www.geeksforgeeks.org/dynamic-programming-set-24-optimal-binary-search-tree/
"""


def min_cost_BST(arr, freq):
    size = rows = cols = len(arr)
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for idx in range(rows):
        dp[idx][idx] = freq[idx]
    for subtree_size in range(2, size + 1):
        for start in range(size + 1 - subtree_size):
            end = start + subtree_size - 1
            dp[start][end] = float("inf")
            total = sum(freq[start:end + 1])
            for k in range(start, end + 1):
                val = total + (0 if k - 1 < 0 else dp[start][k - 1]) + (0 if k + 1 > end else dp[k + 1][end])
                dp[start][end] = min(val, dp[start][end])
    return dp[0][-1]


if __name__ == '__main__':
    input_array = [10, 12, 16, 21]
    freq = [4, 2, 6, 3]
    print(min_cost_BST(input_array, freq))
