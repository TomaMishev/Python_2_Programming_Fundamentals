# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.

def factorial(num):
    fact = 1
    for number in range(1, num + 1):
        fact *= number
    return fact


num1 = int(input())
num2 = int(input())
result = factorial(num1) / factorial(num2)
print(f"{result:.2f}")