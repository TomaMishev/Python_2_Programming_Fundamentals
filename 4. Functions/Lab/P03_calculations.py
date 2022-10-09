# Example Create a function that receives three parameters, calculates a result depending on the given operator,
# and returns it. Print the result of the function. The input comes as three parameters – an operator as a string and
# two integer numbers. The operator can be one of the following:  "multiply", "divide", "add", "subtract".

def calculation(operator, a, b):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return a // b
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


operator_input = input()
a_input = int(input())
b_input = int(input())

print(calculation(operator_input, a_input, b_input))