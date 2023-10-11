class DynamicArray:
    def __init__(self):
        self.arr = [None]
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self.arr) == 0

    def get(self, index):
        if index < 0 and index >= self.size:
            raise IndexError("Index out of bounds")
        return self.arr[index]
    
    def set(self, index, value):
        if index <0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.arr[index] = value

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if self.size >= len(self.arr):
            self._resize()

        for i in range(self.size, index, -1):
            self.arr[i] = self.arr[i - 1]

        self.arr[index] = value
        self.size += 1

    def append(self, value):
        if self.size >= len(self.arr):
            self._resize()
        self.arr[self.size] = value
        self.size += 1

    def remove(self, value):
        for i in range(self.size):
            if self.arr[i] == value:
                self._shift_left(i)
                return
            
        raise ValueError(f"{value} not found in the array")
    
    def _shift_left(self, index):
        for i in range(index, self.size, -1):
            self.arr[i] = self.arr[i+1]
        self.arr[self.size-1] = None
        self.size -= 1

    def _resize(self):
        new_arr = [None] * (2 * len(self.arr))
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def __str__(self):
        return '|' + ','.join(map(str, self.arr[:self.size])) + '|'
    
arr = DynamicArray()

arr.append(1)
arr.append(4)
arr.append(7)
arr.set(1, 44)
#arr.set(5, 99)
print(arr.get(1))
print(arr.is_empty())
arr.insert(1, 33)
arr.remove(7)
print(arr) # this will automatically call the arr.__str__() function
