def check_parenthesis(exp):
    stack = list()
    for i in range(len(exp)):
        if exp[i] == '(' or exp[i] == '[' or exp[i] == '{':
            stack.append(exp[i])
            continue
        if len(stack) == 0:
            return False
        if exp[i] == ')':
            x = stack.pop()
            if x == '[' or x == '{':
                return False
        elif exp[i] == ']':
            x = stack.pop()
            if x == ')' or x == '}':
                return False
        elif exp[i] == '}':
            x = stack.pop()
            if x == ')' or x == ']':
                return False
    return True
    # if len(stack) == 0:
    #     return True
    # else:
    #     return False


if __name__ == '__main__':
    exp = "{[()]}"
    n = len(exp)
    print(check_parenthesis(exp))
