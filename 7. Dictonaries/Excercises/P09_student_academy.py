# Write a program that keeps the information about students and their grades. On the first line, you will receive an
# integer number representing the next pair of rows. On the next lines, you will be receiving each student's name and
# their grade. Keep track of all grades for each student and keep only the students with an average grade higher than
# or equal to 4.50. Print the final dictionary with students and their average grade in the following format: "{name}
# -> {averageGrade}" Format the average grade to the 2nd decimal place.

count = int(input())
grades_dict = {}
for i in range(count):
    name = input()
    grade = float(input())
    if name not in grades_dict:
        grades_dict[name] = [grade]
    else:
        grades_dict[name].append(grade)

grades_above_average = {}
for key, value in grades_dict.items():
    avg = sum(value) / len(value)
    if avg >= 4.50:
        grades_above_average[key] = f"{avg:.2f}"

for key, value in grades_above_average.items():
    print(f"{key} -> {value}")
