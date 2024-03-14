def capitalize_first_letter(sentence):
  words = sentence.split()
  new_sentence = ""
  for word in words:
    new_word = word[0].upper() + word[1:].lower()
    new_sentence += new_word + " "
  return new_sentence.strip()


example_sentence = "hello WoRlD"
capitalized_sentence = capitalize_first_letter(example_sentence)
print(capitalized_sentence)
