class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

class BinaryTree:
    def __init__(self):
        self.root = None  

    def insert(self, value):
        if not self.root:
            self.root = Node(value) 
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value) 
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value) 
            else:
                self._insert_recursive(node.right, value)

    def in_order_traversal(self):
        self._in_order_helper(self.root)

    def _in_order_helper(self, node):
        if node:
            self._in_order_helper(node.left)
            print(node.value, end=" ")
            self._in_order_helper(node.right)
bt = BinaryTree()
bt.insert(50)
bt.insert(30)
bt.insert(70)
bt.insert(20)
bt.insert(40)
bt.insert(60)
bt.insert(80)

print("In-order traversal of the binary tree:")
bt.in_order_traversal() 
