def longest_palindromic_subsequence(given_String):
    rows = cols = string_length = len(given_String)
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        dp[row][row] = 1
    for substring_length in range(2, string_length + 1):
        for row in range(0, string_length + 1 - substring_length):
            col = row + substring_length - 1
            if given_String[row] == given_String[col]:
                if string_length == 2:
                    dp[row][col] = 2
                else:
                    dp[row][col] = 2 + dp[row + 1][col - 1]
            else:
                dp[row][col] = max(dp[row][col - 1], dp[row + 1][col])
    return dp[0][-1]


if __name__ == "__main__":
    given_String = "abgbdba"
    expected_result = 5
    print(longest_palindromic_subsequence(given_String))
    print(expected_result == longest_palindromic_subsequence(given_String))
