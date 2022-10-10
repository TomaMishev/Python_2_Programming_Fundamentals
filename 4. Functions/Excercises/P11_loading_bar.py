# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder (0, 10,
# 20, 30...). Your task is to create a function that returns a loading bar depending on the number you have received
# in the input. Print the result on the console. For more clarification, see the examples below.

def loading_bar(number):
    if number == 100:
        print(f"100% Complete!")
        print(f"[%%%%%%%%%%]")
    else:
        percent = number // 10
        dots = 10 - (number // 10)
        print(f"{number}% [{percent * '%'}{dots * '.'}]")
        print(f"Still loading...")


num = int(input())
loading_bar(num)