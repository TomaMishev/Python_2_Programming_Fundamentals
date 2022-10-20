# On the first line, you will receive a string. On the second line, you will receive a second string. Write a program
# that removes all the occurrences of the first string in the second until there is no match. At the end,
# print the remaining string.

first_srt = input()
second_str = input()

while first_srt in second_str:
    second_str = second_str.replace(first_srt, "")
print(second_str)