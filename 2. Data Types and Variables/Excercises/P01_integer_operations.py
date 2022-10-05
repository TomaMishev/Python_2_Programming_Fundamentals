# Write a program that reads four integer numbers.
# It should add the first to the second number, integer divide the sum by the third number,
# and multiply the result by the fourth number. Print the final result.

first_num, second_num, third_num, fourth_num = int(input()), int(input()), int(input()), int(input())
result = (first_num + second_num) // third_num * fourth_num
print(result)