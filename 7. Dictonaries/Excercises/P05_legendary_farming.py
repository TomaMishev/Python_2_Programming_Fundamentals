# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. However,
# it's a tedious process, and it requires quite a bit of farming. The possible items are: •	"Shadowmourne" - requires
# 250 Shards •	"Valanyr" - requires 250 Fragments •	"Dragonwrath" - requires 250 Motes "Shards", "Fragments",
# and "Motes" are the key materials 	(case-insensitive), and everything else is junk. You will be given lines of
# input in the format: "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}" Keep track of the
# key materials - the first one that reaches 250, wins the race. At that point, you have to print that the
# corresponding legendary item is obtained. In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards} fragments: {number_of_fragments} motes: {number_of_motes}" Finally, print the collected
# junk items in the order of appearance.

key_items_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_items_dict = {}
obtained = False
while True:
    command_line = input().split(" ")
    for i in range(0, len(command_line), 2):
        qty = int(command_line[i])
        material = command_line[i + 1].lower()

        if material == "shards" or material == "fragments" or material == "motes":
            if material not in key_items_dict:
                key_items_dict[material] = qty
            else:
                key_items_dict[material] += qty
        else:
            if material not in junk_items_dict:
                junk_items_dict[material] = qty
            else:
                junk_items_dict[material] += qty

        if material == "shards":
            if key_items_dict[material] >= 250:
                obtained = True
                print(f"Shadowmourne obtained!")
                key_items_dict[material] -= 250
                break
        elif material == "fragments":
            if key_items_dict[material] >= 250:
                obtained = True
                print(f"Valanyr obtained!")
                key_items_dict[material] -= 250
                break
        elif material == "motes":
            if key_items_dict[material] >= 250:
                obtained = True
                print(f"Dragonwrath obtained!")
                key_items_dict[material] -= 250
                break
    if obtained:
        break

print(f"shards: {key_items_dict['shards']}")
print(f"fragments: {key_items_dict['fragments']}")
print(f"motes: {key_items_dict['motes']}")

for key, value in junk_items_dict.items():
    print(f"{key}: {value}")