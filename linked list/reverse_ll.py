class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return 
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def reverse(self):
        if not self.head or not self.head.next:
            return 
        
        prev = None
        current = self.head
        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node
        self.head = prev
    
    def __str__(self):
        linklist = []
        current = self.head
        while current:
            linklist.append(str(current.val)) 
            current = current.next
        linklist.append("None")
        return " -> ".join(linklist)

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.reverse()
print(ll)
            