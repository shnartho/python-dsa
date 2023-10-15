class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty" 
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return f"Size of the stack is {len(self.items)}"
    

new_stack = Stack()
print(new_stack.pop())
new_stack.push(4)
new_stack.push(5)
new_stack.push(6)
print(new_stack.is_empty())
print(new_stack.pop())
print(new_stack.size())
print(new_stack.peek())