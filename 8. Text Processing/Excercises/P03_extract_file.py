# Write a program that reads the path to a file and subtracts the file name and its extension.

path = input().split("\\")
sub_str = path[-1].split(".")
name = sub_str[0]
extension = sub_str[1]
print(f"File name: {name}")
print(f"File extension: {extension}")