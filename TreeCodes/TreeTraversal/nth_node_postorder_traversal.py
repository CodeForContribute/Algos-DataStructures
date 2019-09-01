class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
######################################################################################################################
flag =[0]
def NthPostOrderNode(root, n):
    if root is None:
        return
    if flag[0] <= n[0]:
        NthPostOrderNode(root.left, n)
        NthPostOrderNode(root.right, n)
        flag[0] += 1
        if flag[0] == n[0]:
            print(root.data,end=" ")

#######################################################################################################################
if __name__ == '__main__':
    root = Node(25)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(18)
    root.left.right = Node(22)
    root.right.left = Node(24)
    root.right.right = Node(32)
    n = [6]
    NthPostOrderNode(root, n)