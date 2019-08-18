

def nge_using_stack(arr, n):
    stack = []
    next_greater = [None]*n
    stack.append(0)
    for j in range(1, n):
        element = stack.pop()
        if arr[j] > arr[element]:
            next_greater[element] = j
            # break
            print(str(arr[element]) + "-->" + str(next_greater[element]))
        elif arr[j] < arr[element]:
            stack.append(element)
        stack.append(j)
    while len(stack) != 0:
        element = stack.pop()
        next_greater[element] = 0
        print(str(arr[element]) + "-->" + str(next_greater[element]))
    for i in range(len(next_greater)):
        print(next_greater[i], end=" ")

def nge_left(arr, n):
    pass


if __name__ == '__main__':
    arr = [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
    n = len(arr)
    nge_using_stack(arr, n)
