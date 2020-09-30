# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Brayden Brown

import numpy as np

class DynamicArray:

    capacity = 10
    data = np.empty(capacity,dtype= 'O')

    def is_empty(self):
        return True

    def __len__(self):
        return 0

    def append(self, value):
        myArray=value

    def __getitem__(self, index):
        return 42

    pass
