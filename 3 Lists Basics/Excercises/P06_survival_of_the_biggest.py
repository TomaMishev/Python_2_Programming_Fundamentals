# Write a program that receives a list of integer numbers (separated by a single space) and a number n. The number n
# represents the count of numbers to remove from the list. You should remove the smallest ones, and then, you should
# print all the numbers that are left in the list, separated by a comma and a space ", ".


string_list = input().split(" ")
remove_count = int(input())
numbers_list = []
for i in string_list:
    num_to_int = int(i)
    numbers_list.append(num_to_int)
for i in range(remove_count):
    num_to_remove = min(numbers_list)
    numbers_list.remove(num_to_remove)
final_list = list(map(str, numbers_list))
print(", ".join(final_list))

