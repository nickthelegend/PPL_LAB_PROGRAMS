# Find common values between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common_values = set(list1).intersection(list2)
print("Common values between the two lists:")
print(list(common_values))