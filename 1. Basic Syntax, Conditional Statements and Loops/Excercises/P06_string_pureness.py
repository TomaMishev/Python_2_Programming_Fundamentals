# You will be given number n. After that, you'll receive different strings n times.
# Your task is to check if the given strings are pure, meaning that they do NOT consist of any of the characters:
# comma ",", period ".", or underscore "_":
# •	If a string is pure, print "{string} is pure."
# •	Otherwise, print "{string} is not pure!"

number_of_strings = int(input())
for string in range(number_of_strings):
    is_pure = True
    current_string = input()
    for char in current_string:
        if char == "," or char == "." or char == "_":
            is_pure = False
            break
    if is_pure:
        print(f"{current_string} is pure.")
    else:
        print(f"{current_string} is not pure!")


