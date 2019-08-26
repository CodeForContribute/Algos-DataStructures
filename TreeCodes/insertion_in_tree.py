"""
Given a binary tree and a key, insert the key into the binary tree at first position available in level order.
"""


class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.key, end=" ")
    in_order(root.right)

#######################################################################################################################
def insert_key_in_tree(root, key):
    queue = list()
    queue.append(root)
    while len(queue) != 0:
        root = queue[0]
        queue.pop(0)
        if not root.left:
            root.left = Node(key)
            break
        else:
            queue.append(root.left)
        if not root.right:
            root.right = Node(key)
            break
        else:
            queue.append(root.right)

######################################################################################################################

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print("Inorder traversal before insertion:", end=" ")
    in_order(root)
    print("\n")
    key = 12
    insert_key_in_tree(root, key)

    print()
    print("in_order traversal after insertion:", end=" ")
    in_order(root)
