class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def mergeBalancedBSTs(root1, root2):
    n1 = sizeTree(root1)
    n2 = sizeTree(root2)
    inorder1 = list()
    inorder2 = list()
    storeInorder(root1, inorder1)
    storeInorder(root2, inorder2)
    arr = merge2SortedArrays(inorder1, inorder2, n1, n2)
    return ConstructBST(arr, len(arr))


def sizeTree(root):
    if not root:
        return 0
    lsize = sizeTree(root.left)
    rsize = sizeTree(root.right)
    return lsize + rsize + 1


def storeInorder(root, inorder):
    if not root:
        return
    storeInorder(root.left, inorder)
    inorder.append(root.data)
    storeInorder(root.right, inorder)


def merge2SortedArrays(arr1, arr2, n1, n2):
    arr = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
            k += 1
        elif arr2[j] < arr1[i]:
            arr[k] = arr2[j]
            j += 1
            k += 1
    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1
    return arr


def ConstructBST(arr, n):
    if n <= 0:
        return
    return ConstructBSTUtil(arr, 0, n - 1)


def ConstructBSTUtil(arr, start, end):
    if start > end:
        return None
    mid = start + (end - start) // 2
    node = Node(arr[mid])
    node.left = ConstructBSTUtil(arr, start, mid - 1)
    node.right = ConstructBSTUtil(arr, mid + 1, end)
    return node


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print(root.data, end=" ")
    Inorder(root.right)


#################################################Using limited extra Space ############################################
######################## Time Complexity : O(m+n) #####################################################
######################## Aux space:o(h) - > h=height of tree #############################################
########### Google @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

############### Utility functions to create Stack type Linked List #####################################
class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next


def push(stack, node):
    new_node = SNode(node)
    new_node.next = stack
    stack = new_node


def pop(stack):
    if stack:
        temp = stack
        stack = stack.next
        data = temp.data
        del temp
        return data


def isEmpty(stack):
    if stack is None:
        return True
    return False


############ Utility Function to create Binary Tree ###########################################
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def merge2BSTs(root1, root2):
    stack1 = None
    stack2 = None
    current1 = root1
    current2 = root2
    if not root1:
        inorder(root1)
        return
    if not root2:
        inorder(root1)
        return
    while current1 or not isEmpty(stack1) or current2 or not isEmpty(stack2):
        if current1 or current2:
            if current1:
                push(stack1, current1)
                current1 = current1.left
            if current2:
                push(stack2, current2)
                current2 = current2.left
        else:
            if isEmpty(stack1):
                while not isEmpty(stack2):
                    current2 = pop(stack2)
                    current2.left = None
                    inorder(current2)
                return
            if isEmpty(stack2):
                if not isEmpty(stack1):
                    current1 = pop(stack1)
                    current1.left = None
                    inorder(current1)
                return
        current1 = pop(stack1)
        current2 = pop(stack2)
        if current1.data < current2.data:
            print(current1.data, end=" ")
            current1 = current1.right
            push(stack2, current2)
            current2 = None
        else:
            print(current2.data, end=" ")
            current2 = current2.right
            push(stack1, current1)
            current1 = None


if __name__ == '__main__':
    root1 = Node(100)
    root1.left = Node(50)
    root1.right = Node(300)
    root1.left.left = Node(20)
    root1.left.right = Node(70)

    root2 = Node(80)
    root2.left = Node(40)
    root2.right = Node(120)

    # root = mergeBalancedBSTs(root1, root2)
    # Inorder(root)
    head = SNode(45)
    push(head, 34)
    push(head, 23)
    push(head, 25)
    push(head, 78)
    push(head, 90)
    printList(head)
    pop(head)
    printList(head)

    merge2BSTs(root1, root2)
