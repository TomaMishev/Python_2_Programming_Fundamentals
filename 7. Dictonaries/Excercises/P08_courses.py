# Write a program that keeps the information about courses. Each course has a name and registered students. You will
# be receiving a course name and a student name until you receive the command "end". You should register each user
# into the corresponding course. If the given course does not exist, add it. When you receive the command "end",
# print the courses with their names and total registered users. For each course, print the registered users. Input
# •	Until the "end" command is received, you will be receiving input lines in the format: "{course_name} : {
# student_name}" •	The product data is always delimited by " : " Output •	Print the information about each course in
# the following format: "{course_name}: {registered_students}" •	Print the information about each student in the
# following format: "-- {student_name}"


command = input()
courses_dict = {}

while command != "end":
    command_line = command.split(" : ")
    course = command_line[0]
    if course not in courses_dict:
        courses_dict[course] = [command_line[1]]
    else:
        student = command_line[1]
        courses_dict[course].append(student)

    command = input()

for key, value in courses_dict.items():
    print(f"{key}: {len(value)}")
    for i in value:
        print(f"-- {i}")