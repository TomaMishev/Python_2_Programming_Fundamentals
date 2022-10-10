# You will receive a single number. You should write a function that returns the sum of all even and all odd digits
# in a given number. The result should be returned as a single string in the format: "Odd sum = {sum_of_odd_digits},
# Even sum = {sum_of_even_digits}" Print the result of the function on the console.

def even_odd_sum(string):
    even_sum = 0
    odd_sum = 0
    for i in range(0, len(string)):
        current_num = int(string[i])
        if current_num % 2 == 0:
            even_sum += current_num
        else:
            odd_sum += current_num
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


num = input()
even_odd_sum(num)
