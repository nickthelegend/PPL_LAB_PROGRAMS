def remove_word(input_string, word):
    return input_string.replace(word, '')
result = remove_word("Hello world, Hello people!", "Hello")
print(result)