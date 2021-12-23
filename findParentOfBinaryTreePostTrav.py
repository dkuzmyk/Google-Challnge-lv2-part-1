class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.parent = None


def populate(current_node, num, depth):
    #print('current stats: num',num,'depth', depth)
    if current_node.right is None and depth > 1 and num > 1:
        #print("creating right node",num-1, 'depth',depth-1)
        current_node.right = Node(num - 1)
        current_node.right.parent = current_node
        populate(current_node.right, num - 1, depth - 1)
    #print('current stats: num', num, 'depth', depth)
    if current_node.left is None and depth > 1 and num > 1:
        #print("creating left node", (num - (2 ** (depth - 1))), 'depth',depth-1)
        current_node.left = Node(num - (2 ** (depth - 1)))
        current_node.left.parent = current_node
        populate(current_node.left, num - (2 ** (depth - 1)), depth - 1)


def printTree(root):
    if root:
        printTree(root.left)
        print(root.val)
        printTree(root.right)


def findNode(root, value):
    if root:
        if root.val == value:
            return root.parent.val
        if findNode(root.left, value) is not None:
            return findNode(root.left, value)
        else:
            return findNode(root.right, value)


def solution(h, q):
    numNodes = 0
    ret = []

    # calculate the number of nodes -> sum 2^(h-1)
    for i in range(1, h + 1):
        numNodes += 2 ** (i - 1)

    # create root with max number in numNodes
    root = Node(numNodes)

    # create a tree and populate it in post-order
    populate(root, numNodes, h)
    #printTree(root)

    for i in q:
        if i < numNodes and i > 0:
            ret.append(findNode(root, i))
        else:
            ret.append(-1)

    return ret


print(solution(5, [19, 14, 28]))
print("Should be: 21,15,29")
print('------------')
print(solution(3, [7, 3, 5, 1]))
print("Should be: -1,7,6,3")
print('------------')


