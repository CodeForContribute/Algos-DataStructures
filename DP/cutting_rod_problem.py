"""
Problem Statement
=================
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces.
Video
-----
* https://youtu.be/IRwVmTmN6go
Time Complexity
---------------
1. Recursive Solution = O(2^n)
2. Dynamic Programming Solution = O(n^2)
Reference
---------
http://www.geeksforgeeks.org/dynamic-programming-set-13-cutting-a-rod/
"""


def max_profits(prices, rod_length):
    rod_length_values = [0 for _ in range(rod_length + 1)]
    for length in range(1, rod_length + 1):
        pass
