"""
Problem Statement
=================
Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of dimension p[i-1] x p[i]. We
need to write a function matrix_chain_order() that should return the minimum number of multiplications needed to
multiply the chain.
Video
-----
* https://youtu.be/vgLJZMUfnsU
Note
----
In the code below we give matrices length as an array and each matrix takes 2 indices from the array.
For e.g. {2, 3, 4} represents two matrices (2, 3) and (3, 4) in (row, col) format.
Complexity
----------
Time Complexity: O(n^3)
Reference
---------
* http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
"""


def matrix_chain_multiplication(matrices):
    matrices_length = len(matrices)
    dp = [[0] for _ in range(matrices_length) for _ in range(matrices_length)]
    for gap in range(2, matrices_length):
        for i in range(0, matrices_length - gap):
            j = i + gap
            dp[i][j] = 1000
            for k in range(i + 1, j):
                temp = dp[i][k] + dp[k][j] + matrices[i] * matrices[k] * matrices[j]
                if temp < dp[i][j]:
                    dp[i][j] = temp
            return dp[0][-1]


if __name__ == '__main__':
    matrices = [4, 2, 3, 5, 3]
