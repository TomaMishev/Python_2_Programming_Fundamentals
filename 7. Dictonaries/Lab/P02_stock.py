# You will be given key-value pairs of products and quantities (on a single line separated by space). On the following
# line, you will be given products to search for. Check for each product. You have 2 possibilities: •	If you have
# the product, print "We have {quantity} of {product} left". •	Otherwise, print "Sorry, we don't have {product}".

text = input().split(" ")
stock = dict()
searched_products = input().split(" ")

for i in range(0, len(text), 2):
    product = text[i]
    quantity = text[i + 1]
    stock[product] = quantity
for product in searched_products:
    if product in stock.keys():
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")