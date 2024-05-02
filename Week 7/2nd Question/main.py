def check_words_in_file(file_name, words_to_check):
  try:
    with open(file_name, 'r') as file:
      content = file.read()
      for word in words_to_check:
        if word in content:
          print(f"Found: {word}")
  except FileNotFoundError:
    print(f"File '{file_name}' not found.")


def main():
  words_to_check = ["sad", "her", "intovert"]
  file_name = "sample.txt"
  check_words_in_file(file_name, words_to_check)


if __name__ == "__main__":
  main()
