# Kids drink toddy, teens drink coke, young adults drink beer, and adults drink whisky.
# Create a program that receives a person's age and prints what he/she drinks.
age = int(input())
output = ""
if age <= 14:
    output = "drink toddy"
elif age <= 18:
    output = "drink coke"
elif age <= 21:
    output = "drink beer"
else:
    output = "drink whisky"
print(output)