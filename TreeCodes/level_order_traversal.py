class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


############################# Time Complexity :O(n^2)###################################################################
def print_level_order(root):
    h = height(root)
    # print(h)
    for i in range(1, h + 1):
        print_given_level(root, i)


def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


def print_given_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        print_given_level(root.left, level - 1)
        print_given_level(root.right, level - 1)


####################################### Using Queue Time Complexity :O(max width of tree)###################################
def print_level_order_queue(root):
    if root is None:
        return
    queue = list()
    queue.append(root)
    while len(queue):
        temp = queue.pop(0)
        print(temp.data, end=" ")
        if temp.left is not None:
            queue.append(temp.left)
        if temp.right is not None:
            queue.append(temp.right)

#############################################################################################################################
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Level order traversal of binary tree is -")
    print_level_order(root)
    print("\n")
    print("Level order traversal of binary tree using Queue is -")
    print_level_order_queue(root)

