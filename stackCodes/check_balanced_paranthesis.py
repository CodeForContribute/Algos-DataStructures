def check_balanced_parenthesis(exp):
    stack = list()
    for i in range(len(exp)):
        if exp[i] == '(' or exp[i] == '[' or exp[i] == '{':
            stack.append(exp[i])
            continue
        if len(stack) == 0:
            return False
        if exp[i] == ')':
            x = stack.pop()
            if x == ']' or x == '}':
                return False
        elif exp[i] == '}':
            x = stack.pop()
            if x == '(' or x == '[':
                return False

        elif exp[i] == ']':
            x = stack.pop()
            if x == '{' or x == '(':
                return False
    if len(stack):
        return False
    else:
        return True


if __name__ == '__main__':
    expr = "[{()}][]"
    print(check_balanced_parenthesis(expr))
