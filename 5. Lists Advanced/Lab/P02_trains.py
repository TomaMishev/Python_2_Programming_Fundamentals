# You will receive a number representing the number of wagons a train has. Create a list (train) with the given length
# containing only zeros. Until you receive the command "End", you will receive some of the following commands: •
# "add {people}" – you should add the number of people in the last wagon •	"insert {index} {people}" - you should add
# the number of people at the given wagon •	"leave {index} {people}" - you should remove the number of people from the
# wagon. There will be no case in which the people will be more than the count in the wagon. There will be no case in
# which the index is invalid! After you receive the "End" command print the train.

wagons_count = int(input())
wagons_list = [0 for wagons in range(wagons_count)]
command = input()

while command != "End":
    command_line = command.split(" ")
    command_text = command_line[0]
    if command_text == "add":
        add_people = int(command_line[1])
        wagons_list[-1] += add_people
    elif command_text == "insert":
        wagon_index = int(command_line[1])
        add_people = int(command_line[2])
        wagons_list[wagon_index] += add_people
    elif command_text == "leave":
        wagon_index = int(command_line[1])
        add_people = int(command_line[2])
        wagons_list[wagon_index] -= add_people
    command = input()

print(wagons_list)