# You will be given strings until you receive the command "End".
# For each string given, you should print a string in which each character (case-sensitive) is repeated twice.
# Note that if you receive the string "SoftUni", you should NOT print it!

command = input()

while command != "End":
    output = ""
    if command == "SoftUni":
        command = input()
        continue
    for char in command:
        output += char * 2
    print(output)
    command = input()

