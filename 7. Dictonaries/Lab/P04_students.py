# You will be receiving names of students, their ID, and a course of programming they have taken in the format "{
# name}:{ID}:{course}". On the last line, you will receive a name of a course in snake case lowercase letters. You
# should print only the information of the students who have taken the corresponding course in the format: "{name} -
# {ID}" on separate lines.

students_dict = {}
while True:
    command = input()

    if ":" not in command:
        searched_course = command.replace("_", " ")
        break
    else:
        information = command.split(":")
        student = information[0]
        st_id = information[1]
        st_course = information[2]
        students_dict[st_id] = {student: st_course}
corresponding_students = {}

for key, value in students_dict.items():
    for name, course in value.items():
        if course == searched_course:
            corresponding_students[name] = key
for name, student_id in corresponding_students.items():
    print(f"{name} - {student_id}")