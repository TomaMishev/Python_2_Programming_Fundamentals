# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().

input_list = map(int, list(input().split(" ")))
filtered_list = list(filter(lambda i: i % 2 == 0, input_list))
print(filtered_list)