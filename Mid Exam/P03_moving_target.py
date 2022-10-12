#
# You are at the shooting gallery again, and you need a program that helps you keep track of moving targets. On the
# first line, you will receive a sequence of targets with their integer values, split by a single space. Then,
# you will start receiving commands for manipulating the targets until the "End" command. The commands are the
# following: •	"Shoot {index} {power}" o	Shoot the target at the index if it exists by reducing its value by the
# given power (integer value). o	Remove the target if it is shot. A target is considered shot when its value
# reaches 0. •	"Add {index} {value}" o	Insert a target with the received value at the received index if it exists.
# o	If not, print: "Invalid placement!" •	"Strike {index} {radius}" o	Remove the target at the given index and the
# ones before and after it depending on the radius. o	If any of the indices in the range is invalid, print: "Strike
# missed!" and skip this command. Example:  "Strike 2 2" {radius}	{radius}	{strikeIndex}	{radius}	{radius}
#
# •	"End"
# o	Print the sequence with targets in the following format and end the program:
# "{target1}|{target2}…|{targetn}"
# Input / Constraints
# •	On the first line, you will receive the sequence of targets – integer values [1-10000].
# •	On the following lines, until the "End" will be receiving the command described above – strings.
# •	There will never be a case when the "Strike" command would empty the whole sequence.
# Output
# •	Print the appropriate message in case of any command if necessary.
# •	In the end, print the sequence of targets in the format described above.


targets_list = list(map(int, input().split(" ")))
command = input()
while command != "End":
    command_line = command.split(" ")
    command_text = command_line[0]
    if command_text == "Shoot":
        index = int(command_line[1])
        power = int(command_line[2])
        if 0 <= index < len(targets_list):
            targets_list[index] -= power
            if targets_list[index] <= 0:
                targets_list.pop(index)
    elif command_text == "Add":
        index = int(command_line[1])
        value = int(command_line[2])
        if 0 <= index < len(targets_list):
            targets_list.insert(index, value)
        else:
            print("Invalid placement!")
    elif command_text == "Strike":
        index = int(command_line[1])
        radius = int(command_line[2])
        before_index = index + radius
        after_index = index - radius
        current_index = index
        if 0 <= index < len(targets_list) and 0 <= before_index < len(targets_list) and \
                0 <= after_index < len(targets_list):
            targets_list.pop(index - radius)
            targets_list.pop(index)
            targets_list.pop(index - 1)
        else:
            print(f"Strike missed!")
            command = input()
            continue
    command = input()
targets_list_to_string = list(map(str, targets_list))
print("|".join(targets_list_to_string))
