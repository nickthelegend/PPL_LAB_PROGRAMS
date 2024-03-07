"""
 i) Write a program to convert a list and tuple into arrays

"""
import numpy as np

# Convert list to array
list_data = [1, 2, 3, 4, 5]
array_from_list = np.array(list_data)
print("Array from list:")
print(array_from_list)

# Convert tuple to array
tuple_data = (6, 7, 8, 9, 10)
array_from_tuple = np.array(tuple_data)
print("\nArray from tuple:")
print(array_from_tuple)
