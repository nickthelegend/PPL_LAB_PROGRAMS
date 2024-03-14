def generate_binary_strings(n):
  if n <= 0:
    return []
  if n == 1:
    return ['0', '1']
  else:
    prev_strings = generate_binary_strings(n - 1)
    new_strings = [string + '0' for string in prev_strings
                   ] + [string + '1' for string in prev_strings]
    return new_strings


binary_strings = generate_binary_strings(3)
print(binary_strings)
