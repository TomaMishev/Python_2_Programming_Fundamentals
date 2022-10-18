# You will be given a sequence of strings, each on a new line until you receive the "stop" command. Every odd line on
# the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity. Your task is
# to collect the resources and print them each on a new line. Print the resources and their quantities in the
# following format: "{resource} -> {quantity}" The quantities will be in the range [1 … 2 000 000 000].

command = input()
minerals_dict = {}

while command != "stop":
    resource = command
    qty = int(input())
    if resource not in minerals_dict:
        minerals_dict[resource] = qty
    else:
        minerals_dict[resource] += qty
    command = input()

for key, value in minerals_dict.items():
    print(f"{key} -> {value}")