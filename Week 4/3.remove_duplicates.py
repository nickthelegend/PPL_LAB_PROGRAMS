def remove_duplicates():
  """
    Removes duplicates from a list.
    """

  list1 = input("Enter a list of numbers separated by spaces: ")
  list1 = [int(x) for x in list1.split()]
  list1 = list(set(list1))
  return list1
