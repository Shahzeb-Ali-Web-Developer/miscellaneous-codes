class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.height = 1

class AVLTree:
  def __init__(self):
    self.root = None

  def get_height(self, node):
    if not node:
      return 0
    return node.height

  def get_balance(self, node):
    if not node:
      return 0
    return self.get_height(node.left) - self.get_height(node.right)

  def insert(self, key):
    self.root = self._insert(self.root, key)

  def _insert(self, node, key):
    if not node:
      return Node(key)
    elif key < node.key:
      node.left = self._insert(node.left, key)
    elif key > node.key:
      node.right = self._insert(node.right, key)
    else:
      # Key already exists
      pass

    # Update height of this ancestor node
    node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # Check balance factor and perform rotations if unbalanced
    balance = self.get_balance(node)

    # Left Left Case
    if balance > 1 and key < node.left.key:
      return self.right_rotate(node)

    # Right Right Case
    if balance < -1 and key > node.right.key:
      return self.left_rotate(node)

    # Left Right Case
    if balance > 1 and key > node.left.key:
      node.left = self.left_rotate(node.left)
      return self.right_rotate(node)

    # Right Left Case
    if balance < -1 and key < node.right.key:
      node.right = self.right_rotate(node.right)
      return self.left_rotate(node)

    return node

  def right_rotate(self, node):
    y = node.left
    T2 = y.right

    # Perform rotation
    y.right = node
    node.left = T2

    # Update heights
    node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
    y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

    return y

  def left_rotate(self, node):
    x = node.right
    T2 = x.left

    # Perform rotation
    x.left = node
    node.right = T2

    # Update heights
    node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
    x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

    return x

  def search(self, key):
    return self._search(self.root, key)

  def _search(self, node, key):
    if not node:
      return None
    elif key < node.key:
      return self._search(node.left, key)
    elif key > node.key:
      return self._search(node.right, key)
    else:
      return node

  def get_min_node(self, node):
    if node is None:
      return None
    while node.left is not None:
      node = node.left
    return node

  def delete(self, key):
    self.root = self._delete(self.root, key)

  def _delete(self, node, key):
    if not node:
      return node

    # BST deletion logic
    elif key < node.key:
      node.left = self._delete(node.left, key)
    elif key > node.key:
      node.right = self._delete(node.right, key)
    else:
      # Node with one or no child
      if node.left is None:
        temp = node.right
        node = None


def in_order_traversal(node):
  if node:
    in_order_traversal(node.left)
    print(node.key, end=" ")
    in_order_traversal(node.right)


# Create an AVL tree
tree = AVLTree()

# Sample 1: Insert elements in sorted order
print("Sample 1: Inserting elements in sorted order")
for i in range(1, 11):
  tree.insert(i)

print("In-order traversal:")
in_order_traversal(tree.root)
print()  # Add a newline for better readability

# Sample 2: Insert elements in random order
print("Sample 2: Inserting elements in random order")
import random
elements = list(range(1, 16))
random.shuffle(elements)
for element in elements:
  tree.insert(element)

print("In-order traversal:")
in_order_traversal(tree.root)

