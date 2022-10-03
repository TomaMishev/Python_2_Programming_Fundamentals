# Write a program that reads a floating-point number and:
# -	prints "zero" if the number is zero
# -	prints "positive" or "negative"
# -	adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds  1 000 000

number = float(input())

output = ""
if number == 0:
    output = "zero"
elif number > 0:
    output = "positive"
    if number < 1:
        output = "small positive"
    elif number > 1000000:
        output = "large positive"
elif number < 0:
    output = "negative"
    if number > -1:
        output = "small negative"
    elif number < -1000000:
        output = "large negative"

print(output)
