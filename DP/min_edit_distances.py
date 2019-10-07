"""
Problem Statement
=================
Given two strings str1 and str2, find the minimum number of edits (edit one character to another, delete char from str1
or delete char from str2) to change str1 to str2.
Video
-----
* https://youtu.be/We3YDTzNXEk
Analysis
--------
* DP Runtime : O(len(str1) * len(str2))
* Recursive Solution: Exponential (O(3^(m+n-1)))
Reference
---------
* https://www.clear.rice.edu/comp130/12spring/editdist/
"""


def min_edit_distance(str1, str2):
    rows = len(str2) + 1
    cols = len(str1) + 1
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for j in range(cols):
        dp[0][j] = j
    for i in range(rows):
        dp[i][0] = i
    for i in range(1, rows):
        for j in range(1, cols):
            if str2[i - 1] == str1[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
    printEdits(dp, str1, str2)
    return dp[rows - 1][cols - 1]


def printEdits(dp, str1, str2):
    i = len(dp) - 1  # number of rows
    j = len(dp[0]) - 1  # number of cols
    while True:
        if i == 0 or j == 0:
            break
        if str2[i - 1] == str1[j - 1]:
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j - 1] + 1:
            print("Edit %s in string1 to %s in string2." % (str1[j - 1], str2[i - 1]))
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j] + 1:
            print("Delete in string2.", str2[i - 1])
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            print("Delete in string1.", str1[j - 1])
            j -= 1


if __name__ == '__main__':
    str1 = "azced"
    str2 = "abcdef"
    expected = 3
    assert expected == min_edit_distance(str1, str2)
    assert expected == min_edit_distance(str2, str1)
