class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# ##### Technique1 : we have to print every level line by line so put print new line.Time Complexity : O(n^2)###########
def height(root):
    if root is None:
        return 0
    lheight = height(root.left)
    rheight = height(root.right)
    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1


def level_order_traversal(root):
    if root is None:
        return
    h = height(root)
    for i in range(1, h + 1):
        print_given_level(root, i)
        print("\n")


def print_given_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        print_given_level(root.left, level - 1)
        print_given_level(root.right, level - 1)
########################################################################################################################
# Technique2: Using one queue:we have to count nodes at each level and print these nodes and if there are children to these nodes then push
# to the queue as well. Time Complexity : O(n)
def print_level_order_Traversal_line_by_line_using_one_queue(root):
    if root is None:
        return
    queue = list()
    queue.append(root)
    while len(queue):
        node_count = len(queue)
        while node_count > 0:
            temp = queue.pop(0)
            print(temp.data, end=" ")
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
            node_count -= 1
        print("\n")
########################################################################################################################
# Using 2 Queues:Time Complexity : O(n) Space Complexity : O(max width of tree) can be O(n)
def print_level_order_traversal_using_2_queues(root):
    if root is None:
        return
    queue1 = list()
    queue2 = list()
    queue1.append(root)
    while len(queue1) or len(queue2):
        while len(queue1):
            temp = queue1.pop(0)
            print(temp.data, end=" ")
            if temp.left is not None:
                queue2.append(temp.left)
            if temp.right is not None:
                queue2.append(temp.right)
        print("\n")
        while len(queue2):
            temp = queue2.pop(0)
            print(temp.data, end=" ")
            if temp.left is not None:
                queue1.append(temp.left)
            if temp.right is not None:
                queue1.append(temp.right)
        print("\n")
########################################################################################################################
# Method4: Using one queue and a delimeter-> NULL
def level_order_traversal_using_a_delemeter(root):
    if root is None:
        return
    queue = list()
    queue.append(root)
    queue.append(None)
    while len(queue) > 1:
        temp = queue.pop(0)
        if temp is None:
            queue.append(None)
            print("\n")
        else:
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
            print(temp.data, end=" ")

########################################################################################################################

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Level order traversal of binary tree line by line is -")
    level_order_traversal(root)
    print("Level order traversal of binary tree line by line using Queue is -")
    print_level_order_Traversal_line_by_line_using_one_queue(root)
    print("Level order traversal of binary tree line by line using 2 Queue is -")
    print_level_order_traversal_using_2_queues(root)
    print("Level order traversal of binary tree line by line using 1 Queue and a delemeter is -")
    level_order_traversal_using_a_delemeter(root)
