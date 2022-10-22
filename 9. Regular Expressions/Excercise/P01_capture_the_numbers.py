# Write a program that receives strings on different lines and extracts only the numbers. Print all extracted numbers
# on a single line, separated by a single space.
import re
regex = r"\d+"

while True:
    text = input()

    if not text:
        break

    matches = re.findall(regex, text)
    final_result = []
    for match in matches:
        final_result.append(match)
    for i in final_result:
        print(i, end=" ")
