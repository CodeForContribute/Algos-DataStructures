class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.visited = False
########### Time complexity : O(n^2) ###################
def postOrderTraversal(root):
    temp = root
    while temp and temp.visited is False:
        if temp.left and temp.left.visited is False:
            temp = temp.left
        elif temp.right and temp.right.visited is False:
            temp = temp.right
        else:
            print(temp.data, end=" ")
            temp.visited = True
            temp = root

def postOrderTraversal_map(root):
    if not root:
        return
    hash_map = dict()
    temp = root
    hash_map[temp] = None
    while temp:
        if temp.left and temp.left not in hash_map:
            hash_map[temp.left] = temp
            temp = temp.left
        elif temp.right and temp.right not in hash_map:
            hash_map[temp.right] = temp
            temp =temp.right
        else:
            print(temp.data, end=" ")
            temp = hash_map[temp]



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    # root.left.right.left = Node(4)
    # root.left.right.right = Node(7)
    root.right.right = Node(7)
    root.right.right.left = Node(6)
    postOrderTraversal(root)
    postOrderTraversal_map(root)