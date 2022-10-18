# Write a program that receives info from the console about people and their phone numbers. Each entry should have a
# name and a number (both strings) separated by a "-". If you receive a name that already exists in the phonebook,
# update its number. After filling the phonebook, you will receive a number – N. Your program should be able to
# perform a search of contact by name and print its details in the format: "{name} -> {number}". In case the contact
# isn't found, print: "Contact {name} does not exist."

string_input = input().split("-")
phonebook_dict = {}
while not string_input[0].isdigit():
    if string_input[0] not in phonebook_dict:
        phonebook_dict[string_input[0]] = string_input[1]

    string_input = input().split("-")
searches = int(string_input[0])
for i in range(searches):
    name = input()
    if name not in phonebook_dict:
        print(f"Contact {name} does not exist.")
    else:
        print(f"{name} -> {phonebook_dict[name]}")