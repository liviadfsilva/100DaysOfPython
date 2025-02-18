list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(i) for i in list_of_strings]
result = [n for n in numbers if n % 2 == 0]
print(result)