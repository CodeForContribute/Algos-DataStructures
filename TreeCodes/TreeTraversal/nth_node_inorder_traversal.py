class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
########################################################################################################################
count = [0]
def get_nth_node(root, n):
    if root is None:
        return
    get_nth_node_util(root,n,count)

# Time Complexity : O(n)--> number of nodes
def get_nth_node_util(root, n, count):
    if root is None:
        return
    if count[0] <= n:
        get_nth_node_util(root.left, n, count)
        count[0] += 1
        if count[0] == n:
            print(root.data, end=" ")
        get_nth_node_util(root.right, n, count)

########################################################################################################################
def in_order_traversal(root):
    if root is None:
        return
    in_order_traversal(root.left)
    print(root.data,end=" ")
    in_order_traversal(root.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right = Node(30)
    in_order_traversal(root)
    print("\n")
    # count = 0
    get_nth_node(root,4)
