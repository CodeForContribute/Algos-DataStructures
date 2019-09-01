class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#######################################################################################################################
def height_tree(root):
    if root is None:
        return 0
    lheight = height_tree(root.left)
    rheight = height_tree(root.right)
    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1

def level_order_traversal_spiral_form(root):
    if root is None:
        return
    itr = False
    height = height_tree(root)
    for i in range(1, height+1):
        print_given_level(root, i,itr)
        itr = ~itr

def print_given_level(root, level, itr):
    if root is None:
        return
    if level == 1:
        print(root.data ,end=" ")
    elif level > 1:
        if itr:
            print_given_level(root.left, level-1, itr)
            print_given_level(root.right, level-1, itr)
        else:
            print_given_level(root.right, level-1, itr)
            print_given_level(root.left, level-1, itr)

########################################################################################################################
def print_tree_in_spiral_form_using_1_queue_and_delemeter(root):
    if root is None:
        return
    s1 = list()
    s2 = list()
    s1.append(root)
    while len(s1) or len(s2):
        while len(s1):
            temp = s1.pop()
            print(temp.data, end=" ")
            if temp.right is not None:
                s2.append(temp.right)
            if temp.left is not None:
                s2.append(temp.left)
        while len(s2):
            temp = s2.pop()
            print(temp.data, end=" ")
            if temp.left is not None:
                s1.append(temp.left)
            if temp.right is not None:
                s1.append(temp.right)

########################################################################################################################


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("Level order traversal of binary tree is -")
    level_order_traversal_spiral_form(root)
    print("\n")
    print("spiral traversal of binary tree is -")
    print_tree_in_spiral_form_using_1_queue_and_delemeter(root)