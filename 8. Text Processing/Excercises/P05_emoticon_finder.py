# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.

text = input()
for i in range(len(text)):
    if text[i] == ":" and text[i + 1] != " ":
        print(text[i] + text[i + 1])