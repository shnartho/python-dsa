class PriorityQueue:
    def __init__(self) -> None:
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, item, priority):
        self.elements.append((item, priority))
        self._heapify_up()

    def pop(self):
        if not self.is_empty():
            if len(self.elements) == 1:
                return self.elements.pop()[0]
            
            top_item = self.elements[0][0]
            last_item = self.elements.pop()
            self.elements[0] = last_item
            self._heapify_down()
            return top_item
        else:
            raise IndexError("Priority queue is empty")
        
    def _heapify_up(self):
        index = len(self.elements) - 1
        while index >0 :
            parent_index = (index-1)//2
            if self.elements[index][1] < self.elements[parent_index][1]:
                self.elements[index], self.elements[parent_index] = self.elements[parent_index], self.elements[index]
                index = parent_index
            else:
                break

    def _heapify_down(self):
        index = 0 
        while True:
            left_child_index = 2*index + 1
            right_child_index = 2*index + 2
            smallest = index

            if (
                left_child_index < len(self.elements) and
                self.elements[left_child_index][1] < self.elements[smallest][1]
            ): smallest = left_child_index

            if (
                right_child_index < len(self.elements) and 
                self.elements[right_child_index][1] < self.elements[smallest][1]
            ): smallest = right_child_index

            if smallest != index:
                self.elements[index], self.elements[smallest] = self.elements[smallest], self.elements[index]
                index = smallest 

            else:
                break

pq = PriorityQueue()
pq.push("Task1", 4)
pq.push("Task2", 1)
pq.push("Task3", 6)
pq.push("Task4", 3)
pq.push("Task5", 7)

while not pq.is_empty():
    item = pq.pop()
    print(item)
