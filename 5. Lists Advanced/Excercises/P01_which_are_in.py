# You will be given two sequences of strings, separated by ", ". Print a new list containing only the strings from
# the first input line, which are substrings of any string in the second input line.

first_string = input().split(", ")
second_string = input()

final_list = [word for word in first_string if word in second_string]

print(final_list)