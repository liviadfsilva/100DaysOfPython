with open("file1.txt") as file_1_data:
    file_1 = file_1_data.readlines()

with open("file2.txt") as file_2_data:
    file_2 = file_2_data.readlines()

result = [int(n.strip()) for n in file_1 if n in file_2]

print(result)