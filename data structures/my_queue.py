class Queue:
    def __init__(self):
        self.values = []

    def is_empty(self):
        return len(self.values) == 0
    
    def enqueue(self, value):
        self.values.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.values.pop(0)
        else:
            return "Queue is empty"
        
    def peek(self):
        if not self.is_empty():
            return self.values[0]
        else:
            return "Queue is empty"
        
    def size(self):
        return len(self.values)
    
    def __str__(self):
        return "[" + ",".join(map(str, self.values[:len(self.values)])) + "]"
    
my_queue = Queue()

my_queue.enqueue(5)
my_queue.enqueue(6)
my_queue.enqueue(7)
my_queue.enqueue(8)
my_queue.enqueue(9)
print(my_queue.is_empty())
print(my_queue.dequeue())
print(my_queue.peek())
print(my_queue.size())
print(my_queue)
        