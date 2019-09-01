######################### In Complete #################################################################################
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def InOrder(root):
    if not root:
        return
    InOrder(root.left)
    print(root.data,end=" ")
    InOrder(root.right)

def reverse_path_util(root, node_data, hash_map, level, next_position):
    if not root:
        return
    if node_data == root.data:
        hash_map[level] = root.data
        root.data = hash_map.get(next_position[0])
        next_position[0] += 1
        return root

    hash_map[level] = root.data

    left = reverse_path_util(root.left, node_data, hash_map, level+1, next_position)
    if left is None:
        right = reverse_path_util(root.right, node_data, hash_map,level+1, next_position)

    if left is not None or right is not None:
        root.data = hash_map.get(next_position[0])
        next_position[0] += 1
        return left if left is not None else right

    return None

def reverse_Tree_Path(root, node_data):
    hash_map = dict()
    next_position = [0]
    reverse_path_util(root, node_data, hash_map, 0, next_position)


if __name__ == '__main__':
    root = Node(7)
    root.left = Node(6)
    root.right = Node(5)
    root.left.left = Node(4)
    root.left.right = Node(3)
    root.right.left = Node(2)
    root.right.right = Node(1)
    reverse_Tree_Path(root,4)
    print("Inorder before reversing path")
    InOrder(root)
    reverse_Tree_Path(root,4)
    print("\n")
    print("Inorder after reversing path")
    InOrder(root)

