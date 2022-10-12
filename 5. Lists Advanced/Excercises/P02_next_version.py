# You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}". Your task is
# to print the next version. For example, if the current version is "1.3.4", the next version will be "1.3.5". The
# only rule is that the numbers cannot be greater than 9. If it happens, set the current number to 0 and increase the
# previous number. For more clarification, see the examples below. Note: there will be no case in which the first
# number will become greater than 9.

current_version = input().split(".")
number = int("".join(current_version))
number += 1
number_to_str = str(number)
number_list = []
for i in range(0, len(number_to_str)):
    number_list += number_to_str[i]
print(".".join(number_list))
