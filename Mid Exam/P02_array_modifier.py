# You are given an array with integers. Write a program to modify the elements after receiving the following commands:
# •	"swap {index1} {index2}" takes two elements and swap their places. •	"multiply {index1} {index2}" takes element
# at the 1st index and multiply it with the element at 2nd index. Save the product at the 1st index. •	"decrease"
# decreases all elements in the array with 1. Input On the first input line, you will be given the initial array
# values separated by a single space. On the next lines you will receive commands until you receive the command "end".
# The commands are as follow: •	"swap {index1} {index2}" •	"multiply {index1} {index2}" •	"decrease" Output The
# output should be printed on the console and consist of elements of the modified array – separated by a comma and a
# single space ", ". Constraints •	Elements of the array will be integer numbers in the range [-231...231] •	Count
# of the array elements will be in the range [2...100] •	Indexes will be always in the range of the array

initial_array = list(map(int, input().split(" ")))
command = input()
while command != "end":
    command_line = command.split(" ")
    command_text = command_line[0]
    if command_text == "swap":
        index_swap1 = int(command_line[1])
        index_swap2 = int(command_line[2])
        initial_array[index_swap1], initial_array[index_swap2] = initial_array[index_swap2], initial_array[index_swap1]
    elif command_text == "multiply":
        index1 = int(command_line[1])
        index2 = int(command_line[2])
        initial_array[index1] = initial_array[index1] * initial_array[index2]

    elif command_text == "decrease":
        initial_array = [num - 1 for num in initial_array]
    command = input()
initial_array_to_string = list(map(str, initial_array))
print(", ".join(initial_array_to_string))