# A sorting based solution to find the
# minimum number of subsets of a set
# such that every subset contains distinct
# elements.

# function to count subsets such that all
# subsets have distinct elements.
def subset(ar, n):
    # take input and initialize res = 0
    res = 0

    # sort the array
    ar.sort()

    # traverse the input array and
    # find maximum frequency
    for i in range(0, n):
        count = 1

        # for each number find its repetition / frequency
        for i in range(n - 1):
            if ar[i] == ar[i + 1]:
                count += 1
            else:
                break

        # update res
        res = max(res, count)

    return res


if __name__ == '__main__':
    # Driver code
    ar = [1, 2, 4, 4, 4]
    n = len(ar)
    print(subset(ar, n))

# This code is contributed by
# Smitha Dinesh Semwal
