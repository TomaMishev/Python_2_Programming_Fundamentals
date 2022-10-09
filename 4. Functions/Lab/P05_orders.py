# Write a function that calculates the total price of an order and returns it. The function should receive one of the
# following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. The prices for a single
# piece of each product are: •	coffee - 1.50 •	water - 1.00 •	coke - 1.40 •	snacks - 2.00

def calculate_total(product, qty):
    if product == "coffee":
        return qty * 1.50
    elif product == "water":
        return qty * 1
    elif product == "coke":
        return qty * 1.4
    elif product == "snacks":
        return qty * 2


product = input()
qty = int(input())

total_price = calculate_total(product, qty)

print(f"{total_price:.2f}")