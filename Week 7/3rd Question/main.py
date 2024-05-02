import re

def find_most_common_word(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        words = re.findall(r'\w+', content.lower())
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        most_common_word = max(word_count, key=word_count.get)
        return most_common_word

most_common_word = find_most_common_word("sample.txt")
print(f"The most common word in the file is: {most_common_word}")