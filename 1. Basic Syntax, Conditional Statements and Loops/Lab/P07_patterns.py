# Write a program that receives a number and creates the following pattern.
# The number represents the largest count of stars on one row.

number = int(input())

for i in range(number):
    for j in range(0, i + 1):
        print("*", end="")
    print()

for i in range(number - 1, -1, -1):
    for j in range(0, i):
        print("*", end="")
    print()
