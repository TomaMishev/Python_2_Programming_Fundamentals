# Peter is a programming enthusiast who wants to create a chat where people will send messages via number codes. He
# starts by creating a program for only four messages. Create a program that receives the n number of messages sent.
# On the following n lines, it will receive integer numbers. For each number, the program should print a different
# message:
# •If the number is 88 - "Hello"
# •	If the number is 86 - "How are you?"
# •	If the number is not 88 nor 86, and it is below 88 - "GREAT!"
# •	If the number is over 88 - "Bye."

number_of_messages = int(input())
for message in range(number_of_messages):
    current_message = int(input())
    output = ""
    if current_message == 88:
        output = "Hello"
    elif current_message == 86:
        output = "How are you?"
    elif (current_message != 88 and current_message != 86) and current_message < 88:
        output = "GREAT!"
    elif current_message > 88:
        output = "Bye."
    print(output)
