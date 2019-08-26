class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

########################################################################################################################
# Morris Traversal : Time Complexity : O(n) Space Complexity :O(1)
def in_order_traversal_without_recursion_and_stack(root):
    if root is None:
        return
    current = root
    while current is not None:
        if current.left is None:
            print(current.data, end=" ")
            current = current.right
        else:
            pred = current.left
            while pred.right is not None and pred.right is not current:
                pred = pred.right
            if pred.right is None:
                pred.right = current
                current = current.left
            else:
                pred.right = None
                print(current.data, end=" ")
                current = current.right

########################################################################################################################
def pre_order_traversal(root):
    if root is None:
        return
    current = root
    while current is not None:
        if current.left is None:
            print(current.data, end=" ")
            current = current.right
        else:
            pred = current.left
            while pred.right is not None and pred.right is not current:
                pred = pred.right
            if pred.right is None:
                pred.right = current
                print(current.data, end=" ")
                current = current.left
            else:
                pred.right = None
                current = current.right

########################################################################################################################

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    in_order_traversal_without_recursion_and_stack(root)
    print("\n")
    print("Pre-Order Traversal of tree is:")
    pre_order_traversal(root)
