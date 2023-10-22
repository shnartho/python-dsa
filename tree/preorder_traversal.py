class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val  
        self.left = left
        self.right = right

tree_node = TreeNode(2, TreeNode(8, TreeNode(3), TreeNode(7)), TreeNode(4,right=TreeNode(1,left=TreeNode(6))))

def preorder_traversal(tree_node):
    if not tree_node:
        return
    print(tree_node.val, end="->")
    preorder_traversal(tree_node.left)
    preorder_traversal(tree_node.right)

preorder_traversal(tree_node)
print("None")