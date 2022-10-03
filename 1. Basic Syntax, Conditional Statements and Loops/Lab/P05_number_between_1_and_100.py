# Write a program that reads different floating-point numbers from the console.
# When it receives a number between 1 and 100 inclusive, the program should stop reading and should print
# "The number {number} is between 1 and 100".

number_between_1_and_100 = 0
is_number_between_1_and_100 = False
while not is_number_between_1_and_100:
    current_number = float(input())
    if 1 <= current_number <= 100:
        is_number_between_1_and_100 = True
        number_between_1_and_100 = current_number
print(f"The number {number_between_1_and_100} is between 1 and 100")
