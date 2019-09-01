class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    print(root.data, end=" ")
    print_inorder(root.right)


def buildTree(InOrder, LevelOrder):
    if InOrder:
        for i in range(len(LevelOrder)):
            if LevelOrder[i] in InOrder:
                node = Node(LevelOrder[i])
                io_index = InOrder.index(LevelOrder[i])
                break
        # if not InOrder:
        #     return node
        node.left = buildTree(InOrder[0:io_index], LevelOrder)
        node.right = buildTree(InOrder[io_index+1:len(inorder)],LevelOrder)
        return node


if __name__ == '__main__':
    levelorder = [20, 8, 22, 4, 12, 10, 14]
    inorder = [4, 8, 10, 12, 14, 20, 22]
    root = buildTree(inorder, levelorder)
    print_inorder(root)

