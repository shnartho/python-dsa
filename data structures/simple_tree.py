class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(node, level=0):
    if node:
        inorder_traversal(node.right, level + 1)
        print("     " * level + str(node.data))
        inorder_traversal(node.left, level + 1)
        
tree = TreeNode(7)
tree.left = TreeNode(6)
tree.right = TreeNode(5)
tree.left.right = TreeNode(8)
tree.left.left = TreeNode(9)

inorder_traversal(tree)
    