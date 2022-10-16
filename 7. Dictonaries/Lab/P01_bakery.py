# You will receive a single line containing some food (keys) and quantities (values). They will be separated by a
# single space (the first element is the key, the second – the value, and so on). Create a dictionary with all the
# keys and values and print it on the console.

text = input().split(" ")
bakery = dict()
for i in range(0, len(text), 2):
    product = text[i]
    quantity = int(text[i + 1])
    bakery[product] = quantity
print(bakery)