with open('file1.txt', 'r') as file1:
  data1 = file1.read()

with open('file2.txt', 'r') as file2:
  data2 = file2.read()

with open('merged_file.txt', 'w') as merged_file:
  print("DONE")
  merged_file.write(data1 + data2)
with open('merged_file.txt', 'r') as merged_file:
  data3 = merged_file.read()
  print(data3)
