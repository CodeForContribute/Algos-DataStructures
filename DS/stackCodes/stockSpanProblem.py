"""
  Time Complexity : O(n^2)
  Space Complexity: O(1)
"""


def calculate_span(price, n, s):
    s[0] = 1
    for i in range(1, n):
        s[i] = 1
        j = i - 1
        while j >= 0 and price[i] > price[j]:
            s[i] += 1
            j -= 1


def print_array(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


# Time Complexity : O(n)
# Space Complexity : O(n)
def calculate_span_using_stack(price, n, s):
    stack = list()
    stack.append(0)
    s[0] = 1
    for i in range(1, n):
        while len(stack) > 0 and price[stack[-1]] <= price[i]:
            stack.pop()
        s[i] = i + 1 if len(stack) <= 0 else i - stack[-1]
        stack.append(i)


# without using any stack:
def calculate_span_without_stack(price, n, s):
    s[0] = 1
    for i in range(1, n):
        counter = 1
        while i - counter >= 0 and price[i] > price[i - counter]:
            counter += s[i - counter]
        s[i] = counter


if __name__ == '__main__':
    arr = [10, 4, 5, 90, 120, 80]
    n = len(arr)
    s = [None] * n
    # calculate_span(arr, n, s)
    # calculate_span_using_stack(arr, n, s)
    calculate_span_using_stack(arr, n, s)
    print_array(s, len(s))
