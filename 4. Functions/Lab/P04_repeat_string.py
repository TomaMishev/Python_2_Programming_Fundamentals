# Write a function that receives a string and a counter n. The function should return a new string – the result of
# repeating the old string n times. Print the result of the function. Try using lambda.

repeat_string_function = lambda str_to_repeat, count_times: str_to_repeat * count_times

input_string = input()
count = int(input())
result_string = repeat_string_function(input_string, count)

print(result_string)



