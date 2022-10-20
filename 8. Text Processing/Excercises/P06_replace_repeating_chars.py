# Write a program that reads a string from the console and replaces any sequence of the same letters with a single
# corresponding letter.

text = input()
result = []
for i in range(len(text) - 1):
    current_char = text[i]
    next_char = text[i + 1]
    if current_char != next_char:
        result.append(current_char)

result.append(text[-1])
print(f"{''.join(result)}")


