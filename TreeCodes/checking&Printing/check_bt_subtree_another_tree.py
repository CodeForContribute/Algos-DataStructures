class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

################ Time Complexity : O(m*n) #########
def areIdentical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return root1.data == root2.data and areIdentical(root1.left, root2.left) and areIdentical(root1.right, root2.right)

def isSubtree(T, S):
    if not S:
        return True
    if not T:
        return False
    if areIdentical(T, S):
        return True
    return isSubtree(T.left, S) or isSubtree(T.right,S)
############# using Inorder and PreOrder Traversal #####
def storeInorderTree(root, Inorder, nextpos):
    if not root:
        Inorder[nextpos[0]] = '#'
        nextpos[0] += 1
        return
    storeInorderTree(root.left, Inorder, nextpos)
    Inorder[nextpos[0]] = root.data
    nextpos[0] += 1
    storeInorderTree(root.right, Inorder, nextpos)


def storePreorder(root, preOrder, nextpos1):
    if not root:
        preOrder[nextpos1[0]] = "#"
        nextpos1[0] += 1
    preOrder[nextpos1[0]] = root.data
    nextpos1[0] += 1
    storePreorder(root.left,preOrder, nextpos1)
    storePreorder(root.right, preOrder, nextpos1)

def isSubtreeTree(T, S):
    if not S:
        return True
    if not T:
        return False
    InorderS = [0]
    preOrderS = [0]

    InorderT = [0]
    preOrderT = [0]*20

    nextpos =[0]
    nextpos1 = [0]

    storeInorderTree(S, InorderS, nextpos)
    storeInorderTree(T, InorderT, nextpos)


    # storePreorder(S, preOrderS, nextpos1)
    # storePreorder(T, preOrderT, nextpos1)

    # if InorderS in InorderT and preOrderS in preOrderT:
    #     return True
    # else:
    #     return False



if __name__ == '__main__':
    T = Node(26)
    T.right = Node(3)
    T.right.right = Node(3)
    T.left = Node(10)
    T.left.left = Node(4)
    T.left.left.right = Node(30)
    T.left.right = Node(6)

    """ TREE 2 
         Construct the following tree 
              10 
            /    \ 
          4      6 
           \ 
            30 
        """
    S = Node(10)
    S.right = Node(6)
    S.left = Node(4)
    S.left.right = Node(30)

    if isSubtree(T, S):
        print("Tree 2 is subtree of Tree 1")
    else:
        print("Tree 2 is not a subtree of Tree 1")
    if isSubtreeTree(T, S):
        print("Tree 2 is subtree of Tree 1")
    else:
        print("Tree 2 is not a subtree of Tree 1")