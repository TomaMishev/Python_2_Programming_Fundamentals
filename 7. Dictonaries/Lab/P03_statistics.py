# You will be receiving key-value pairs on separate lines separated by ": " until you receive the command
# "statistics". Sometimes you may receive a product more than once. In that case, you have to add the new quantity to
# the existing one. When you receive the "statistics" command, print the following: "Products in stock: - {product1}:
# {quantity1} - {product2}: {quantity2} … - {productN}: {quantityN} Total Products: {count_all_products} Total
# Quantity: {sum_all_quantities}"

text = input()
products = dict()

while text != "statistics":
    command = text.split(": ")
    product = command[0]
    qty = int(command[1])

    if product in products.keys():
        products[product] += qty
    else:
        products[product] = qty

    text = input()
print("Products in stock:")
for product, qty in products.items():
    print(f"- {product}: {qty}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")