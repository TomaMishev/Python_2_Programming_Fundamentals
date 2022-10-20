# Write a program that reads a sequence of strings, separated by a single space. Each string should be repeated N
# times, where N is the length of the string. Print the final strings concatenated into one string.

text = input().split(" ")
output_str = ""
for i in text:
    add_text = i * len(i)
    output_str += add_text
print(output_str)
