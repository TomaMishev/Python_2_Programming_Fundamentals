# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round().

def rounding_funct(default_list):
    modified_list = list()
    for i in default_list:
        current_num = round(float(i))
        modified_list.append(current_num)
    return modified_list


input_list = input().split(" ")
rounded_list = rounding_funct(input_list)

print(rounded_list)
