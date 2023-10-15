import heapq 

class PriorityQueue:
    def __init__(self) -> None:
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0
    
    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.elements)[1]
        else:
            raise IndexError("Priority queue is empty")
        
pq = PriorityQueue()
pq.push("Task1", 11)
pq.push("Task2", 7)
pq.push("Task3", 9)

while not pq.is_empty():
    item = pq.pop()
    print(item)