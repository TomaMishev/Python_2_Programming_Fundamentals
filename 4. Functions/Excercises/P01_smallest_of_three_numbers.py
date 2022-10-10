# Write a function that receives three integer numbers and returns the smallest.
# Print the result on the console. Use an appropriate name for the function.

def smallest_num(a, b, c):
    return min(a, b, c)


num1 = int(input())
num2 = int(input())
num3 = int(input())


print(smallest_num(num1, num2, num3))
