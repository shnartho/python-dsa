class TreeNode:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self._insert_recursive(current_node.left, data)
        
        else:
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self._insert_recursive(current_node.right, data)
    
    def inorder_traversal(self, node, level= 0):
        if node:
            self.inorder_traversal(node.right, level+1)
            print("     "*level + str(node.data))
            self.inorder_traversal(node.left, level+1)

binary_tree = BinaryTree()
binary_tree.insert(24)
binary_tree.insert(6)
binary_tree.insert(43)
binary_tree.insert(44)
binary_tree.insert(23)
binary_tree.insert(19)
binary_tree.insert(11)
binary_tree.insert(27)
binary_tree.insert(29)
binary_tree.insert(44)
binary_tree.insert(14)
binary_tree.insert(8)
binary_tree.insert(9)
binary_tree.insert(1)
binary_tree.insert(51)
binary_tree.insert(33)
binary_tree.insert(25)
binary_tree.insert(21)
binary_tree.inorder_traversal(binary_tree.root)