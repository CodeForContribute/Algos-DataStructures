"""
Method 1 (Change Left subtree to its Mirror and compare it with Right subtree)
Algorithm: isFoldable(root)

1) If tree is empty, then return true.
2) Convert the left subtree to its mirror image
    mirror(root->left); /* See this post */
3) Check if the structure of left subtree and right subtree is same
   and store the result.
    res = isStructSame(root->left, root->right); /*isStructSame()
        recursively compares structures of two subtrees and returns
        true if structures are same */
4) Revert the changes made in step (2) to get the original tree.
    mirror(root->left);
5) Return result res stored in step 2.

Time Complexity: O(n)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order_tree(root):
    if root is None:
        return
    in_order_tree(root.left)
    print(root.data, end=" ")
    in_order_tree(root.right)

#######################################################################################################################
def mirror(root):
    if root is None:
        return
    else:
        mirror(root.left)
        mirror(root.right)
        root.left, root.right = root.right, root.left


def is_structure_same(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None and is_structure_same(root1.left, root2.left) and is_structure_same(
            root1.right, root2.right):
        return True
    return False


def is_foldable(root):
    if root is None:
        return True
    mirror(root.left)
    result = is_structure_same(root.left, root.right)
    mirror(root.left)
    return result
#######################################################################################################################

"""
Time complexity: O(n)

Method 2 (Check if Left and Right subtrees are Mirror)
There are mainly two functions:

// Checks if tree can be folded or not

IsFoldable(root)
1) If tree is empty then return true
2) Else check if left and right subtrees are structure wise mirrors of
    each other. Use utility function IsFoldableUtil(root->left,
    root->right) for this.
// Checks if n1 and n2 are mirror of each other.

IsFoldableUtil(n1, n2)
1) If both trees are empty then return true.
2) If one of them is empty and other is not then return false.
3) Return true if following conditions are met
   a) n1->left is mirror of n2->right
   b) n1->right is mirror of n2->left
filter_none"""
#####################################################################################################################

def is_foldable_mirror(root):
    if root is None:
        return True
    return is_foldable_util(root.left, root.right)


def is_foldable_util(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return is_foldable_util(root1.left, root2.right) and is_foldable_util(root1.right, root2.left)
#######################################################################################################################

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    print("In Order Traversal of Tree:")
    in_order_tree(root)
    print("\n")
    # mirror(root.left)
    # print("\n")
    # in_order_tree(root)
    print("\n")
    print(is_foldable(root))
    print("\n")
    print(is_foldable_mirror(root))
