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



def min_value_node(node):

    current = node

    while current.left is not None:
        current = current.left

    return current


# Delete Function
def delete(root, key):

    if root is None:
        return root

    # Traverse Left
    if key < root.data:
        root.left = delete(root.left, key)

    # Traverse Right
    elif key > root.data:
        root.right = delete(root.right, key)

    else:

        # Case 1 & 2: One child or no child
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        # Case 3: Two children
        temp = min_value_node(root.right)

        root.data = temp.data

        root.right = delete(root.right, temp.data)

    return root


# Inorder Traversal
def inorder(root):

    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Main Program
root = None

keys = [50, 30, 70, 20, 40, 60, 80]

# Insert Nodes
for key in keys:
    root = insert(root, key)

print("Original BST:")
inorder(root)

# Delete Leaf Node
root = delete(root, 20)
print("\n\nAfter Deleting Leaf Node (20):")
inorder(root)

# Delete Node with One Child
root = delete(root, 30)
print("\n\nAfter Deleting Node with One Child (30):")
inorder(root)

# Delete Node with Two Children
root = delete(root, 50)
print("\n\nAfter Deleting Node with Two Children (50):")
inorder(root)