# You will be given two strings.
# Transform the first string into the second one, letter by letter, starting from the first one.
# After each interaction, print the resulting string only if it is unique.

str1 = input()
str2 = input()

for ch in range(len(str1)):
    if str1[ch] != str2[ch]:
        replacement = str2[ch]
        word = str1[0:ch] + replacement + str1[ch + 1:]
        str1 = word
        print(str1)
