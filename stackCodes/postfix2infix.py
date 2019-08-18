def postfix2infix(exp):
    stack = list()
    for i in range(len(exp)):
        if exp[i].isalpha():
            stack.append(exp[i])
        if exp[i] in ["+", "-", "/", "*", "^"]:
            a = stack.pop()
            b = stack.pop()
            result = '(' + b + exp[i] + a + ')'
            stack.append(result)
    return stack.pop()


if __name__ == '__main__':
    exp = "ab*c+"
    n = len(exp)
    print(postfix2infix(exp))
