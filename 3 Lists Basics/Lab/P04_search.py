# On the first line, you will receive a number n. On the second line, you will receive a word.
# On the following n lines, you will be given some strings. You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.

total_elements = int(input())
searched_word = input()
full_list = list()
filtered_list = list()
for element in range(total_elements):
    current_element = input()
    full_list.append(current_element)
    if searched_word in current_element:
        filtered_list.append(current_element)
print(full_list)
print(filtered_list)