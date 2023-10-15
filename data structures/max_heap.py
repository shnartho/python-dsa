class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return self.size() == 0
    
    def insert(self, item):
        self.heap.append(item)
        self._heapify_up()

    def extract_max(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        if self.size() == 1: 
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down()

        return max_value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0]

    def _heapify_up(self):
        index = self.size() - 1 
        while index > 0:
            parent_index = (index -1 ) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index

            else:
                break
    
    def _heapify_down(self):
        index = 0
        while index > 0:
            left_child_index = (index*2) + 1
            right_child_index = (index*2) + 2
            largest = index

            if (
                left_child_index < self.size() and 
                self.heap[left_child_index] > self.heap[largest]
            ): largest = left_child_index

            if (
                right_child_index < self.size() and 
                self.heap[right_child_index] > self.heap[largest]
            ): largest = right_child_index

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break
    
    def print_heap(self):
        if self.is_empty():
            print("Max Heap is empty")
            return

        height = (self.size() - 1).bit_length()  # Calculate the height of the heap
        max_width = 2 ** height  # Maximum width of the last level

        level = 0
        elements_in_level = 1
        element_index = 0

        while element_index < self.size():
            elements_in_level = min(elements_in_level, self.size() - element_index)

            # Calculate the spacing for proper alignment
            spacing = (max_width * 4) // (elements_in_level * 2)

            for _ in range(elements_in_level):
                # Print the element with appropriate spacing
                print(f"{self.heap[element_index]:{spacing}}", end=" ")
                element_index += 1

            print()  # Move to the next line
            level += 1
            elements_in_level *= 2

max_heap = MaxHeap()
max_heap.insert(4)
max_heap.insert(14)
max_heap.insert(42)
max_heap.insert(3)
max_heap.insert(13)
max_heap.insert(15)
max_heap.insert(7)
max_heap.insert(8)
max_heap.insert(9)
max_heap.insert(2)
max_heap.insert(11)
max_heap.insert(17)
max_heap.insert(19)
max_heap.insert(22)

print("Max heap:")
#while not max_heap.is_empty():
#    print(max_heap.extract_max())
max_heap.print_heap()