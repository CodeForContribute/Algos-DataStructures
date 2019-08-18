def is_operator(x):
    if x in ["+", "-", "*", "/", "^"]:
        return True
    return False


def prefix2infix(exp):
    exp2 = exp[::-1]
    arr = list()
    for i in exp2:
        if i.isalpha():
            arr.append(i)
        if is_operator(i):
            result = '(' + str(arr.pop()) + str(i) + str(arr.pop()) + ')'
            arr.append(result)

    return arr.pop()


if __name__ == '__main__':
    exp1 = "*-A/BC-/AKL"
    print(prefix2infix(exp1))
