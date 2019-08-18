def next_greater_frequency(arr, n):
    hash_map = dict()
    for i in range(n):
        if arr[i] in hash_map.keys():
            hash_map[arr[i]] += 1
        else:
            hash_map[arr[i]] = 1

    res = [0]*n
    top = -1
    top += 1
    stack = [0]*n
    stack[top] = 0
    for i in range(1, n):
        # If the frequency of the element which is pointed by the top of the stack is greater than
        # the frequency of the current element then push the current position i in the stack
        if hash_map[arr[stack[top]]] > hash_map[arr[i]]:
            top += 1
            stack[top] = i
        else:
            #  If the frequency of the element which
            #             is pointed by the top of stack is less
            #             than frequency of the current element, then
            #             pop the stack and continuing popping until
            #             the above condition is true while the stack
            #             is not empty'''
            while top > -1 and hash_map[arr[stack[top]]] < hash_map[arr[i]]:
                res[stack[top]] = arr[i]
                top -= 1
            top += 1
            stack[top] = i
    while top > -1:
        res[stack[top]] = -1
        top -= 1
    for i in range(n):
        print(res[i], end=" ")


if __name__ == '__main__':
    arr = [1, 1, 2, 3, 4, 2, 1]
    n = len(arr)
    next_greater_frequency(arr, n)
