class MinHeap:
    def __init__(self) -> None:
        self.heap = []

    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return self.size() == 0
    
    def insert(self, item):
        #step 1: add the new item to the end of the heap
        self.heap.append(item)
        # step 2: restore the heap property by moving the newly added item up.
        self._heapify_up()

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        if self.size() == 1:
            # if there is only one item in the heap, remove and return it
            return self.heap.pop()
        
        #step 1: Replace the root (minimum element) with the last item in the heap
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        #step 2 restore the heap property by moving the new root down to its correct position
        self._heapify_down()
        return min_value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def _heapify_up(self):
        index = self.size() -1 
        while index > 0:
            # lets calculate the parent index for the curent node
            parent_index = (index -1 )//2
            if self.heap[index] < self.heap[parent_index]:
                # if the child is smaller than its parent, swap them
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index

            else:
                # the hepa priority is restored
                break

    def _heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index
            if (
                left_child_index < self.size() and
                self.heap[left_child_index] < self.heap[smallest]
            ): smallest = left_child_index

            if (
                right_child_index < self.size() and 
                self.heap[right_child_index] < self.heap[smallest]
            ): smallest = right_child_index

            if smallest != index: 
                # if the smallest child is smaller than the parent, swap them
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

min_heap = MinHeap()
min_heap.insert(5)
min_heap.insert(55)
min_heap.insert(15)
min_heap.insert(4)
min_heap.insert(3)
min_heap.insert(44)
min_heap.insert(51)
min_heap.insert(25)
min_heap.insert(45)
min_heap.insert(35)
min_heap.insert(11)

print("Min heap:")
while not min_heap.is_empty():
    print(min_heap.extract_min())

