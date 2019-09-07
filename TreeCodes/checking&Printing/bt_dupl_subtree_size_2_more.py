class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def DuplicateSubtreeUtil(root):
    s = " "
    if not root:
        return s + MArker
    lstr = DuplicateSubtreeUtil(root.left)
    if lstr == s:
        return s
    rstr = DuplicateSubtreeUtil(root.right)
    if rstr == s:
        return s
    s = s + root.data + lstr + rstr
    if len(s) > 3 and s  in set1:
        return " "
    set1.add(s)
    return s


if __name__ == '__main__':
    MArker = '$'
    set1 = set()
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')

    root.right.right = Node('B')
    root.right.right.right = Node('E')
    root.right.right.left = Node('F')
    str = DuplicateSubtreeUtil(root)
    if len(str):
        print("Yes")
    else:
        print("No")
