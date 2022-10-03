# Write a program that receives three whole numbers and prints the largest one.

num1 = int(input())
num2 = int(input())
num3 = int(input())

output = 0
if num1 > num2 and num1 > num3:
    output = num1
elif num2 > num1 and num2 > num3:
    output = num2
else:
    output = num3

print(output)
