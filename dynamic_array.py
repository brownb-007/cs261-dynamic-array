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
        if not 0 <= index < self.next_index:
            raise IndexError("IndexError: index out of range.")
        return self.data[index]

    def clear(self):
        self.next_index = 0

    def pop(self):
        if self.next_index == 0:
            raise IndexError("IndexError: index out of range.") 
        self.next_index -= 1
        return self.data[self.next_index]

    pass
