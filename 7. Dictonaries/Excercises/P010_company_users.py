# Write a program that keeps the information about companies and their employees. You will be receiving company names
# and an employees' id until you receive the command "End" command. Add each employee to the given company. Keep in
# mind that a company cannot have two employees with the same id. Print the company name and each employee's id in the
# following format: "{company_name} -- {id1} -- {id2} … -- {idN}" Input / Constraints •	Until you receive the "End"
# command, you will be receiving input in the format: "{company_name} -> {employee_id}". •	The input always will be
# valid.

command = input()
id_dict = {}

while command != "End":
    command_line = command.split(" -> ")
    company = command_line[0]
    user_id = command_line[1]
    if company not in id_dict:
        id_dict[company] = set([user_id])
        sorted(id_dict[company])
    else:
        id_dict[company].add(user_id)

    command = input()

for key, values in id_dict.items():
    print(f"{key}")
    for i in values:
        print(f"-- {i}")

