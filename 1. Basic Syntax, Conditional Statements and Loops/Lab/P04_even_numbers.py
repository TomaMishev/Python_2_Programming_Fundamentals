# Write a program that receives a number n on the first line. On the following n lines, it receives different
# integer numbers. If the program receives an odd number, print "{num} is odd!" and end the program.
# Otherwise, if all numbers given are even, print "All numbers are even.".
number_of_iterations = int(input())
is_number_even = True
odd_number = 0


for i in range(number_of_iterations):
    current_number = int(input())
    if current_number % 2 == 0:
        continue
    else:
        odd_number = current_number
        is_number_even = False
        break
if is_number_even:
    print("All numbers are even.")
else:
    print(f"{odd_number} is odd!")


