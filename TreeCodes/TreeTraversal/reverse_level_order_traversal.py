class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
########################################################################################################################
# Time Complexity->O(n^2)
def height(root):
    if not root:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    if lheight > rheight:
        return lheight+1
    else:
        return rheight+1

def print_given_level(root, level):
    if not root:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        print_given_level(root.left, level-1)
        print_given_level(root.right, level-1)


def reverse_level_order_traversal(root):
    if not root:
        return
    h = height(root)
    for i in range(h,0, -1):
        print_given_level(root, i)
        # print("\n")
#######################################################################################################################

def reverse_level_order_traversal_using_queue_and_Stack(root):
    if not root:
        return
    Stack = list()
    Queue = list()
    Queue.append(root)
    while len(Queue):
        temp = Queue.pop(0)
        Stack.append(temp)
        if temp.left is not None:
            Queue.append(temp.left)
        if temp.right is not None:
            Queue.append(temp.right)
    while len(Stack):
        print(Stack.pop().data, end=" ")



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Given reversed level order traversal is:")
    reverse_level_order_traversal(root)
    print("Given reversed level order traversal using stack and a queue is:")
    reverse_level_order_traversal_using_queue_and_Stack(root)

