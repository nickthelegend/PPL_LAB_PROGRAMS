def is_sorted():
  """
    Checks if a list is sorted.
    """
  # Get the list from the user
  list = input("Enter a list of numbers separated by spaces: ")
  # Convert the list to a list of integers
  list = [int(x) for x in list.split()]
  # Check if the list is sorted
  if list == sorted(list):
    print("The list is sorted.")
  else:
    print("The list is not sorted.")


# Test the function
