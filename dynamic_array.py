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
        return self.next_index == 0

    def __len__(self):
        return self.next_index

    def append(self, value):
        self.increase_capacity()
        self.data[self.next_index] = value
        self.next_index += 1

    def __getitem__(self, index):
        if 0 <= index < self.next_index:
            return self.data[index]
        else:
            raise (IndexError)

    def clear(self):
        self.next_index = 0

    def pop(self):
        if self.next_index == 0:
            raise (IndexError) 
        self.next_index -= 1
        return self.data[self.next_index]

    def delete(self, index):
        if 0 <= index < self.next_index:
            for i in range(index, self.next_index - 1):
                 self.data[i] = self.data[i + 1] 
            self.next_index -= 1 
        else:
            raise (IndexError)

    def is_full(self):
        return self.next_index >= self.capacity

    def increase_capacity(self):
        new_arr_capacity = self.capacity*2
        if self.is_full():
            new_array = np.empty(new_arr_capacity, dtype=np.object)
            for i, x in enumerate(self.data):
                new_array[i] = x
            self.data = new_array
            self.capacity = new_arr_capacity

    def insert(self, index, value):
        if 0 <= index <= self.next_index:
            self.next_index += 1
            if self.is_full():
                self.increase_capacity()
            for i in range(self.next_index, index, -1):
                self.data[i] = self.data[i - 1]
            self.data[index] = value
        else:
            raise (IndexError)

    def linear_search(self, value):
        for i, x in enumerate(self.data):
            if x == value:
                return i
        return None

    def max(self):
        max_value = self.data[0]
        for i in self.data:
            if i == None:
                True
            elif i > max_value:
                max_value = i
        return max_value

    def min(self):
        min_value = self.data[0]
        for i in self.data:
            if i == None:
                True
            elif i < min_value:
                min_value = i
        return min_value

    def sum(self):
        summed_array = 0
        for i in range(self.next_index):
            summed_array += self.data[i]
        if summed_array == 0:
            return None
        return summed_array
    pass
