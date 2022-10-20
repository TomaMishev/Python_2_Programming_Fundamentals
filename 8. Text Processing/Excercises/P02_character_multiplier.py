# Create a program that receives two strings on a single line separated by a single space. Then, it prints the sum of
# their multiplied character codes as follows: multiply str1[0] with str2[0] and add the result to the total sum,
# then continue with the next two characters. If one of the strings is longer than the other, add the remaining
# character codes to the total sum without multiplication.

text = input().split(" ")
first_str = text[0]
second_str = text[1]
total_sum = 0
if len(first_str) >= len(second_str):
    for i in range(len(first_str)):
        if i < len(second_str):
            result = ord(first_str[i]) * ord(second_str[i])
            total_sum += result
        else:
            total_sum += ord(first_str[i])
else:
    for i in range(len(second_str)):
        if i < len(first_str):
            result = ord(first_str[i]) * ord(second_str[i])
            total_sum += result
        else:
            total_sum += ord(second_str[i])
print(total_sum)