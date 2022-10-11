# Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers.

numbers_string = input().split(", ")
list_of_even_indexes = []
for i in range(len(numbers_string)):
    if int(numbers_string[i]) % 2 == 0:
        list_of_even_indexes.append(i)
print(list_of_even_indexes)