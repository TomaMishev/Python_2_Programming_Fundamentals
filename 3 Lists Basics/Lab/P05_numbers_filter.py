# On the first line, you will receive a single number n.
# On the following n lines, you will receive integers. After that, you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

total_elements = int(input())
odd_list = list()
even_list = list()
positive_list = list()
negative_list = list()
for element in range(total_elements):
    current_num = int(input())
    if current_num % 2 == 0:
        even_list.append(current_num)
    else:
        odd_list.append(current_num)

    if current_num >= 0:
        positive_list.append(current_num)
    else:
        negative_list.append(current_num)
word_filter = input()
if word_filter == "even":
    print(even_list)
elif word_filter == "odd":
    print(odd_list)
elif word_filter == "positive":
    print(positive_list)
elif word_filter == "negative":
    print(negative_list)
