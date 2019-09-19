class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.lcount = 0
        self.sum = 0


# using augmented DS
def insert(root, data):
    if not root:
        return Node(data)

    if root.data > data:
        root.lcount += 1
        root.sum += data
        root.left = insert(root.left, data)
    if root.data < data:
        root.right = insert(root.right, data)
    return root


def ksmallestelementsSum(root, k):
    if k < 0:
        return
    sum = [0]
    ksmallestelementsSumUtil(root, k, sum)
    return sum[0]


def ksmallestelementsSumUtil(root, k, sum):
    if not root:
        return
    if root.lcount + 1 == k:
        sum[0] += root.data + root.sum
        return
    elif k > root.lcount:
        sum[0] += root.data + root.sum
        k = k - root.lcount + 1
        ksmallestelementsSumUtil(root.right, k, sum)
    else:
        ksmallestelementsSumUtil(root.left, k, sum)


############################################ Method2 Using Inorder Traversal ############################
def InorderTraversal(root):
    if not root:
        return
    s = list()
    s.append(root)
    result = list()
    root = s.pop()
    while len(s) or root:
        while root:
            s.append(root)
            root = root.left
        root = s.pop()
        result.append(root.data)
        root = root.right

    return result


################################## Method3 Using Simple Recursion ##################################
def ksmallestElementSumRec(root, k, count):
    if not root:
        return 0
    res = ksmallestElementSumRec(root.left, k, count)
    if count[0] >= k[0]:
        return res
    res += root.data
    count[0] += 1

    return res + ksmallestElementSumRec(root.right,
                                        k, count)


def ksmallestElementSum(root, k):
    count = [0]
    return ksmallestElementSumRec(root, k, count)


################################################################################################################
if __name__ == '__main__':
    # root = Node(20)
    # root.left = Node(8)
    # root.right = Node(22)
    # root.left.left = Node(4)
    # root.left.right = Node(12)
    # root.left.right.left = Node(10)
    # root.left.right.right = Node(14)
    # k = [3]
    # print(ksmallestElementSum(root, k))
    # result = InorderTraversal(root)
    # res = 0
    # for j in range(3):
    #     res += result[j]
    # print(res)
    root = None
    root = insert(root,20)
    insert(root, 8)
    insert(root, 22)
    insert(root, 4)
    insert(root, 12)
    insert(root, 10)
    insert(root, 14)
    k = 3
    result = ksmallestelementsSum(root, k)
    print(result)
