def analyze_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        num_words = len(content.split())
        num_vowels = sum([1 for char in content if char.lower() in 'aeiou'])
        num_spaces = content.count(' ')
        num_lower_case = sum([1 for char in content if char.islower()])
        num_upper_case = sum([1 for char in content if char.isupper()])

    print(f"Number of words: {num_words}")
    print(f"Number of vowels: {num_vowels}")
    print(f"Number of spaces: {num_spaces}")
    print(f"Number of lowercase letters: {num_lower_case}")
    print(f"Number of uppercase letters: {num_upper_case}")


file_name = "sample.txt"
analyze_file(file_name)