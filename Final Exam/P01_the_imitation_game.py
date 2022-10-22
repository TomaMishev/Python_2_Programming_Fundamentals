# During World War 2, you are a mathematician who has joined the cryptography team to decipher the enemy's enigma
# code. Your job is to create a program to crack the codes. On the first line of the input, you will receive the
# encrypted message. After that, until the "Decode" command is given, you will be receiving strings with instructions
# for different operations that need to be performed upon the concealed message to interpret it and reveal its true
# content. There are several types of instructions, split by '|' •	"Move {number of letters}": o	Moves the first n
# letters to the back of the string •	"Insert {index} {value}": o	Inserts the given value before the given index in
# the string •	"ChangeAll {substring} {replacement}": o	Changes all occurrences of the given substring with the
# replacement text Input / Constraints •	On the first line, you will receive a string with a message. •	On the
# following lines, you will be receiving commands, split by '|' . Output •	After the "Decode" command is received,
# print this message: "The decrypted message is: {message}"


decrypted_message = input()
command = input()
manipulated_message = [i for i in decrypted_message]

while command != "Decode":
    command_line = command.split("|")
    token = command_line[0]
    if token == "Move":
        number_of_letters = int(command_line[1])
        for i in range(1, number_of_letters + 1):
            ch_to_insert = manipulated_message[0]
            manipulated_message.append(ch_to_insert)
            manipulated_message.pop(0)
    elif token == "Insert":
        index = int(command_line[1])
        value = command_line[2]
        manipulated_message.insert(index, value)
    elif token == "ChangeAll":
        substring = command_line[1]
        replacement = command_line[2]
        current_str = "".join(manipulated_message)
        current_str = current_str.replace(substring, replacement)
        manipulated_message = [i for i in current_str]
    command = input()

print(f"The decrypted message is: {''.join(manipulated_message)}")