class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_operator(item):
    if item in ["+", "-", "*", "/", "^"]:
        return True
    else:
        return False


def in_order_tree(root):
    if root is None:
        return
    in_order_tree(root.left)
    print(root.data, end=" ")
    in_order_tree(root.right)


def not_greater(i, stack):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    # return  True if a in precedence and b in precedence and a<= b else False
    try:
        a = precedence[i]
        b = precedence[stack[-1]]
        return True if a <= b else False
    except KeyError as err:
        return False


def construct_expression_tree(postfix_exp):
    # postfix_exp = infix_2_postfix_conversion(infix_exp)
    stack = []
    for i in postfix_exp:
        # root = None
        if not is_operator(i):
            root = Node(i)
            stack.append(root)
        else:
            a = stack.pop()
            b = stack.pop()
            root = Node(i)
            root.right = a
            root.left = b
            stack.append(root)
    return stack.pop()


# def infix_2_postfix_conversion(exp):
#     # self.precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
#     output = list()
#     stack = []
#     for i in exp:
#         if i.isalpha():
#             output.append(i)
#         elif i == "(":
#             stack.append(i)
#         elif i == ")":
#             while len(stack) != 0 and stack[-1] != "(":
#                 a = stack.pop()
#                 output.append(a)
#             if len(stack) != 0 and stack[-1] != '(':
#                 return -1
#             else:
#                 stack.pop()
#         else:
#             while len(stack) != 0 and not_greater(i, stack):
#                 output.append(stack.pop())
#             stack.append(i)
#
#     while len(stack) != 0:
#         output.append(stack.pop())
#
#     while len(output) != 0:
#         return "".join(output)


if __name__ == '__main__':
    infix_exp = "a + b - e * f * g"
    # print(infix_2_postfix_conversion(infix_exp))
    postfix_exp = "ab+ef*g*-"
    in_order_tree(construct_expression_tree(postfix_exp))
    # print(construct_expression_tree(infix_exp)
