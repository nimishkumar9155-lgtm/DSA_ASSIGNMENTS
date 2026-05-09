class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert Function
def insert(root, key):

    if root is None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)

    elif key > root.data:
        root.right = insert(root.right, key)

    return root


# Search Function
def search(root, key):

    if root is None or root.data == key:
        return root

    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)


# Inorder Traversal
def inorder(root):

    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)



root = None

keys = [50, 30, 70, 20, 40, 60, 80]

# Insert Keys
for key in keys:
    root = insert(root, key)

# Inorder Traversal
print("Inorder Traversal:")
inorder(root)

# Search Key
search_key = 60

result = search(root, search_key)

if result:
    print(f"\n{search_key} Found in BST")
else:
    print(f"\n{search_key} Not Found in BST")