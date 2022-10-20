# You will be given strings on separate lines until you receive an "end" command. Write a program that reverses
# strings and prints each pair on a separate line in the format "{word} = {reversed_word}".

command = input()

while command != "end":
    current_str = command
    reversed_str = reversed(current_str)
    print(f"{current_str} = {''.join(reversed_str)}")
    command = input()
