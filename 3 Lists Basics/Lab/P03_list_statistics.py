# On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"

total_numbers = int(input())
positives_list = list()
negatives_list = list()
for num in range(total_numbers):
    current_num = int(input())
    if current_num >= 0:
        positives_list.append(current_num)
    else:
        negatives_list.append(current_num)
print(positives_list)
print(negatives_list)
print(f"Count of positives: {len(positives_list)}")
print(f"Sum of negatives: {sum(negatives_list)}")