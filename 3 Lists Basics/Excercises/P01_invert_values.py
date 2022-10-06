# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.

default_list = input().split(" ")
filtered_list = list()
for value in default_list:
    if int(value) >= 0:
        filtered_list.append(-int(value))
    else:
        filtered_list.append(abs(int(value)))
print(filtered_list)
