class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if not root:
        return Node(data)
    if root.data > data:
        root.left = insert(root.left, data)
    if root.data < data:
        root.right = insert(root.right, data)
    return root


# Time Complexity: O(N)
# Auxiliary Space: O(1)
def iterative_predSuc(root, target, Suc, pred):
    if not root:
        return
    while root:
        if root.data == target:
            if root.right:
                Suc[0] = root.right
                while Suc[0].left:
                    Suc[0] = Suc[0].left

            if root.left:
                pred[0] = root.left
                while pred[0].right:
                    pred[0] = pred[0].right
            return
        elif root.data < target:
            pred[0] = root
            root = root.right
        else:
            Suc[0] = root
            root = root.left


# Recursive Approach
# Time Complexity: O(N)
# Auxiliary Space: O(h)
def recursive_PredSuc(root, target, Suc, pred):
    if not root:
        return
    if root.data == target:
        if root.left:
            pred[0] = root.left
            while pred[0].right:
                pred[0] = pred[0].right
        if root.right:
            Suc[0] = root.right
            while Suc[0].left:
                Suc[0] = Suc[0].left
        return
    elif root.data > target:
        Suc[0] = root
        recursive_PredSuc(root.left, target, Suc, pred)
    else:
        pred[0] = root
        recursive_PredSuc(root.right, target, Suc, pred)


if __name__ == '__main__':
    key = 20  # Key to be searched in BST

    # Let us create following BST
    #             50
    #         / \
    #         / \
    #         30     70
    #         / \     / \
    #     / \ / \
    #     20 40 60 80

    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)
    pred = [None]
    Suc = [None]
    # iterative_predSuc(root, key, Suc, pred)
    recursive_PredSuc(root, key, Suc, pred)
    if pred[0]:
        print("Predecessor is:", pred[0].data)
    else:
        print("Predecessor is:-1")
    if Suc[0]:
        print("Successor is:", Suc[0].data)
    else:
        print("Successor is: -1")
    # print(iterative_predSuc(root, key,Suc,pred))
