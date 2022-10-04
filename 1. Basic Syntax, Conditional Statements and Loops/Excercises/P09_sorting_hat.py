# Help out the sorting hat to sort the new students in the houses of Hogwarts.
# You will be receiving names until the command "Welcome!".
# The length of each name determines in which house the student is going:
# •	If the name is less than 5 chars, the student is going into Gryffindor
# o	Print "{name} goes to Gryffindor."
# •	If the name is exactly 5 chars, the student is going into Slytherin
# o	Print "{name} goes to Slytherin."
# •	If the name is exactly 6 chars, the student is going into Ravenclaw
# o	Print "{name} goes to Ravenclaw."
# •	If the name is more than 6 chars, the student is going into Hufflepuff
# o	Print "{name} goes to Hufflepuff."
# While receiving names, if you receive "Voldemort", print "You must not speak of that name!" and end the program.
# No more sorting for today!
# If all students are sorted successfully, print "Welcome to Hogwarts."

student_name = input()
is_name_wrong = False
while student_name != "Welcome!":
    if student_name == "Voldemort":
        is_name_wrong = True
        break
    name_length = len(student_name)
    if name_length < 5:
        print(f"{student_name} goes to Gryffindor.")
    elif name_length == 5:
        print(f"{student_name} goes to Slytherin.")
    elif name_length == 6:
        print(f"{student_name} goes to Ravenclaw.")
    elif name_length > 6:
        print(f"{student_name} goes to Hufflepuff.")
    student_name = input()
if is_name_wrong:
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")