"""
Problem Statement
=================
Given two sequences A = [A1, A2, A3,..., An] and B = [B1, B2, B3,..., Bm], find the length of the longest common
subsequence.
Video
-----
* https://youtu.be/NnD96abizww
Complexity
----------
* Recursive Solution: O(2^n) (or O(2^m) whichever of n and m is larger).
* Dynamic Programming Solution: O(n * m)

"""


# DP solution
def longest_common_subsequence(seq1, seq2):
    cols = len(seq1) + 1
    rows = len(seq2) + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    max_length = 0
    for i in range(1, rows):
        for j in range(1, cols):
            if seq2[i - 1] == seq1[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            max_length = max(max_length, dp[i][j])
    return max_length


# Recursive Solution

def longest_common_subsequence_recursive_Util(sequence1, sequence2, index1, index2):
    if index1 == len(sequence1) or index2 == len(sequence2):
        return 0
    if sequence1[index1] == sequence2[index2]:
        return 1 + longest_common_subsequence_recursive_Util(sequence1, sequence2, index1 + 1, index2 + 1)
    return max(longest_common_subsequence_recursive_Util(sequence1, sequence2, index1 + 1, index2),
               longest_common_subsequence_recursive_Util(sequence1, sequence2, index1, index2 + 1))


def longest_common_subsequence_recursive(sequence1, sequence2):
    return longest_common_subsequence_recursive_Util(sequence1, sequence2, 0, 0)


if __name__ == "__main__":
    sequence1 = 'ABCDGHLQR'
    sequence2 = "AEDPHR"
    print(longest_common_subsequence(sequence1, sequence2))
    print(longest_common_subsequence_recursive(sequence1, sequence2))
