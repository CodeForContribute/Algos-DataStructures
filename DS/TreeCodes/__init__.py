"""
    Properties of Binary Tree:
    1. The max number of nodes at a level 'l' is pow(2,l-1)
    2. Max number of nodes in a binary tree of height is pow(2,h)- 1
       Height of a tree means max number of nodes from root to the leaf path
    3.In a binary tree with n nodes, min possible height or min number of levels is log2(n+1)
    4. A binary tree with l leaves has at least log2(l) + 1 levels
    5. In Binary tree every node has 0 or 2 children, number of leaf nodes is always one more than
         nodes with two children.
    6. Full Binary tree- A binary tree is called Full if every node has 0 or 2 children or a binary tree in which all
       nodes except leaves have two children.
    7.Complete Binary Tree-A binary tree is called a complete binary tree if all levels are completely filled except
      possibly the last level and last level has all keys as left as possible.
    8. perfect Binary tree:A Binary tree is called a perfect one if all internal nodes have two children and all leaves
       are at the same level.
    9. Balanced Binary tree: A Binary tree is called balanced one if height of tree is o(log(n)) where n is the number
                             of nodes.
                             for ex:AVL tree maintains O(log(n)) height by making sure that the difference of left and
                              right subtrees is 1
                             Red-Black Tree:It maintains height O(log(n)) by making sure that the number of black nodes
                                             on every path from root to leaf node is same and there is no adjacent red
                                             nodes
    10. Degenerate node: A tree is called a degenerate one where every internal node has one child.such tree are
                         performance wise same as linked List
"""
