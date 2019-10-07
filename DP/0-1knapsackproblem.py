"""
Problem Statement
=================
0/1 Knapsack Problem - Given items of certain weights/values and maximum allowed weight how to pick items to pick items
from this set to maximize sum of value of items such that sum of weights is less than or equal to maximum allowed
weight.
Runtime Analysis
----------------
Time complexity - O(W*total items)
Video
-----
* Topdown DP - https://youtu.be/149WSzQ4E1g
* Bottomup DP - https://youtu.be/8LusJS5-AGo
References
----------
* http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/
* https://en.wikipedia.org/wiki/Knapsack_problem
"""


def knap_sack_problem(values, weights, total):
    total_items = len(weights)
    rows = total_items + 1
    cols = total + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(1, rows):
        for j in range(1, cols):
            if j < weights[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])

    return dp[rows - 1][cols - 1]


#


if __name__ == '__main__':
    total_weight = 7
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    print(knap_sack_problem(values, weights, total_weight))
    total_weight = 7
    weights = [2, 2, 4, 5]
    values = [2, 4, 6, 9]
    print(knap_sack_problem(values, weights, total_weight))
