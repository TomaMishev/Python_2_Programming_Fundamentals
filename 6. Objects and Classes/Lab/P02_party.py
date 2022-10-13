# Create a class Party that only has an attribute people – empty list. The __init__ method should not accept any
# parameters. You will be given names of people (on separate lines) until you receive the command "End". Use the
# created class to solve this problem. After you receive the "End" command, print 2 lines: •	"Going: {people}" -
# the people should be separated by comma and space ", ". •	"Total: {total_people_going}"

class Party:
    def __init__(self):
        self.list = []


party = Party()
command = input()
while command != "End":
    party.list.append(command)
    command = input()
print(f"Going: {', '.join(party.list)}")
print(f"Total: {len(party.list)}")