class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

########################################################################################################################
class Tree:
    def height(self, root):
        if root is None:
            return 0
        else:
            # left_height = self.height(root.left)
            # right_height = self.height(root.right)
            # if left_height > right_height:
            #     return left_height + 1
            # if right_height > left_height:
            #     return right_height + 1
            return 1 + max(self.height(root.left), self.height(root.right))

    def diameter(self, root):
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        left_diameter = self.diameter(root.left)
        right_diameter = self.diameter(root.right)
        return max(left_height+right_height+1, max(left_diameter, right_diameter))

#######################################################################################################################

if __name__ == '__main__':
    tree = Tree()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Diameter of given binary tree is %d" % (tree.diameter(root)))
