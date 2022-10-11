# You will be receiving to-do notes until you get the command "End". The notes will be in the format: "{importance}-{
# note}". Return a list containing all to-do notes sorted by importance in ascending order. The importance value will
# always be an integer between 1 and 10 (inclusive).

initial_list = ["" for i in range(11)]
command = input()

while command != "End":
    command_line = command.split("-")
    priority = int(command_line[0])
    item = command_line[1]
    initial_list[priority] += item
    command = input()

to_do_list = [item for item in initial_list if item != ""]
print(to_do_list)