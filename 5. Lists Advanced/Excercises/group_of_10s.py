# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints the
# numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}". Examples: •	The numbers 2,
# 8, 4, and 10 fall into the group of 10's. •	The numbers 13, 19, 14, and 15 fall into the group of 20's.

list = input().split(", ")
int_list = [int(el) for el in list]
index = 10
current_list = []
while len(int_list) > 0:
    for el in int_list:
        if el <= index:
            current_list.append(el)
    for el in current_list:
        if el == el in int_list:
            int_list.remove(el)

    print(f"Group of {index}'s: {current_list}")
    current_list = []
    index += 10