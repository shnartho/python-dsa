class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        if not self.head:
            return 
        
        if self.head.value == value:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None
        
    def traverse(self):
        current = self.head
        while current:
            print(current.value, "|", str(current.next)[-19:-1] , end=" -> ")
            current = current.next
        print("None")

new_linked_list = LinkedList()
new_linked_list.append(5)
new_linked_list.append(6)
new_linked_list.append(7)
new_linked_list.append(9)
new_linked_list.prepend(8)
new_linked_list.delete(7)
new_linked_list.search(9)
new_linked_list.traverse()