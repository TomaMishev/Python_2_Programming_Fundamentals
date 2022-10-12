# Write a program that prints you a receipt for your new computer. You will receive the parts' prices (without tax)
# until you receive what type of customer this is - special or regular. Once you receive the type of customer you
# should print the receipt. The taxes are 20% of each part's price you receive. If the customer is special,
# he has a 10% discount on the total price with taxes. If a given price is not a positive number, you should print
# "Invalid price!" on the console and continue with the next price. If the total price is equal to zero, you should
# print "Invalid order!" on the console. Input •	You will receive numbers representing prices (without tax) until
# command "special" or "regular": Output •	The receipt should be in the following format: "Congratulations you've
# just bought a new computer! Price without taxes: {total price without taxes}$ Taxes: {total amount of taxes}$
# ----------- Total price: {total price with taxes}$" Note: All prices should be displayed to the second digit after
# the decimal point! The discount is applied only on the total price. Discount is only applicable to the final price!

command = input()

total_price_without_tax = 0
total_tax = 0

while command != "special" and command != "regular":
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
        command = input()
        continue
    tax = current_price * 0.20
    total_price_without_tax += current_price
    total_tax += tax
    command = input()

total_price = total_price_without_tax + total_tax
if total_price == 0:
    print(f"Invalid order!")
else:
    if command == "regular":
        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price_without_tax:.2f}$")
        print(f"Taxes: {total_tax:.2f}$")
        print("-----------")
        print(f"Total price: {total_price:.2f}$")
    elif command == "special":
        total_price *= 0.90
        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price_without_tax:.2f}$")
        print(f"Taxes: {total_tax:.2f}$")
        print("-----------")
        print(f"Total price: {total_price:.2f}$")
