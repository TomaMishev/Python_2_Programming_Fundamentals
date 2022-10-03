# Write a program that reads an integer number representing a budget.
# On the following lines, it reads integer numbers representing the prices of each product you should buy until
# it receives the command "End".
# During the iterations, if there is not enough budget left to buy the next product, it prints
# "You went in overdraft!" and end the program.
# Otherwise, if you accomplished to buy all products before receiving "End", it prints "You bought everything needed."

budget = int(input())
command_line = input()
is_over_budget = False
while command_line != "End":
    current_price = float(command_line)
    if budget >= current_price:
        budget -= current_price
        command_line = input()
    else:
        is_over_budget = True
        break
if not is_over_budget:
    print("You bought everything needed.")
else:
    print("You went in overdraft!")