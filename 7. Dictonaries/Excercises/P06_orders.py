# Write a program that keeps the information about products and their prices. Each product has a name, a price,
# and a quantity: •	If the product doesn't exist yet, add it with its starting quantity. •	If you receive a product,
# which already exists, increases its quantity by the input quantity and if its price is different, replace the price
# as well. You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy",
# keep adding items. Finally, print all items with their names and the total price of each product. Input •	Until you
# receive "buy", the products will be coming in the format: "{name} {price} {quantity}". •	The product data is always
# delimited by a single space. Output •	Print information about each product in the following format: "{product_name}
# -> {total_price}" •	Format the total price to the 2nd digit after the decimal separator.

command = input()
orders = {}

while command != "buy":
    command_line = command.split(" ")
    product = command_line[0]
    price = float(command_line[1])
    qty = int(command_line[2])

    if product in orders:
        orders[product] = [price, qty + orders[product][1]]
    else:
        orders[product] = [price, qty]

    command = input()

for i in orders.keys():
    total_sum = orders[i][0] * orders[i][1]
    print(f"{i} -> {total_sum:.2f}")