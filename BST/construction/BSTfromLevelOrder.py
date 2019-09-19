class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelOrderTraversal(root):
    if not root:
        return
    q = list()
    q.append(root)
    while len(q):
        countNodes = len(q)
        while countNodes:
            temp = q.pop(0)
            print(temp.data,end=" ")
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            countNodes -= 1
        print()

def constructBST(levelOrder, n):
    if n == 0:
        return None
    root = None
    for i in range(n):
        root = LevelOrder(root, levelOrder[i])
    return root

def LevelOrder(root, data):
    if not root:
        root = Node(data)
        return root
    if data <= root.data:
        root.left = LevelOrder(root.left, data)
    else:
        root.right = LevelOrder(root.right, data)
    return root


if __name__ == '__main__':
    levelorder = [7, 4, 12, 3, 6, 8, 1, 5, 10]
    root = constructBST(levelorder, len(levelorder))
    print("LevelOrder Traversal")
    levelOrderTraversal(root)

