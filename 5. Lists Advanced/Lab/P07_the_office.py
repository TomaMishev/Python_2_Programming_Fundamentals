# You will receive two lines of input:
# •	a list of employees' happiness as a string of numbers separated by a single space
# •	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# •	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"

employee_happiness_list = list(map(int, input().split(" ")))
factor = int(input())
employees_list = [employee * factor for employee in employee_happiness_list]
filtered = list(filter(lambda x: x >= sum(employees_list) / len(employees_list), employees_list))

if len(filtered) >= len(employees_list) / 2:
    print(f"Score: {len(filtered)}/{len(employees_list)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees_list)}. Employees are not happy!")