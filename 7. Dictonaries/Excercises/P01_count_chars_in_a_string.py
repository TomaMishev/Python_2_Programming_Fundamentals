# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

chars_dict = {}
string_input = input()
for ch in string_input:
    if ch != " ":
        if ch not in chars_dict:
            chars_dict[ch] = 1
        else:
            chars_dict[ch] += 1

for key, value in chars_dict.items():
    print(f"{key} -> {value}")