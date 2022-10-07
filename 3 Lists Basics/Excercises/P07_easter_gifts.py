# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the
# gifts you plan on buying on a single line, separated by space, in the following format: "{gift1} {gift2} {gift3}… {
# giftn}" Then you will start receiving commands until you read the "No Money" message. There are three possible
# commands: •	"OutOfStock {gift}" o	Find the gifts with this name in your collection, if any, and change their
# values to "None". •	"Required {gift} {index}" o	If the index is valid, replace the gift on the given index with
# the given gift. •	"JustInCase {gift}" o	Replace the value of your last gift with this one. In the end,
# print the gifts on a single line, except the ones with value "None", separated by a single space in the following
# format: "{gift1} {gift2} {gift3} … {giftn}" Input / Constraints •	On the 1st line,  you will receive the names of
# the gifts, separated by a single space. •	On the following lines, until the "No Money" command is received,
# you will be receiving commands. •	The input will always be valid. Output •	Print the gifts in the format
# described above.

gift_list = input().split(" ")
command = input()
while command != "No Money":
    command_line_list = command.split(" ")
    if command_line_list[0] == "OutOfStock":
        for i in range(len(gift_list)):
            if gift_list[i] == command_line_list[1]:
                gift_list[i] = "None"

    elif command_line_list[0] == "Required":
        gift = command_line_list[1]
        index = int(command_line_list[2])
        if index >= 0 or index < len(gift_list):
            for i in range(len(gift_list)):
                if i == index:
                    gift_list[i] = gift
    elif command_line_list[0] == "JustInCase":
        gift_list[-1] = command_line_list[1]

    command = input()

for i in gift_list:
    if i == "None":
        continue
    print(i, end=" ")
