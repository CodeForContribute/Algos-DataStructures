class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def heightSize(root, size):
    if not root:
        return 0
    lheight = heightSize(root.left, size)
    rheight = heightSize(root.right,size)
    size[0] += 1
    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1

def DensityTree(root):
    if not root:
        return
    size = [0]
    height_size = heightSize(root, size)
    return size[0]/ height_size


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    print("Density of given binary tree is ",DensityTree(root))