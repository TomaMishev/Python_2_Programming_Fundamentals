# Write a program that reads an integer n.
# Then, for all numbers in the range [1, n], prints the number and if it is special or not (True / False).
# A number is special when the sum of its digits is 5, 7, or 11.

integer_n = int(input())
for number in range(1, integer_n + 1):
    current_number = number
    sum = 0
    while current_number > 0:
        digit = current_number % 10
        sum += digit
        current_number //= 10
    if sum == 5 or sum == 7 or sum == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")

