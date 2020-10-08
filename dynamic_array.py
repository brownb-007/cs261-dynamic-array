# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Brayden Brown

import numpy as np

class DynamicArray:

    def __init__(self):
        self.capacity = 10
        self.data = np.empty(self.capacity, dtype=np.object)
        self.next_index = 0

    def is_empty(self):
        if self.next_index == 0:
            return True
        return False

    def __len__(self):
        return self.next_index

    def append(self, value):
        self.data[self.next_index] = value
        self.next_index += 1

    def __getitem__(self, index):
        if 0 <= index < self.next_index:
            return self.data[index]
        else:
            raise IndexError("IndexError: index out of range.")

    def clear(self):
        self.next_index = 0

    def pop(self):
        if self.next_index == 0:
            raise IndexError("IndexError: index out of range.") 
        self.next_index -= 1
        return self.data[self.next_index]

    def delete(self, index):
        if 0 <= index < self.next_index:
            for i in range(index, self.next_index-1):
                 self.data[i] = self.data[i + 1]
            self.data[self.next_index - 1] = None
            self.next_index -= 1 
        else:
            raise IndexError("IndexError: index out of range.")

    def is_full(self):
        if self.next_index == self.capacity:
            return True
        return False

    pass
