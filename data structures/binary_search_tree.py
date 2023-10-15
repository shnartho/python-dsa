class TreeNode:
    def __init__(self, data) -> None:
        self.data = data 
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self,node,data):
        if node is None:
            return TreeNode(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        else:
            node.right = self._insert_recursive(node.right, data)

        return node
    
    def search(self, data):
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
 
    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.data = self._find_min(node.right)
            node.right = self._delete_recursive(node.right, data)
        return node
    
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node.data
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)



bst = BinarySearchTree()
bst.insert(5)
bst.insert(6)
bst.insert(7)
bst.insert(8)
bst.insert(9)
bst.insert(10)
bst.insert(99)
bst.insert(15)
bst.insert(16)
bst.insert(51)
bst.insert(12)

print("Inorder Traversal")
print(bst.inorder_traversal())

print("Search for 4:", bst.search(4))
print("Search for 9:", bst.search(9))

bst.delete(99)
print("Inorder Traversal after deleting")
print(bst.inorder_traversal())