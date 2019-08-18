# def infix2prefix(exp):
#     arr = list()
#     output = list()
#     for i in exp:
#         if i.isalpha():
#             arr.append(i)
#         elif i == '+' or i == '-' or i == '*' or i == '/' or i == '^':
#             while len(arr) != 0:
#                 output.append(i)
#                 output.append(arr.pop())
#     while len(arr) != 0:
#         output.append(arr.pop())
#
#     for i in range(len(output)):
#         print(''.join(output[i]), end=" ")

def infix2prefix(exp):
    l = len(exp)
    exp2 = exp[::-1]
    print(exp2)
    exp4 = ''
    for i in exp2:
        if i == ')':
            exp4 += '('
        elif i == '(':
            exp4 += ')'
        else:
            exp4 += i
    print(exp4)
    exp5 = infix2Postfix(exp4)
    exp3 = exp5[::-1]
    return exp3


def infix2Postfix(exp):
    output = list()
    arr = list()
    for i in exp:
        if i.isalpha():
            output.append(i)

        elif i == '(':
            arr.append(i)

        elif i == ')':
            while len(arr) != 0 and arr[-1] != '(':
                output.append(arr.pop())
            if len(arr) != 0 and arr[-1] != '(':
                return -1
            else:
                arr.pop()

        else:
            while len(arr) != 0 and not_greater(arr, i):
                output.append(arr.pop())
            arr.append(i)

    while len(arr) != 0:
        output.append(arr.pop())
    return "".join(output)


def not_greater(arr, i):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    try:
        a = precedence[i]
        b = precedence[arr[-1]]
        return True if a <= b else False
    except KeyError as ex:
        return False


if __name__ == '__main__':
    exp = "(a-b/c)*(a/k-l)"
    print(infix2prefix(exp))
