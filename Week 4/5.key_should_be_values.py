def invert_dictionary(dictionary):
  return {v: k for k, v in dictionary.items()}


my_dict = {1: 'one', 2: 'two', 3: 'three'}
inverted_dict = invert_dictionary(my_dict)
