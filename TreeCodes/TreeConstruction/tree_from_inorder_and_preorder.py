# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def builTree(inOrder, preOrder, inStrt, inEnd):
#     preIndex = 0
#     if inStrt > inEnd:
#         return None
#     tnode = Node(preOrder[preIndex])
#     preIndex += 1
#     if inStrt == inEnd:
#         return tnode
#     inIndex = search(inOrder, inStrt, inEnd, tnode.data)
#     tnode.left = builTree(inOrder, preOrder, inStrt, inIndex-1)
#     tnode.right = builTree(inOrder, preOrder, inIndex+1, inEnd)
#     return tnode
#
# def search(inOrder, start, end, data):
#     for i in range(start, end+1):
#         if inOrder[i] == data:
#             return i
#
# def printInorder(root):
#     if not root:
#         return
#     printInorder(root.left)
#     print(root.data, end=" ")
#     printInorder(root.right)
#
# if __name__ == '__main__':
#     inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
#     preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
#     root = builTree(inOrder, preOrder,0,len(inOrder)-1)
#     printInorder(root)

# Python program to construct tree using inorder and
# preorder traversals

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


"""Recursive function to construct binary of size len from 
Inorder traversal in[] and Preorder traversal pre[]. Initial values 
of inStrt and inEnd should be 0 and len -1. The function doesn't 
do any error checking for cases where inorder and preorder 
do not form a tree """

############### Time complexity : O(n^2) in worst case when the tree is left skewed
def buildTree(inOrder, preOrder, inStrt, inEnd):
    if inStrt > inEnd:
        return None

    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1
    if inStrt == inEnd:
        return tNode
    inIndex = search(inOrder, inStrt, inEnd, tNode.data)
    tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex - 1)
    tNode.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd)
    return tNode


# UTILITY FUNCTIONS
# Function to find index of vaue in arr[start...end]
# The function assumes that value is rpesent in inOrder[]

def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i

################## Time complexity can be optimised using hashmap ############################
def buildTree_hash_map(inOrder, preOrder, inStart, inEnd, hash_map):
    if inEnd < inStart:
        return None
    data= preOrder[buildTree_hash_map.preIndex]
    Tnode = Node(data)
    buildTree_hash_map.preIndex += 1
    if inStart == inEnd:
        return Tnode
    inIndex = hash_map[data]
    Tnode.left = buildTree_hash_map(inOrder, preOrder, inStart, inIndex-1, hash_map)
    Tnode.right = buildTree_hash_map(inOrder, preOrder, inIndex+1, inEnd, hash_map)
    return Tnode

def buildTree_hash_map_wrap(inOrder, preOrder):
    n = len(inOrder)
    hash_map = dict()
    for i in range(n):
        if inOrder[i] not in hash_map:
            hash_map[inOrder[i]] = i
    return buildTree_hash_map(inOrder, preOrder, 0, len(inOrder)-1, hash_map)


def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.data,end=" ")
    printInorder(node.right)


if __name__ == '__main__':
    # Driver program to test above function
    inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
    preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
    # Static variable preIndex
    buildTree.preIndex = 0
    buildTree_hash_map.preIndex = 0
    root = buildTree(inOrder, preOrder, 0, len(inOrder) - 1)
    print("Inorder traversal of the constructed tree is")
    printInorder(root)
    print("\n")
    node = buildTree_hash_map_wrap(inOrder, preOrder)
    print("In order traversal of Tree is:")
    printInorder(node)
