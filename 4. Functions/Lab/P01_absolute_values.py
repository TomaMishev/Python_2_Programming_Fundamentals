# Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value
# as a list. Use abs().

def convert_list_to_absolute_values(list_to_convert):
    converted_list = list()
    for n in list_to_convert:
        current_num = abs(float(n))
        converted_list.append(current_num)
    return converted_list


input_list = input().split(" ")
edited_list = convert_list_to_absolute_values(input_list)
print(edited_list)
