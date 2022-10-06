# Write a program that receives two numbers (factor and count).
# It should create a list with a length of the given count that contains only integer numbers,
# which are multiples of the given factor. The numbers should be only positive, and they should be arranged in
# ascending order, starting from the value of the factor.

factor = int(input())
count = int(input())
values_list = list()
for value in range (1, count + 1):
    values_list.append(value * factor)
values_list.sort()
print(values_list)