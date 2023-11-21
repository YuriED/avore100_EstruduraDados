import random

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def create_random_tree(n):
    values = random.sample(range(101), n)
    root = None
    for value in values:
        root = insert(root, value)
    return root

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def dsw_balance(root):
    nodes = []
    linearize(root, nodes)
    return build_tree(nodes, 0, len(nodes) - 1)

def linearize(root, nodes):
    if root is not None:
        linearize(root.left, nodes)
        nodes.append(root)
        linearize(root.right, nodes)

def build_tree(nodes, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = nodes[mid]
    root.left = build_tree(nodes, start, mid - 1)
    root.right = build_tree(nodes, mid + 1, end)
    return root

def print_inorder(root):
    if root is not None:
        print_inorder(root.left)
        print(root.key, end=" ")
        print_inorder(root.right)


initial_tree = create_random_tree(100)


for _ in range(20):
    value = random.randint(0, 100)
    initial_tree = insert(initial_tree, value)


print("Árvore inicial:")
print_inorder(initial_tree)
print("\n")


balanced_tree = dsw_balance(initial_tree)


print("Árvore balanceada:")
print_inorder(balanced_tree)
