# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and prints
# all the positive, negative, even, and odd numbers on separate lines as shown below. Note: Zero is counted for a
# positive number

numbers = list(map(int, input().split(", ")))
positive = [num for num in numbers if num >= 0]
negatives = [num for num in numbers if num < 0]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

positives_list = list(map(str, positive))
negatives_list = list(map(str, negatives))
even_list = list(map(str, even))
odd_list = list(map(str, odd))

print(f"Positive: {', '.join(positives_list)}")
print(f"Negative: {', '.join(negatives_list)}")
print(f"Even: {', '.join(even_list)}")
print(f"Odd: {', '.join(odd_list)}")