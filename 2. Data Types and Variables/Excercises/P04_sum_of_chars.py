# Write a program, which sums the ASCII codes of N characters and prints the sum on the console. On the first line,
# you will receive N – the number of lines. On the following N lines – you will receive a letter per line. Print the
# total sum in the following format: "The sum equals: {total_sum}".

sum_of_chars = 0
number_of_chars = int(input())
for iteration in range(number_of_chars):
    current_char = input()
    sum_of_chars += ord(current_char)
print(f"The sum equals: {sum_of_chars}")

