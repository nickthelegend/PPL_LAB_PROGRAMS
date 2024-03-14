def has_duplicated():
  """
    Checks if a list has any duplicates.
    """
  # Get the list from the user
  list = input("Enter a list of numbers separated by spaces: ")
  # Convert the list to a list of integers
  list = [int(x) for x in list.split()]
  # Check if the list has any duplicates
  if len(list) != len(set(list)):
    print("The list has duplicates.")
  else:
    print("The list does not have duplicates.")
