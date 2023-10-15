class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
            
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def insert_after(self, prev_data, new_data):
        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(new_data)
                new_node.prev = current
                new_node.next = current.next

                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                
                current.next = new_node
                return
            current = current.next

    def insert_before(self, after_data, new_data):
        current = self.head
        while current:
            if current.data == after_data:
                new_node = Node(new_data)
                new_node.next = current
                new_node.prev = current.prev

                if current.prev:
                    current.prev.next = new_node
                else:
                    self.head = new_node
                current.prev = new_node
                return
            current = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def __str__(self) -> str:
        return ' <-> '.join(map(str, self.display()))
    
doubly_linkedlist = DoublyLinkedList()
doubly_linkedlist.append(5)
print(doubly_linkedlist)
doubly_linkedlist.append(6)
print(doubly_linkedlist)
doubly_linkedlist.prepend(7)
print(doubly_linkedlist)
doubly_linkedlist.append(8)
print(doubly_linkedlist)
print(doubly_linkedlist.is_empty())
doubly_linkedlist.insert_after(6, 67)
print(doubly_linkedlist)
doubly_linkedlist.insert_before(8, 78)
print(doubly_linkedlist)
doubly_linkedlist.insert_after(8, 89)
print(doubly_linkedlist)
doubly_linkedlist.delete(7)
print(doubly_linkedlist)
doubly_linkedlist.delete(67)
print(doubly_linkedlist)
print(doubly_linkedlist.search(89))
print(doubly_linkedlist.search(99))
print(doubly_linkedlist)

