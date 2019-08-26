############################## INComplete##################################################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next_inorder_succ_node = None
        self.left = None
        self.right = None

######################################################################################################################
def populateInorderSuccessors(root):
    next_node = None
    # if root is None:
    #     return
    if root is not None:
        populateInorderSuccessors(root.right)
        root.next_inorder_succ_node = next_node
        next_node = root
        populateInorderSuccessors(root.left)

#######################################################################################################################

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(3)
    root.right = Node(12)
    populateInorderSuccessors(root)
    ptr = root.left.left
    while ptr is not None:
        next_node = ptr.next_inorder_succ_node
        print("node=={} and node's next=={}".format(ptr.data, next_node.data))
        ptr = ptr.next_inorder_succ_node


